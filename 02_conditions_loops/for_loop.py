'''for loop explanation:
A for loop is used when we want to repeat an action a fixed number 
of times. 

range (1, 6) generates numbers from 1 to 5.
the loop runs once for each number.
each time it runs the current value is printed.'''

for i in range (1, 6):
    print(i) 

#example 2

#Step 1: Create an empty list

numbers = [] 


#Step 2: First for loop – filling the list
for i in range(1, 11):
    numbers.append(i)  

#Step 3: Prepare to calculate sum
total = 0

#Step 4: Second for loop – calculating sum
for num in numbers:
 total += num

#Step 5: Calculate average
average = total / len(numbers)

print("Numbers:", numbers)
print("Sum:", total)
print("Average:", average)



