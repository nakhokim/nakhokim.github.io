year = 2000

def greetings():
    if year < 1900:
        print ("Welcome to the world of tomorrow")
    elif year >= 1900 and year < 2018:
        print ("Welcome to the world of today")
    else:
        print ("Welcome back in time")

greetings()
