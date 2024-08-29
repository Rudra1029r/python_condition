year = 2024;

if  (year%400 == 0) or (year%4 == 0  and year%100 != 0):
    show = "THIS IS A LEAP YEAR"
else :
    show = "THIS  IS NOT A LEAP YEAR"
    
print(show);    