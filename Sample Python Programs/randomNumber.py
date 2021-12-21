import random

s = 'abcde'
print(random.choice(s))

list = [1, 2, 3, 4]
print(list)
random.shuffle(list)
print(list)

print(random.random())

print(random.randrange(2, 10, 2))

print(random.uniform(2, 9))