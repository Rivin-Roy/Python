#read a list from the keyboard and return unique elements
numbers=input("Enter some numbers: ").split()
numbers=list(map(int,numbers))
print(numbers)
set1=set(numbers)
print(set1)
numbers=list(set1)
print(numbers)
