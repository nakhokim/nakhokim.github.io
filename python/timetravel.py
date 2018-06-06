year = input("WHEN did you come from? ")
type(year)
year = int(year)
# probably there's a way to test if it's an integer. Google it.

def greetings():
    if year < 1900:
        print ("Welcome to the world of tomorrow")
    elif year >= 1900 and year < 2018:
        print ("Welcome to the world of today")
    else:
        print ("Welcome back in time")

greetings()
