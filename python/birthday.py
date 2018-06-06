birth_dates={"Stevens":1879, "Some guy":1945, "Other woman":1820}
def counter():
    counter1 = 0
    counter2 = 0
    for name, year in birth_dates.items():
        if year < 1901 and year > 1800:
            counter1 +=1
        elif year < 2001 and year > 1900:
            counter2 +=1
    counter1 = str(counter1)
    counter2 = str(counter2)
    print ("There are " + counter1 + " 19th C births and " + counter2 + " 20th C births in my collection." )

counter()
