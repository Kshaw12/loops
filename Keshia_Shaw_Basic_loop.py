# Basic print integers 0-150
for x in range(0,151,1):
    print(x)

# multiples-print multiple of 5
for a in range(5,1001,5):
    print(a*5)

# Dojo Counting
def dojo_counting():
    for i in range(0,101,1):
        if i % 5 == 0:
            print('Coding')
        elif i % 10 == 0:
            print('Coding Dojo')
dojo_counting()

# Sucker Huge
minimum = 0
maximum = 5000
total = 0
if x in range(minimum, maximum + 1):
    if x % 2 != 0:
        print("{0}".format(x))
        total = total + x
print("The final sum=".format(minimum, maximum, total))

# Countdown by fours
def count_down_fours():
    number = 2018
    while number > 0:
        print(number)
        number = number - 4
count_down_fours()


# Flexible counter
def flex_counter(low, high, multi):
    for i in range(low, high+1):
        if i % multi == 0:
            print (i)
flex_counter(2,9,3)

