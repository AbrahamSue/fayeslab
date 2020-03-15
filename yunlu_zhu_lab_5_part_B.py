# This program asks users to input values for mile, fahrenheit, gallon, pound and inch,
# Users must enter valid values for each input, or else there are 2 more attemps for
# a total of 3 attemps.
# Then convert each value to kilometer, celsius, liter, kilogram and centimeter,
# Then it displays the result at the end


# Get the value for each variable, and check if number is valid, if it's valid, move to
# the next variable, if not, there are 2 more attempts for a total of 3 attempts,
# then program proceeds or stops with an error message.
def main():
    mile = float(input('William, how many miles do you want to convert to kilometers? '))
    total = 0
    while mile < 0 and total < 2:
        print('Please enter a correct number for miles, you have 3 attempts. \
Attempt', total + 2, end='')
        mile = float(input(': '))
        total += 1
        if total == 2 and mile < 0:
            print('ERROR: you cannot enter a negative number for miles.')
    if mile >=0:
        milesToKm(mile)
        fahrenheit = float(input('\nWilliam, now tell me, what is the Fahrenheit \
you want to convert to Celsius? '))
        total = 0
        while fahrenheit >1000 and total < 2:
            print('Please enter a correct number for fahrenheit, you have 3 attempts. \
Attempt', total + 2, end='')
            fahrenheit = float(input(': '))
            total += 1
            if total == 2 and fahrenheit > 1000:
                print('ERROR: you cannot enter a value above 1000 degrees for fahrenheit.')
        if fahrenheit <= 1000:
            FahToCel(fahrenheit)
            gallon = float(input('\nWilliam, now tell me, how many gallons do you want \
to convert to liters? '))
            total = 0
            while gallon < 0 and total < 2:
                print('Please enter a correct number for gallons, you have 3 attempts. \
Attempt', total + 2, end='')
                gallon = float(input(': '))
                total += 1
                if total == 2 and gallon < 0:
                    print('ERROR: you cannot enter a negative number for gallons.')
            if gallon >= 0:
                GalToLit(gallon)
                pound = float(input('\nWilliam, now tell me, how many pounds do \
you want to convert to kilograms? '))
                total = 0
                while pound < 0 and total < 2:
                    print('Please enter a correct number for pounds, you have 3 \
attempts. Attempt',total + 2, end='')
                    pound = float(input(': '))
                    total += 1
                    if total == 2 and pound < 0:
                        print('ERROR: you cannot enter a negative number for pounds.')
                if pound >= 0:
                    PoundsToKg(pound)
                    inch = float(input('\nWilliam, lastly, how many inches do you want \
to convert to centimeters? '))
                    total = 0
                    while inch < 0 and total < 2:
                        print('Please enter a correct number for inches, you have 3 \
attempts. Attempt',total + 2, end='')
                        inch = float(input(': '))
                        total += 1
                        if total == 2 and inch < 0:
                            print('error: you cannot enter a negative number for inches.')
                    if inch >=0:
                        InchesToCm(inch)   

def milesToKm(mile):
    mileToKm = mile*1.6
    print(mile, 'miles is equal to', format(mileToKm, '.2f'), '\
kilometers, pretty cool huh?')

def FahToCel(fahrenheit):
    fahrenheitToCelsius = (fahrenheit - 32)*5/9
    print(fahrenheit, 'degrees fahrenheit is equal \
to', format(fahrenheitToCelsius, '.2f'), 'degrees Celsius, not bad right?')

def GalToLit(gallon):
    gallonToLiter = gallon*3.9
    print(gallon, 'gallons is equal to', format(gallonToLiter, '.2f'), 'liters, surprise!')

def PoundsToKg(pound):
    poundToKg = pound*0.45
    print(pound, 'pounds is equal \
to', format(poundToKg, '.2f'), 'kilograms, easy right?')

def InchesToCm(inch):
    inchToCm = inch*2.54
    print(inch, 'inches is equal to', format(inchToCm, '.2f'), 'centimeters, do you agree?')
    print('\nNow William, should you have more questions, run program again for more \
numbers! Again, welcome to America!')
                        
main()
                    
                                        


