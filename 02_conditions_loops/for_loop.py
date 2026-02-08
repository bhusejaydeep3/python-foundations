
FOR LOOP — Simple Explanation

A for loop is used when we know:
- how many times we want to repeat an action

Here:
range(1, 6) generates numbers from 1 to 5.
The loop runs once for each number.


# range(start, end) → end is not included
for i in range(1, 6):
    # i takes one value at a time: 1 → 2 → 3 → 4 → 5
    print(i)   # prints current value of i


example 2 

n = int(input("Enter a number: "))

total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum:", total)
