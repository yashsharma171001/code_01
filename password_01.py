import random
a = list()
b = ['$','#','@','*','%']
print("Password length 8 :-")
for i in range(2):
    a.append(chr(random.randrange(65,91)))
    a.append(chr(random.randrange(97,123)))
    a.append(chr(random.randrange(48,58)))
    a.append(random.choice(b))

random.shuffle(a)
print(''.join(a))