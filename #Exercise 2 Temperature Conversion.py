#Exercise 2 Temperature Conversion 

#fahrenheit = float(input("What is temperature in degrees Fahrenheit?"))

#celsius = (fahrenheit - 32) * 5/9
#kelvin = (celsius + 273.15)
#rankine = (kelvin * 1.8)
#print(f"The temperature is {celsius} in degrees Celsius")
#print(f"The temperature is {kelvin} in degrees Kelvin")
#print(f"The temperature is {rankine} in degrees Rakine")

unit = input("What unit of temperature was initially given to you (Celsius, Fahrenheit, Kelvin, Rankine)? ").capitalize()
temp = float(input("Enter the given value: "))
if unit == "Celsius":
    celsius = temp
    fahrenheit = (celsius * 9/5) + 32
    kelvin = (celsius + 273.15)
    rankine = (celsius + 273.15) * 1.8
elif unit == "Fahrenheit":
    fahrenheit = temp
    celsius = (fahrenheit - 32) * 5/9
    kelvin = celsius - 273.15
    rankine = kelvin * 1.8
elif unit == "Kelvin":
    kelvin = temp
    celsius = kelvin + 273.15
    fahrenheit = (celsius * 9/5) + 32
    rankine = (celsius + 273.15) * 1.8
elif unit == "Rankine":
    rankine = temp
    kelvin = rankine / 1.8
    celsius = kelvin + 273.15
    fahrenheit = (celsius * 9/5) + 32
else:
    print("Error: Invalid Unit Entered!")
    exit()

print(f"Conversions for {temp}{unit.capitalize()}")
print(f"Celsius: {celsius: .2f} degrees Celsius")
print(f"Fahrenheit: {fahrenheit: .2f} degrees Fahrenheit")
print(f"Kelvin: {kelvin: .2f} degrees Kelvin")
print(f"Rankine: {rankine: .2f} degrees Rankine")