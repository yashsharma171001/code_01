def isprime(n):
    for i in range(2,n):
        if n%i == 0 :
            return 0

    return 1

n = int(input("Enter a number : "))
if isprime(n) == 1 :
    print(f"{n} is Prime")

else :
    print(f"{n} is not Prime")