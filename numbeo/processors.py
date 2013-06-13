def my_float(a):
   try:
       a = float(a)
   except ValueError,e:
       a = -1.0
   return a