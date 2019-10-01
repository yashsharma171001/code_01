def factorial(n):
    if n==1 :
        return 1

    f = n* factorial(n-1)
    return f 

n = int(input("Enter a number :"))
print(f"Factorial of {n} : {factorial(n)}")