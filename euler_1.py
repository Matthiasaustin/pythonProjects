#Euler Problem 1

# If we list all the natural numbers below 10 that are 
# multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples
# is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


# initiallizes a list holding all numbers between 3 and 999 to draw from 
working_list = list(range(3,1000))

#initializes list to hold the numbers once sorted
problem_list = []

#initializes value to hold final answer
answer = 0

#for loop that works through the whole working list of numbers between 3 and 999 and then sorts by modulo whether a number is a multiple of 3 or 5 and then appends it to problem list
for num in working_list:
	if num % 3 == 0:
		problem_list.append(num)
	elif num % 5 == 0:
		problem_list.append(num)
	
#sums the problem list of all multiples of 3 and 5 < 1000 and then prints
answer = sum(problem_list)
print (answer)		