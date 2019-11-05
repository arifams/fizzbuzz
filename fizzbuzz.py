print('a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”')

f = 'Fizz'
b = 'Buzz'
fb = f + b

print('------')
print('1st method')
print('using elif')
print('------')

for line in range(1, 101) :
	if line % 3 == 0 and line % 5 == 0 :
		print(f,b)
	elif line % 3 == 0 :
		print(b)
	elif line % 5 == 0 :
		print(b)
	else :
		print(line)

print('------')
print('a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”')
print('------')
print('2st method')
print('------')

for line in range(1, 101):
    string = ''
    if line % 3 == 0 :
        string = string + f
    if line % 5 == 0 :
        string = string + b
    if line % 5 != 0 and line % 3 != 0:
        string = string + str(line)
    print(string)