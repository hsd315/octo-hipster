# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import sqlite3

class NumbeoPipeline(object):
    def __init__(self):
        self.conn = sqlite3.connect('basic_cpi.db')
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            if item['consumer_price_index_excl_rent']:
                pass
        except:
            pass
        else:
             self.cur.execute(
                 "insert into cpibasic\
                 (\
                 country,\
                 city,\
                 consumer_price_index_excl_rent,\
                 consumer_price_index_with_rent,\
                 groceries_index,\
                 local_purchasing_power,\
                 rent_index,\
                 restaurants_index\
                 ) values(?,?,?,?,?,?,?,?)",(
                 item['country'],
                 item['city'],
                 item['consumer_price_index_excl_rent'],
                 item['consumer_price_index_with_rent'],
                 item['groceries_index'],
                 item['local_purchasing_power'],
                 item['rent_index'],
                 item['restaurants_index'])
             )
        try:
            if item['meal_inexpensive_restaurant']:
                pass
        except:
            pass
        else:
             self.cur.execute(
                 "insert into cpidetail_restaurant\
                 (\
                 country,\
                 city,\
                 meal_inexpensive_restaurant,\
                 meal_for_2_mid_range_restaurant_three_course,\
                 combo_meal_at_mcdonalds_or_similar,\
                 domestic_beer_0_5_liter_draught,\
                 imported_beer_0_33_liter_bottle,\
                 cappuccino_Regular,\
                 coke_pepsi_0_33_liter_bottle,\
                 water_0_33_liter_bottle\
                 ) values(?,?,?,?,?,?,?,?,?,?)",(
                 item['country'],
                 item['city'],
                 item['meal_inexpensive_restaurant'],
                 item['meal_for_2_mid_range_restaurant_three_course'],
                 item['combo_meal_at_mcdonalds_or_similar'],
                 item['domestic_beer_0_5_liter_draught'],
                 item['imported_beer_0_33_liter_bottle'],
                 item['cappuccino_Regular'],
                 item['coke_pepsi_0_33_liter_bottle'],
                 item['water_0_33_liter_bottle']
                 )
             )
        try:
            if item['milk_regular_1_liter']:
                pass
        except:
            pass
        else:
             self.cur.execute(
                 "insert into cpidetail_markets\
                 (\
                 country,\
                 city,\
                 milk_regular_1_liter,\
                 loaf_of_fresh_white_bread_500g,\
                 rice_1kg,\
                 eggs_12,\
                 local_cheese_1kg,\
                 chicken_breasts_boneless_skinless_1kg,\
                 apples_1kg,\
                 oranges_1kg,\
                 tomato_1kg,\
                 potato_1kg,\
                 lettuce_1_head,\
                 water_1_5_liter_bottle,\
                 bottle_of_wine_mid_range,\
                 domestic_beer_0_5_liter_bottle,\
                 imported_beer_0_33_liter_bottle,\
                 pack_of_cigarettes_marlboro\
                 ) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(
                 item['country'],
                 item['city'],
                 item['milk_regular_1_liter'],
                 item['loaf_of_fresh_white_bread_500g'],
                 item['rice_1kg'],
                 item['eggs_12'],
                 item['local_cheese_1kg'],
                 item['chicken_breasts_boneless_skinless_1kg'],
                 item['apples_1kg'],
                 item['oranges_1kg'],
                 item['tomato_1kg'],
                 item['potato_1kg'],
                 item['lettuce_1_head'],
                 item['water_1_5_liter_bottle'],
                 item['bottle_of_wine_mid_range'],
                 item['domestic_beer_0_5_liter_bottle'],
                 item['imported_beer_0_33_liter_bottle'],
                 item['pack_of_cigarettes_marlboro'],
                 )
             )

        try:
            if item['one_way_ticket_local_transport']:
                pass
        except:
            pass
        else:
             self.cur.execute(
                 "insert into cpidetail_transportation\
                 (\
                 country,\
                 city,\
                 one_way_ticket_local_transport,\
                 monthly_pass_regular_price,\
                 taxi_start_normal_tariff,\
                 taxi_1km_normal_tariff,\
                 taxi_1hour_waiting_normal_tariff,\
                 gasoline_1_liter,\
                 volkswagen_golf_1_4_90_kw_trendline_or_equivalent_new_car\
                 ) values(?,?,?,?,?,?,?,?,?)",(
                 item['country'],
                 item['city'],
                 item['one_way_ticket_local_transport'],
                 item['monthly_pass_regular_price'],
                 item['taxi_start_normal_tariff'],
                 item['taxi_1km_normal_tariff'],
                 item['taxi_1hour_waiting_normal_tariff'],
                 item['gasoline_1_liter'],
                 item['volkswagen_golf_1_4_90_kw_trendline_or_equivalent_new_car']
                 )
             )
        try:
            if item['basic_electricity_heating_water_garbage_for_85m2_apartment']:
                pass
        except:
            pass
        else:
             self.cur.execute(
                 "insert into cpidetail_utilities\
                 (\
                 country,\
                 city,\
                 basic_electricity_heating_water_garbage_for_85m2_apartment,\
                 a_min_of_prepaid_mobile_tariff_local_no_discounts_or_plans,\
                 internet_6_mbps_unlimited_data_cable_adsl\
                 ) values(?,?,?,?,?)",(
                 item['country'],
                 item['city'],
                 item['basic_electricity_heating_water_garbage_for_85m2_apartment'],
                 item['a_min_of_prepaid_mobile_tariff_local_no_discounts_or_plans'],
                 item['internet_6_mbps_unlimited_data_cable_adsl']
                 )
             )
        try:
            if item['fitness_club_monthly_fee_for_1_adult']:
                pass
        except:
            pass
        else:
             self.cur.execute(
                 "insert into cpidetail_sports\
                 (\
                 country,\
                 city,\
                 fitness_club_monthly_fee_for_1_adult,\
                 tennis_court_rent_1_hour_on_weekend,\
                 cinema_international_release_1_seat\
                 ) values(?,?,?,?,?)",(
                 item['country'],
                 item['city'],
                 item['fitness_club_monthly_fee_for_1_adult'],
                 item['tennis_court_rent_1_hour_on_weekend'],
                 item['cinema_international_release_1_seat']
                 )
             )
        try:
            if item['pair_of_jeans_levis_501_or_similar']:
                pass
        except:
            pass
        else:
             self.cur.execute(
                 "insert into cpidetail_clothing\
                 (\
                 country,\
                 city,\
                 pair_of_jeans_levis_501_or_similar,\
                 summer_dress_in_a_chain_store_zara_h_and_m,\
                 pair_of_nike_shoes,\
                 pair_of_men_leather_shoes\
                 ) values(?,?,?,?,?,?)",(
                 item['country'],
                 item['city'],
                 item['pair_of_jeans_levis_501_or_similar'],
                 item['summer_dress_in_a_chain_store_zara_h_and_m'],
                 item['pair_of_nike_shoes'],
                 item['pair_of_men_leather_shoes']
                 )
             )
        try:
            if item['apartment_1_bedroom_in_city_centre']:
                pass
        except:
            pass
        else:
             self.cur.execute(
                 "insert into cpidetail_rent\
                 (\
                 country,\
                 city,\
                 apartment_1_bedroom_in_city_centre,\
                 apartment_1_bedroom_outside_of_centre,\
                 apartment_3_bedrooms_in_city_centre,\
                 apartment_3_bedrooms_outside_of_centre\
                 ) values(?,?,?,?,?,?)",(
                 item['country'],
                 item['city'],
                 item['apartment_1_bedroom_in_city_centre'],
                 item['apartment_1_bedroom_outside_of_centre'],
                 item['apartment_3_bedrooms_in_city_centre'],
                 item['apartment_3_bedrooms_outside_of_centre']
                 )
             )
        try:
            if item['price_per_square_meter_to_buy_apartment_in_city_centre']:
                pass
        except:
            pass
        else:
             self.cur.execute(
                 "insert into cpidetail_apartment\
                 (\
                 country,\
                 city,\
                 price_per_square_meter_to_buy_apartment_in_city_centre,\
                 price_per_square_meter_to_buy_apartment_outside_of_centre\
                 ) values(?,?,?,?)",(
                 item['country'],
                 item['city'],
                 item['price_per_square_meter_to_buy_apartment_in_city_centre'],
                 item['price_per_square_meter_to_buy_apartment_outside_of_centre']
                 )
             )
        try:
            if item['median_monthly_disposable_salary_after_tax']:
                pass
        except:
            pass
        else:
             self.cur.execute(
                 "insert into cpidetail_salaries\
                 (\
                 country,\
                 city,\
                 median_monthly_disposable_salary_after_tax,\
                 mortgage_interest_rate_in_percentange_yearly\
                 ) values(?,?,?,?)",(
                 item['country'],
                 item['city'],
                 item['median_monthly_disposable_salary_after_tax'],
                 item['mortgage_interest_rate_in_percentange_yearly']
                 )
             )
        try:
            if item['entries_18_months']:
                pass
        except:
            pass
        else:
             self.cur.execute(
                 "insert into cpidetail_stats\
                 (\
                 country,\
                 city,\
                 number_of_entries,\
                 entries_18_months,\
                 last_update\
                 ) values(?,?,?,?,?)",(
                 item['country'],
                 item['city'],
                 item['number_of_entries'],
                 item['entries_18_months'],
                 item['last_update']
                 )
             )



        self.conn.commit()
        return item
