
def milesToKm(mi):
    km = 1.60934 * mi
    print "%.2f mile equals to %.2f kilometer" % (mi, km)
    return km


def FahToCel(fah):
    cel = (fah - 32) * 5 / 9
    print "%.2f Fahrenheit equals to %.2f celsius" % (fah, cel)
    return cel


def GalToLit(gal):
    lit = 3.78541 * gal
    print "%.2f Gallon equals to %.2f Litter" % (gal, lit)
    return lit


def PoundsToKg(pd):
    kg = 0.453592 * pd
    print "%.2f pounds equals to %.2f Kg" % (pd, kg)
    return kg


def InchesToCm(i):
    cm = 2.54 * i
    print "%.2f inchs equals to %.2f cm" % (i, cm)
    return i


def main():
    attempt = 0
    miles = -1
    fah = -1
    gal = -1
    pd = -1
    inches = -1
    while attempt < 3 and miles < 0:
        attempt += 1
        miles = float(input("Please provide your input for miles: "))
    if miles >= 0:
        attempt = 0
        milesToKm(miles)

    while attempt < 3 and fah < 0:
        attempt += 1
        fah = float(input("Please provide your input for tempeture: "))
    if fah >= 0:
        attempt = 0
        FahToCel(fah)

    while attempt < 3 and gal < 0:
        attempt += 1
        gal = float(input("Please provide your input for gal: "))
    if gal >= 0:
        attempt = 0
        GalToLit(gal)

    while attempt < 3 and pd < 0:
        attempt += 1
        pd = float(input("Please provide your input for pounds: "))
    if pd >= 0:
        attempt = 0
        PoundsToKg(pd)

    while attempt < 3 and inches < 0:
        attempt += 1
        inches = float(input("Please provide your input for inches: "))
    if inches >= 0:
        attempt = 0
        InchesToCm(inches)


if __name__ == '__main__':
    main()
