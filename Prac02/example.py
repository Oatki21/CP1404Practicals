name = "Gibson L-5 CES"
year = 1922
cost = 16035.40
# The ‘old’ manual way to format text:
print("My guitar: " + name + ", first made in " + str(year))
# A better way using str.format():
print("My guitar: {}, first made in {}".format(name, year))
print("My guitar: {0}, first made in {1}".format(name, year))
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))
# Formatting currency:
print("My {} would cost ${:,.2f}".format(name, cost))
# Aligning columns:
numbers = [1, 19, 123, 456, -25]
for i in range(len(numbers)):
 print("Number {0} is {1:>5}".format(i + 1, numbers[i]))

#import random
 #print(random.randint(5, 20)) # line 1
#Smallest answer: 5. Biggest answer: 20.
#print(random.randrange(3, 10, 2)) # line 2
 #smallest answer: 3. Biggest answer: 9
#print(random.uniform(2.5, 5.5)) # line 3
 #smallest answer: 2.500000000 Biggest answer: 5.500000000