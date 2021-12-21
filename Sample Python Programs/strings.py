str = 'Welcome to Python Prigramming'
print(str)
print(str[0])
print(str[-1])
print(str[11:17])
print(str[11:])
print(str[:6])
print(str + ' session')     #immutable
print(str * 2)
print(len(str))
print(str.lower())
print(str.upper())
print(str.swapcase())
print(str.title())

str = 'This is old and this is New'
print('\n' + str)
print(str.replace(' is ', ' was ', 1))
print(str.replace('i', ''))     #Remmove a charector
print(str.count('is'))
print(str.count('is', 2, 8))