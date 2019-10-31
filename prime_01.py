def isprime(x):
    for i in range(2,x):
        if x%i == 0 :
            return 0

    return 1

x = int(input("Enter a number : "))

  if isprime(x) == 1 :
    print(f"{x} is Prime")

  else :
    print(f"{x} is not Prime")
