# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field
from scrapy.contrib.loader.processor import TakeFirst, MapCompose
from scrapy.utils.markup import remove_entities
from scrapy.contrib.loader import XPathItemLoader

from numbeo.processors import filter_start_of_string, filter_end_of_string, convert_to_float, remove_initial_string
class NumbeoItemCpiBasic(Item):
    # define the fields for your item here like:
    # name = Field()
    #city = Field(
    #    input_processor = MapCompose(filter_start_of_string, filter_end_of_string))
    city = Field()
    country = Field(
        input_processor = MapCompose(remove_initial_string),
        output_processor = TakeFirst(),)
    consumer_price_index_excl_rent = Field(
        input_processor = MapCompose(convert_to_float),
        output_processor = TakeFirst(),) 
    rent_index = Field(
        input_processor = MapCompose(convert_to_float),
        output_processor = TakeFirst(),)
    groceries_index = Field(
        input_processor = MapCompose(convert_to_float),
        output_processor = TakeFirst(),)
    restaurants_index = Field(
        input_processor = MapCompose(convert_to_float),
        output_processor = TakeFirst(),)
    consumer_price_index_with_rent = Field(
        input_processor = MapCompose(convert_to_float),
        output_processor = TakeFirst(),)
    local_purchasing_power = Field(
        input_processor = MapCompose(convert_to_float),
        output_processor = TakeFirst(),)
    list_of_fields=['consumer_price_index_excl_rent','rent_index','groceries_index','restaurants_index','consumer_price_index_with_rent','local_purchasing_power']

class NumbeoItemCpiDetailRestaurant(Item):
    #restaurants
    country = Field()
    city = Field()
    meal_inexpensive_restaurant = Field()
    meal_for_2_mid_range_restaurant_three_course = Field()
    combo_meal_at_mcdonalds_or_similar = Field()
    domestic_beer_0_5_liter_draught = Field()
    imported_beer_0_33_liter_bottle = Field()
    cappuccino_Regular = Field()
    coke_pepsi_0_33_liter_bottle = Field()
    water_0_33_liter_bottle = Field()
    list_of_fields=['meal_inexpensive_restaurant','meal_for_2_mid_range_restaurant_three_course','combo_meal_at_mcdonalds_or_similar','domestic_beer_0_5_liter_draught','imported_beer_0_33_liter_bottle','cappuccino_Regular','coke_pepsi_0_33_liter_bottle','water_0_33_liter_bottle']

class NumbeoItemCpiDetailMarkets(Item):
    #markets
    country = Field()
    city = Field()
    milk_regular_1_liter = Field()
    loaf_of_fresh_white_bread_500g = Field()
    rice_1kg = Field()
    eggs_12 = Field()
    local_cheese_1kg = Field()
    chicken_breasts_boneless_skinless_1kg = Field()
    apples_1kg = Field()
    oranges_1kg = Field()
    tomato_1kg = Field()
    potato_1kg = Field()
    lettuce_1_head = Field()
    water_1_5_liter_bottle = Field()
    bottle_of_wine_mid_range = Field()
    domestic_beer_0_5_liter_bottle = Field()
    imported_beer_0_33_liter_bottle = Field()
    pack_of_cigarettes_marlboro = Field()
    list_of_fields = ['milk_regular_1_liter','loaf_of_fresh_white_bread_500g','rice_1kg','eggs_12','local_cheese_1kg','chicken_breasts_boneless_skinless_1kg','apples_1kg','oranges_1kg','tomato_1kg','potato_1kg','lettuce_1_head','water_1_5_liter_bottle','bottle_of_wine_mid_range','domestic_beer_0_5_liter_bottle','imported_beer_0_33_liter_bottle','pack_of_cigarettes_marlboro']
        
class NumbeoItemCpiDetailTransportation(Item):
    #transportation
    country = Field()
    city = Field()
    one_way_ticket_local_transport = Field()
    monthly_pass_regular_price = Field()
    taxi_start_normal_tariff = Field()
    taxi_1km_normal_tariff = Field()
    taxi_1hour_waiting_normal_tariff = Field()
    gasoline_1_liter = Field()
    volkswagen_golf_1_4_90_kw_trendline_or_equivalent_new_car = Field()
    list_of_fields = ['one_way_ticket_local_transport','monthly_pass_regular_price','taxi_start_normal_tariff','taxi_1km_normal_tariff','taxi_1hour_waiting_normal_tariff','gasoline_1_liter','volkswagen_golf_1_4_90_kw_trendline_or_equivalent_new_car']
    
class NumbeoItemCpiDetailUtilities(Item):
    #utilities_monthly
    country = Field()
    city = Field()
    basic_electricity_heating_water_garbage_for_85m2_apartment = Field()
    a_min_of_prepaid_mobile_tariff_local_no_discounts_or_plans = Field()
    internet_6_mbps_unlimited_data_cable_adsl = Field()
    list_of_fields = ['basic_electricity_heating_water_garbage_for_85m2_apartment','a_min_of_prepaid_mobile_tariff_local_no_discounts_or_plans','internet_6_mbps_unlimited_data_cable_adsl']
    
class NumbeoItemCpiDetailSports(Item):
    #sports_and_leisure
    country = Field()
    city = Field()
    fitness_club_monthly_fee_for_1_adult = Field()
    tennis_court_rent_1_hour_on_weekend = Field()
    cinema_international_release_1_seat = Field()
    list_of_fields = ['fitness_club_monthly_fee_for_1_adult','tennis_court_rent_1_hour_on_weekend','cinema_international_release_1_seat']
    
class NumbeoItemCpiDetailClothing(Item):
    #clothing_and_shoes
    country = Field()
    city = Field()
    pair_of_jeans_levis_501_or_similar = Field()
    summer_dress_in_a_chain_store_zara_h_and_m = Field()
    pair_of_nike_shoes = Field()
    pair_of_men_leather_shoes = Field()
    list_of_fields = ['pair_of_jeans_levis_501_or_similar','summer_dress_in_a_chain_store_zara_h_and_m','pair_of_nike_shoes','pair_of_men_leather_shoes']
    
class NumbeoItemCpiDetailRent(Item):
    #rent_per_month
    country = Field()
    city = Field()
    apartment_1_bedroom_in_city_centre = Field()
    apartment_1_bedroom_outside_of_centre = Field()
    apartment_3_bedrooms_in_city_centre = Field()
    apartment_3_bedrooms_outside_of_centre = Field()
    list_of_fields = ['apartment_1_bedroom_in_city_centre','apartment_1_bedroom_outside_of_centre','apartment_3_bedrooms_in_city_centre','apartment_3_bedrooms_outside_of_centre']
    
class NumbeoItemCpiDetailApartment(Item):
    #buy_apartment_price
    country = Field()
    city = Field()
    price_per_square_meter_to_buy_apartment_in_city_centre = Field()
    price_per_square_meter_to_buy_apartment_outside_of_centre = Field()
    list_of_fields = ['price_per_square_meter_to_buy_apartment_in_city_centre','price_per_square_meter_to_buy_apartment_outside_of_centre']
    
class NumbeoItemCpiDetailSalaries(Item):
    #salaries_and_financing
    country = Field()
    city = Field()
    median_monthly_disposable_salary_after_tax = Field()
    mortgage_interest_rate_in_percentange_yearly = Field()
    list_of_fields = ['median_monthly_disposable_salary_after_tax','mortgage_interest_rate_in_percentange_yearly']
    
class NumbeoItemCpiDetailStats(Item):
    #stats on entries
    country = Field()
    city = Field()
    number_of_entries = Field()
    entries_18_months = Field()
    last_update = Field()
    list_of_fields = ['number_of_entries','entries_18_months','last_update']
    '''
class NumbeoLoader(XPathItemLoader):
    default_input_processor = MapCompose(convert_to_float)
    default_output_processor = TakeFirst()

    country_in = MapCompose(remove_initial_string)
    '''
