'''
num = [1,2,3,4,5]

for i in num:
    print(i*2)
'''

num = [1,2,3,4,5]

Ashik = [i + 2 for i in num]
print(Ashik)
Ashik = [i * 2 for i in num]
print(Ashik)
Ashik = [i / 2 for i in num]
print(Ashik)


# sort list [Accending and Decending]
print('\n')

number = [1,3,5,2,10,14,99,45]
letter = ['a','c','r','t','f']
number.sort()
letter.sort()
print(number)
print(letter)
Ashik = [1,5,9,7,3,0]
Ashik.sort(reverse=True)
print(Ashik)

#Copy list
print('\n')

num = [1,2,3,4,5]
num2 = num.copy()
print(num)
print(num2)

# Join list
print('\n')

Ash = [1,2,3]
Adib = [4,5,6]
Roj = [7,8,9]
#Join = Ash + Adib + Roj
#print(Join)
Ash.extend(Adib + Roj)
print(Ash)

