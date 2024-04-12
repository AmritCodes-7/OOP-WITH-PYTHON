# to find if a number is prime or not 

num = int(input("Enter a num: "))
prime = True
i = 2
for i in range(2, num):
    if(num % i == 0 and num != 2):
        prime = False
        break

if prime:
    print("The number is prime.")
else:
    print("The number is not prime.")
    

