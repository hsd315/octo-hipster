from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.http import Request
from scrapy.http import HtmlResponse
from scrapy.http import FormRequest
from scrapy import log

from numbeo.processors import my_float
#from numbeo.items import NumbeoItemCpiBasic 
#from numbeo.items import NumbeoItemCpiDetailRestaurant 
#from numbeo.items import NumbeoItemCpiDetailMarkets
from numbeo import items
import re
import datetime

class NumbeoSpider(CrawlSpider):
    name = 'numbeo_crawl'
    allowed_domains = ['numbeo.com']
    start_urls = ['http://www.numbeo.com/cost-of-living/']

    rules = (Rule(
        SgmlLinkExtractor(allow=("country_result.jsp\?country=*","city_result.jsp\?country=*",)), 
        follow=True), )

    def _urljoin(self, response, url):
        """Helper to convert relative urls to absolute"""
        return urljoin_rfc(response.url, url, response.encoding)

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        countries = hxs.select("/html/body/div[4]/span/table/tr/td/a/@href")
        for country in countries:
            relative_url = country.extract()+'&displayCurrency=USD'
            url = self._urljoin(response,relative_url)
            yield Request(url, callback = self.parse_cpi)


    def fill_country_and_city(self, itemclass,hxs,city_level_data):
        item = itemclass
        item['country'] = hxs.select(
            "//*[@class='breadcrumb-outer']//td[1]//a[3]/text()").extract()[0].encode('ascii',errors='ignore')
        if city_level_data:
            item['city'] = hxs.select(
                "//*[@class='breadcrumb-outer']//td[1]//a[4]/text()").extract()[0].encode('ascii',errors='ignore')
        else:
            item['city'] = 'country_level_data'

    def parse_helper(
        self, 
        hxs, 
        itemclass, 
        counter_value, 
        hxs_general_selector_string = "//*[@class='data_wide_table']",
        hxs_element_selector_string1 = '(//tr[', 
        hxs_element_selector_string2 = ']//td[2]/text())[1]',
        city_level_data = False
        ):
        numtype_regex = re.compile(r'[^\d.]+')
        cpi_detail_items = []
        cpi_detail_values = hxs.select(hxs_general_selector_string)
	#If table does not exist, return a set of values (country followed by -1s for every field)
        if len(cpi_detail_values) == 0:
            item = fill_country_and_city(itemclass,hxs,city_level_data):
            for var_name in item.list_of_fields:
                item[var_name] = -1
        for cpi_value in cpi_detail_values:
            item = fill_country_and_city(itemclass,hxs,city_level_data)
            for var_name in item.list_of_fields:
                #.encode() - converts to ascii and ignores any characters that 
                #cannot be converted
                item[var_name] = my_float(
                    numtype_regex.sub(
                    '', cpi_value.select(
                    hxs_element_selector_string1+str(counter_value)+hxs_element_selector_string2
                    ).extract()[0].encode('ascii',errors='ignore')
                    )
                )
                counter_value+=1
            cpi_detail_items.append(item)
        return item


    def parse_stats(
        self, 
        hxs, 
        itemclass, 
        hxs_selector_string1 = "/html/body/div[4]",
        city_level_data = False
        ):
        item = itemclass
        item['country'] = hxs.select(
            "//*[@class='breadcrumb-outer']//td[1]//a[3]/text()"\
            ).extract()[0].encode('ascii',errors='ignore')
        if city_level_data:
            item['city'] = hxs.select(
                "//*[@class='breadcrumb-outer']//td[1]//a[4]/text()"\
                ).extract()[0].encode('ascii',errors='ignore')
        else:
            item['city'] = 'country_level_data'
        #temp, temp2 and temp3 can be combined into one
        #statement, however, they are easier to understand this way 
        temp =  hxs.select(hxs_selector_string1).extract()[0].encode('ascii',errors='ignore')
        temp2 = temp.split("These data are based on ")[1]
        temp3 = temp2.split('\n')[0]
        entries = [int(s) for s in temp3.split() if s.isdigit()]
        item['number_of_entries'] = int(entries[0])
        item['entries_18_months'] = int(entries[2])
        temp4 = temp2.split('\n')[1]
        date_string = temp4.split(':')[1].strip()
        #Note that we are fitting day as 01 and time as 00:00:00.000
        #This does not accurately reflect proper day or time,
        #However it converts to proper sql date format and we don't need day
        #level of accuracy for our date
        date_format = datetime.datetime.strptime(date_string, '%B, %Y').strftime('%Y-%m-01 00:00:00.000')
        item['last_update'] = date_format
        return item


    def parse_cpi(self, response):
        hxs = HtmlXPathSelector(response)
        if 'city_result.jsp' in response.url:
            city_level_data_bool = True
        else:
            city_level_data_bool = False

        #CPI basic fields
        temp_item = items.NumbeoItemCpiBasic()
        general_selector_string = "//*[@class='table_indexes']"
        item = self.parse_helper(
            hxs = hxs,
            itemclass = temp_item,
            counter_value = 2,
            hxs_general_selector_string = general_selector_string,
            city_level_data = city_level_data_bool
        )
        yield item
        #CPI restaurant detail fields
        temp_item = items.NumbeoItemCpiDetailRestaurant()
        general_selector_string = "//*[@class='data_wide_table']"
        element_selector_string1 = '(//tr['
        element_selector_string2 = ']//td[2]/text())[1]'
        item = self.parse_helper(
            hxs = hxs,
            itemclass = temp_item,
            counter_value = 4,
            city_level_data = city_level_data_bool
        )
        yield item
        #CPI markets detail fields
        temp_item = items.NumbeoItemCpiDetailMarkets()
        item = self.parse_helper(
            hxs = hxs,
            itemclass = temp_item,
            counter_value = 14,
            city_level_data = city_level_data_bool
        )
        yield item
        #CPI transportation detail fields
        temp_item = items.NumbeoItemCpiDetailTransportation()
        item = self.parse_helper(
            hxs = hxs,
            itemclass = temp_item,
            counter_value = 32,
            city_level_data = city_level_data_bool
        )
        yield item
        #CPI utilities detail fields
        temp_item = items.NumbeoItemCpiDetailUtilities()
        item = self.parse_helper(
            hxs = hxs,
            itemclass = temp_item,
            counter_value = 41,
            city_level_data = city_level_data_bool
        )
        yield item
        #CPI sports detail fields
        temp_item = items.NumbeoItemCpiDetailSports()
        item = self.parse_helper(
            hxs = hxs,
            itemclass = temp_item,
            counter_value = 46,
            city_level_data = city_level_data_bool
        )
        yield item
        #CPI clothing detail fields
        temp_item = items.NumbeoItemCpiDetailClothing()
        item = self.parse_helper(
            hxs = hxs,
            itemclass = temp_item,
            counter_value = 51,
            city_level_data = city_level_data_bool
        )
        yield item
        #CPI rent detail fields
        temp_item = items.NumbeoItemCpiDetailRent()
        item = self.parse_helper(
            hxs = hxs,
            itemclass = temp_item,
            counter_value = 57,
            city_level_data = city_level_data_bool
        )
        yield item
        #CPI apartment detail fields
        temp_item = items.NumbeoItemCpiDetailApartment()
        item = self.parse_helper(
            hxs = hxs,
            itemclass = temp_item,
            counter_value = 63,
            city_level_data = city_level_data_bool
        )
        yield item
        #CPI salaries detail fields
        temp_item = items.NumbeoItemCpiDetailSalaries()
        item = self.parse_helper(
            hxs = hxs,
            itemclass = temp_item,
            counter_value = 67,
            city_level_data = city_level_data_bool
        )
        yield item
        #CPI stats detail fields
        temp_item = items.NumbeoItemCpiDetailStats()
        item = self.parse_stats(
            hxs = hxs,
            itemclass = temp_item,
            city_level_data = city_level_data_bool
        )
        yield item

    
        #Once we are done importing country level data on the country_result page
        #we move on to extracting city level data  
        if 'city_result.jsp' not in response.url:
            values = hxs.select("//*[@id='city']/option/text()").extract()
            form_responce_url_list=[]
            for value in values:
                # we are not yielding FormRequest directly, because we need to append the 
                #url with displayCurrency in order to get normalized output for all
                #countries and cities. We simply use the URL from FormRequest and get back
                #data from url with displayCurrency appended. 
                #It would be possible to yield to FormRequest and then go to page and have
                #another formrequest to choose currency, but that only means that we are
                #sending GET request to a page without scraping any data from it
                temp_url = (FormRequest.from_response(response,formdata={'city':value}).url)
                url = temp_url+'&displayCurrency=USD'
                if '--- Select city---' in url:
                    pass
                else:
                    yield Request(url, callback = self.parse_cpi)