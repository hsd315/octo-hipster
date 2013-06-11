import sqlite3
conn = sqlite3.connect("basic_cpi.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE cpibasic
(
country TEXT,
city TEXT,
consumer_price_index_excl_rent REAL,
consumer_price_index_with_rent REAL,
groceries_index REAL,
local_purchasing_power REAL,
rent_index REAL,
restaurants_index REAL
)""")

cursor.execute("""CREATE TABLE cpidetail_restaurant
(
country TEXT,
city TEXT,
meal_inexpensive_restaurant REAL,
meal_for_2_mid_range_restaurant_three_course REAL,
combo_meal_at_mcdonalds_or_similar REAL,
domestic_beer_0_5_liter_draught REAL,
imported_beer_0_33_liter_bottle REAL,
cappuccino_Regular REAL,
coke_pepsi_0_33_liter_bottle REAL,
water_0_33_liter_bottle REAL
)""")

cursor.execute("""CREATE TABLE cpidetail_markets
(
country TEXT,
city TEXT,
milk_regular_1_liter REAL,
loaf_of_fresh_white_bread_500g REAL,
rice_1kg REAL,
eggs_12 REAL,
local_cheese_1kg REAL,
chicken_breasts_boneless_skinless_1kg REAL,
apples_1kg REAL,
oranges_1kg REAL,
tomato_1kg REAL,
potato_1kg REAL,
lettuce_1_head REAL,
water_1_5_liter_bottle REAL,
bottle_of_wine_mid_range REAL,
domestic_beer_0_5_liter_bottle REAL,
imported_beer_0_33_liter_bottle REAL,
pack_of_cigarettes_marlboro REAL
)""")


cursor.execute("""CREATE TABLE cpidetail_transportation
(
country TEXT,
city TEXT,
one_way_ticket_local_transport REAL,
monthly_pass_regular_price REAL,
taxi_start_normal_tariff REAL,
taxi_1km_normal_tariff REAL,
taxi_1hour_waiting_normal_tariff REAL,
gasoline_1_liter REAL,
volkswagen_golf_1_4_90_kw_trendline_or_equivalent_new_car REAL
)""")
cursor.execute("""CREATE TABLE cpidetail_utilities 
(
country TEXT,
city TEXT,
basic_electricity_heating_water_garbage_for_85m2_apartment REAL,
a_min_of_prepaid_mobile_tariff_local_no_discounts_or_plans REAL,
internet_6_mbps_unlimited_data_cable_adsl REAL
)""")
cursor.execute("""CREATE TABLE cpidetail_sports 
(
country TEXT,
city TEXT,
fitness_club_monthly_fee_for_1_adult REAL,
tennis_court_rent_1_hour_on_weekend REAL,
cinema_international_release_1_seat REAL
)""")
cursor.execute("""CREATE TABLE cpidetail_clothing 
(
country TEXT,
city TEXT,
pair_of_jeans_levis_501_or_similar REAL,
summer_dress_in_a_chain_store_zara_h_and_m REAL,
pair_of_nike_shoes REAL,
pair_of_men_leather_shoes REAL
)""")
cursor.execute("""CREATE TABLE cpidetail_rent 
(
country TEXT,
city TEXT,
apartment_1_bedroom_in_city_centre REAL,
apartment_1_bedroom_outside_of_centre REAL,
apartment_3_bedrooms_in_city_centre REAL,
apartment_3_bedrooms_outside_of_centre REAL
)""")
cursor.execute("""CREATE TABLE cpidetail_apartment 
(
country TEXT,
city TEXT,
price_per_square_meter_to_buy_apartment_in_city_centre REAL,
price_per_square_meter_to_buy_apartment_outside_of_centre REAL
)""")
cursor.execute("""CREATE TABLE cpidetail_salaries 
(
country TEXT,
city TEXT,
median_monthly_disposable_salary_after_tax REAL,
mortgage_interest_rate_in_percentange_yearly REAL
)""")
cursor.execute("""CREATE TABLE cpidetail_stats 
(
country TEXT,
city TEXT,
number_of_entries REAL,
entries_18_months REAL,
last_update TEXT
)""")
