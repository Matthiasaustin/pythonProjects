# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
x = 0
num = 1
fib_list = []

while num < 4000000 :
	added = x + num
	fib_list.append(added)
	x = num
	num = added

print (fib_list)
final_list = []
for num in fib_list:
	if num % 2 == 0:
		final_list.append(num)
answer = sum (final_list)
print (answer)