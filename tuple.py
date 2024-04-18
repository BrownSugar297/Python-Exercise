#negative indexing

NewTuple = (1,2,3,"Ashik",False)
print(type(NewTuple))

print(NewTuple[-3])

#range of indexes
print('\n')
Tuple = (4, 5, 6, 'Adib', 'Rojoni', True)
print(Tuple[0:4])

#update tuples
print('\n')

FamilyTuple = ('ashik','adib','rojoni')
a = list(FamilyTuple)
a.append('bunny')

FamilyTuple = tuple(a)
print(FamilyTuple)

#unpack tuple
print('\n')

fruit = ('apple','orange','banana')
(a,b,c) = fruit
print(b)

Xfruit = ('apple','orange','banana','mango','malta')
(*a,b) = Xfruit
print(b)

#join tuple
print('\n')

num1 = (1,2,3,4)
num2 = (5,6,7,8)
print(num1 + num2)
print(num1 * 10)

#tuple method
Ashik = (1,2,3,3,3,'B','b','b')
As = Ashik.count(3)
hi = Ashik.count('B')
k = Ashik.count('b')
print(As)
print(hi)
print(k)

print(len(Ashik))