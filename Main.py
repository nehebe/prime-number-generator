from math import sqrt

# n is the number to be check whether it is prime or not
n = int(input("What number do you want to start from: "))
 

def isPrime(n):
	prime_flag = 0
	 
	if(n > 1):
	    for i in range(2, int(sqrt(n)) + 1):
	        if (n % i == 0):
	            prime_flag = 1
	            break
	    if (prime_flag == 0):
	        return True
	    else:
	        return False
	else:
	    return False

def Check(num):
	curnum = num + 1
	flag = 0
	while flag == 0:
		if isPrime(curnum) == True:
			flag = 1
		else:
			curnum += 1
	return curnum


print(Check(n)) 
user_input = input("Would you like to see the next prime number? (yes/no): ")
while user_input.lower() == "yes" or user_input.lower() == "y":
	n = Check(n + 1)
	print(Check(n))
	user_input = input("Would you like to see the next prime number? (yes/no): ")

exit()


		

