import random
def randInt(min=   0, max=   100):
    if min > max:
        print ("Min can't be greater than max!")
        return "Min can't be greater than max!"
    if max < 0:
        print ("Max can't be less than 0!")
        return "Max can't be less than 0!"
    num = round(random.random()*max)
    print(num)
#print(randInt()) 		    # should print a random integer between 0 to 100
#print(randInt(max=50)) 	    # should print a random integer between 0 to 50
#print(randInt(min=50)) 	    # should print a random integer between 50 to 100
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500

randInt(-10, -2)
