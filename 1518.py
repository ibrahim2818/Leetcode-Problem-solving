# There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water bottles from the market with one full water bottle.

# The operation of drinking a full water bottle turns it into an empty bottle.

# Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.
a= int(input())
b= int(input())
total=a
while a>=b:
    newBottle=(a//b) 
    left= a%b
    newBottle=newBottle+left
    a=newBottle
    total= total+a -left
print(total)