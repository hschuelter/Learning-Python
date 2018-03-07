def fibonacci_list(number):
	lista = [0,1]

	while len(lista) <= number:
		front = len(lista) - 1
		num = lista[front] + lista[front - 1]
		lista.append(num)

	return lista.pop()

def fibonice(num, value = 1, prev = 0):
	if num == 0:
		return prev
	if num == 1:
		return value

	return fibonice(num-1, value+prev, value)

def fibo_recur(number):

	if number <= 1:
		return number

	return fibo_recur(number-1) + fibo_recur(number-2)



print "Calculating the n-th number of Fibonacci sequence:"
print "    1 - with lists:\t" + str( fibonacci_list(35) )
print "    2 - with recursion: " + str( fibonice(35,1,0) ) + " (faster)"
print "    3 - with recursion: " + str( fibo_recur(35) ) + " (slower)"