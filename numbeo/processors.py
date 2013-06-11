
def filter_start_of_string(heading):
    return heading[len('Cost of Living in '):]
def filter_end_of_string(heading):
    return heading[:-1*len(', India')]
def convert_to_float(number_in_string_form):
    return float(number_in_string_form)
def remove_initial_string(price_country_string):
    return price_country_string[len('price_country_string'):]
def my_float(a):
   try:
       a = float(a)
   except ValueError,e:
       a = -1.0
   return a

