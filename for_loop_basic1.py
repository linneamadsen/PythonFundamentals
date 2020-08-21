print("Basic")
for x in range (0,151):
    print(x)

print("Multiples of Five")
for x in range (5, 1001, 5):
    print(x)

print("Counting, the Dojo Way")
for x in range(1, 101):
    if x % 5 == 0 and x % 10 !=0:
        print("Coding")
    elif x % 10 == 0:
        print("Coding Dojo")
    else: print(x)

print("Whoa. That Sucker's Huge")
sum = 0
for integer in range(0, 500001):
    if integer %2 == 0:
        sum = sum + integer
print(sum)

print("Countdown by Fours")
for year in range (2018, 0, -4):
    print(year)

print("Flexible Counter")
lowNum = 2
highNum = 9
mult = 3
for number in range(lowNum, highNum + 1):
    if number % mult == 0:
        print(number)
