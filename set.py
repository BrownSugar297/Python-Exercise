
Myset = {1,'Ashik',True,False,}
print(Myset)
print(type(Myset))
print(len(Myset))
print('\n')
#Access set item
Set = {1,2,3,4,5}
for i in Set:
    print(i)

print(3 in Set)
print('\n')

#Add new item

Set1 = {'ashik','adib','rojoni','ammu','abbu'}
Set1.add('bunny')
print(Set1)
#Remove item

set = {1,2,3,4,5,6}
set.remove(3)   #remove 10 dile eror but discard dile no eror no output
print(set)

#Set update()

Set2 = {'Ashik','Bunny'}
Set3 = {1,2,3}      #list hobe jodi = []
Set2.update(Set3)
print(Set2)
#union
unionset3 = Set2.union(Set3)
print(unionset3)
#pop
set1 = {1,2,3,4,5}
set1.pop()
print(set1)
set1.clear()
print(set1)
print('\n')

#loop set
for ashik in Set1:
    print(ashik)

#Exercise
fruit = {"apple","banana","mango"}
if "apple"in  fruit:
    print("Apple is in")
fruit.add("orange")
print(fruit)
