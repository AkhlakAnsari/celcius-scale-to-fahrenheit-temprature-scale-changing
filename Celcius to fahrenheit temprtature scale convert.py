#Celcius to Fahrenheit temprature scale convertion using def and input from user
def convert(c):
    F = (9/5)*c + 32
    return (F)
#F= fahrenheit
#C= celcius
celcius = float(input("Enter the temperature: "))
Fahrenheit = convert(celcius)
print ("The temperature in Fahrenheit is ",round(Fahrenheit,2))
# thanks akhlakansari94@gmail.com
