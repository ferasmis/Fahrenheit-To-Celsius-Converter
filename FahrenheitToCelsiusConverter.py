## Author: Feras
## Description: Fahrenheit to Celsius converter
## Formula: (fahrenheit - 32) * (5/9)


fahrenheit = float(input("Enter fahrenheit degrees: "))
def fhTocCel(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    return celsius
print("The degrees in Celsius is: " + str(fhTocCel(fahrenheit)))