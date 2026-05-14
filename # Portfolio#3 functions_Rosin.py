# Portfolio#3 functions

# this portfolio is about temperature conversion

#converting the input of the user to celsius
def to_cel(unit,value):
    if unit == "Celsius":
        return value
    elif unit == "Fahrenheit":
        return (value - 32) * 5/9
    elif unit == "Kelvin":
        return value - 273.15
    elif unit == "Rankine":
        return (value - 491.67) * 5/9

#converting the celsius value calculated above into other units
def from_cel(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    rankine = kelvin * 1.8
    return fahrenheit, kelvin, rankine
# this is the main program, where the user is asked for inputs like the given unit and value they would like to convert
unit = (input("Enter the given unit (Celsius, Fahrenheit, Kelvin, Rankine): ")).capitalize()

value = float(input("Enter the value of the unit: "))

# in case the user inputs an invalid unit 
if unit not in ["Celsius", "Fahrenheit", "Kelvin", "Rankine"]:
    print("Error: Invalid Unit Entered!")
    exit()

# using the def function above, the inputs is translated into the expected temperature output

#convert to celsius first
else:
    Celsius = to_cel(unit, value)

# convert from celsius to other temps

fahrenheit, kelvin, rankine = from_cel(Celsius)

# output of the conversion in the nearest hundredths
print("===== TEMPERATURE CONVERSIONS ======")
print(f"Celsius: {Celsius:.2f} C")
print(f"Fahrenheit: {fahrenheit:.2f} F")
print(f"Kelvin: {kelvin:.2f} K")
print(f"Rankine: {rankine:.2f} R")





