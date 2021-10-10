'''1. Write a Python program to sum all the items in a list.'''

lst = [1,2,3,4,-8]
sum =0
for x in lst:
	sum +=x
print('sum all the items in a list is:',sum)




'''2. Write a Python program to multiply all the items in a list.'''

lst = [1,2,3,4]
mul = 1
for x in lst:
	mul *= x
print('multiply of all the items in a list is: ',mul)




'''3. Write a Python program to get the largest number from a list. '''

l = [90,8,22,10,6,9]
max = l[0]
for x in l:
	if x > max:
		max = x
print('largest number from a list is:',max)



'''4. Write a Python program to get the smallest number from a list.'''

l = [90,8,22,10,6,9]
min =l[0]
for x in l:
	if x < min:
		min = x
print('smallest number from a list: ',min)



'''5. Write a Python program to count the number of strings where the string length is
2 or more and the first and last character are same from a given list of strings. 
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2                                  '''


l = ['abc', 'xyz', 'aba', '1221']
ctr = 0
for word in l:
	print(word)
	if len(word) > 1 and word[0] == word[-1]:
		ctr += 1
print(ctr)



'''6..............'''




'''7. Write a Python program to remove duplicates from a list. '''

a = [10,20,30,20,10,50,60,40,80,50,40]

print(list(set(a)))
print()

''''''''''or'''''''''
uniq_items = []
for x in a:
    if x not in uniq_items:
        uniq_items.append(x)
print(uniq_items)



'''8. Write a Python program to check a list is empty or not. '''


l = []
if len(l)==0:
	print('"List is empty"')



'''9. Write a Python program to clone or copy a list. '''

l = [10,20,30,40,50]
l1=l
print(l)
print(l1)
print(id(l1))
print(id(l))

print()
''''''''''''''''''''''''''''''or''''''''''''''''''''''''

l2=l.copy()
print(l2)
print(l)
print(id(l2))
print(id(l))



'''10. Write a Python program to find the list of words that
are longer than n from a given list of words.'''


str1 = input('enter a string: ')
print(str1)
n = int(input('enter the n: '))
list_word = str1.split(' ')
lst=[]
for word in list_word:
	if len(word) > n:
		lst.append(word)
print(lst)



'''11. Write a Python function that takes two lists and 
returns True if they have at least one common member.      '''


lst1 = [10,20,30,40]
lst2 = [50,60,70,10]
for x in lst1:
	if x in lst2:
		print(True)



'''12. Write a Python program to print a specified list after removing the 
0th, 4th and 5th elements.
                 '''


lst = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
lst = [x for(i,x) in enumerate(lst) if i not in (0,4,5)]
print(lst)



'''13. Write a Python program to generate a 3*4*6 3D array whose each element is *.'''

array = [[ ['*' for col in range(6)] for col in range(4)] for row in range(3)]
print(array)



'''14. Write a Python program to print the numbers of a specified list 
after removing even numbers from it          '''


lst = [x for x in range(11) if x%2 != 0]
print(lst)



'''15. Write a Python program to shuffle and print a specified list.'''


from random import shuffle
lst = [1,2,3,4,5]
shuffle(lst)
print(lst)



'''16. Write a Python program to generate and print a list of first and last
5 elements where the values are square of numbers between 1 and 30 (both included).'''


l = [x*x for x in range(21)]
print(l[:5],l[-5:])



'''17. Write a Python program to generate and print a list except for the first 5 elements,
where the values are square of numbers between 1 and 30 (both included).'''

l = [x*x for x in range(21)]
print(l[5:])



'''19. Write a Python program to get the difference between the two lists..'''


list1 = [1, 3, 5, 7, 9]
list2=[1, 2, 4, 6, 7, 8]

diff1 = list(set(list1) - set(list2))
diff2 = list(set(list2) - set(list1))
total_diff = diff1 + diff2
print(total_diff )



'''20. Write a Python program access the index of a list.'''

lst = [10,20,30,40,50]
x = 0
for i in lst:
	print('index {} of a list element is {}'.format(x,i))
	x+=1



'''21. Write a Python program to convert a list of characters into a string.'''


l = ['p','y','t','h','o','n']
l1 = ''.join(l)
print(l1)



'''22. Write a Python program to find the index of an item in a specified list.'''

specified_list = [1,2,3,4,5]
x = int(input('enter any element to find index: '))
if x in specified_list:
	i=specified_list.index(x)
	print('{} element first occurence index is:{}'.format(x,i))



'''23. Write a Python program to flatten a shallow list.'''


lst1 = [[2,4,3],[1,5,6], [9], [7,9,0]]
lst = []
for x in lst1:
	for i in x:
		lst.append(i)
print(lst)



'''24. Write a Python program to append a list to the second list.'''

lst = [1,2,3,4]
lst1 = [5,6,7,8,9]

print(lst + lst1)



'''25. Write a Python program to select an item randomly from a list.'''


import random
color_list = ['Red', 'Blue', 'Green', 'White', 'Black']
print(random.choice(color_list))

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
lst = ['Red', 'Blue', 'Green', 'White', 'Black']

i = int(input('enter a random index: '))
if i in range(len(lst)-1):
	print('item randomly from a list:',lst[i])
else:
	print('plz enter corrent index')



'''26..................'''



'''27. Write a Python program to find the second smallest number in a list.'''


lst = [12, 45, 2, 41, 31, 10, 8, 6, 4]
length = len(lst)
print(length)
lst.sort()
print("Largest element is:", lst[length-1])	
print("Smallest element is:", lst[0])
print("Second Largest element is:", lst[length-2])
print("Second Smallest element is:", lst[1])



'''28. Write a Python program to find the second largest number in a list.'''


lst = [12, 45, 2, 41, 31, 10, 8, 6, 4]
lenght = len(lst)
lst.sort()
print(' second largest number in a list: ',lst[lenght-2])



'''29. Write a Python program to get unique values from a list.'''

lst = [12, 45, 2, 41, 31, 10, 8, 6, 4]

print("Original List : ",lst )
my_set = set(lst )
my_new_list = list(my_set)
print("List of unique numbers : ",my_new_list)



'''30. Write a Python program to get the frequency of the elements in a list.'''


lst = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]

d = {}
for x in lst:
	if x in d:
		d[x]+=1
	else:
		d[x]=1
print(d)



'''31. Write a Python program to count the number of 
elements in a list within a specified range. '''


lst = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]
min = 40
max = 100
ctr = 0
for x in lst:
	if min <= x <= max:
		ctr += 1
print(ctr)


'''32................34.........'''


''' 35. Write a Python program to create a list by concatenating a
given list which range goes from 1 to n.

Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']    '''


lst = ['p', 'q']
n = int(input('enter the value of n: '))
l = []
for x in range(1,n):
	print(x)
	for y in lst:
		c = y+str(x) 
		l.append(c)
print(l)


'''36...............................'''




'''37. Write a Python program to find common items from two lists.'''


color1 = ["Red", "Green", "Orange", "White"]

color2 = ["Black", "Green", "White", "Pink"]

print(set(color1) & set(color2))


'''38...................'''



'''39. Write a Python program to convert a list of multiple integers into a single integer.
Sample list: [11, 33, 50]
Expected Output: 113350                 '''


l = [11,33,50]
for x in l:
	print(str(x),end='')



'''40. Write a Python program to split a list based on first character of word.

d_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

incomplete
'''

l = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']
l.sort()

print(l)



'''41. Write a Python program to create multiple lists.'''

d = {}
for i in range(1,21):
	d[str(i)] = []
print(d)



'''42. Write a Python program to find missing and additional values in two lists.'''


list1 = ['a','b','c','d','e','f']
list2 = ['d','e','f','g','h']
print('Missing values in list2: ', ','.join(set(list1).difference(list2)))
print('Additional values in list1: ', ','.join(set(list2).difference(list1)))



'''43. Write a Python program to split a list into different variables.  '''

lst = [('apple(1,2,3)','bbbbb','cat'),('banana(1,2,3)','ccccc','rat'),
('mango(1,2,3)','ddddd','mouse')]



l1,l2,l3 = lst

print(l1)
print(l2)
print(l3)



'''45. Write a Python program to convert a pair of values into a sorted unique array.'''


L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
 (7, 8), (9, 10)]
print("Original List: ", L)
print("Sorted Unique Data:",sorted(set().union(*L)))



'''46. Write a Python program to select the odd items of a list.'''

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_list = []
for x in l:
	if x%2 !=0:
		odd_list.append(x)
print(odd_list)



'''47. Write a Python program to insert an element before each element of a list.
Sample Output:

Original List:  ['Red', 'Green', 'Black']                                                                     
Original List:  ['c', 'Red', 'c', 'Green', 'c', 'Black']           '''

lst = ['Red', 'Green', 'Black']
l = []
for elt in lst:
	for v in ('c', elt):
		l.append(v)
print(l)



'''48. Write a Python program to print a nested lists (each list on a new line)
using the print() function.'''


lst = [['red'],['green'],['black']]

for x in lst:
	print(x)



''' 49. Write a Python program to convert list to list of dictionaries.
Sample lists: 

["Black", "Red", "Maroon", "Yellow"], 
["#000000", "#FF0000", "#800000", "#FFFF00"]

Expected Output:
	
[{'color_name': 'Black', 'color_code': '#000000'}, 
{'color_name': 'Red', 'color_code': '#FF0000'}, 
{'color_name': 'Maroon', 'color_code': '#800000'}, 
{'color_name': 'Yellow', 'color_code': '#FFFF00'}]                    '''


color_name = ["Black", "Red", "Maroon", "Yellow"]
color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
for f, c in zip(color_name, color_code):
	print([{'color_name': f, 'color_code': c}])



'''50. Write a Python program to sort a list of nested dictionaries. '''

my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
print('original list')
print(my_list)
print('sort a list of nested dictionaries')

my_list.sort(key=lambda e: e['key']['subkey'], reverse=True)
print(my_list)





'''53. Write a Python program to create a list with infinite elements.  '''



import itertools
c = itertools.count()
while True:
	print(next(c))



'''54. Write a Python program to concatenate elements of a list. '''


l = [1,2,3,4,5]
add = 0
for x in l:
	add +=x
print(add)



'''56. Write a Python program to convert a string to a list.'''


s = input('enter a string:')
lst = []
l=s.split()
for x in l:
	lst.append(x)
print(lst)



'''57. Write a Python program to check if all items of a given 
list of strings is equal to a given string'''


l1 = ["green", "orange", "black", "white"]
l2 = ["green", "green", "green", "green"]

print(all(c == 'blue' for c in l1))
print(all(c == 'green' for c in l2))
	


'''58. Write a Python program to replace the last element in a list with another list.
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]        '''


l1 = [1, 3, 5, 7, 9, 10]
l2 = [2, 4, 6, 8]


l1[-1:]=l2
print(l1)



'''59. Write a Python program to check whether the n-th element exists in a given list.'''


l = [1, 2, 3, 4, 5, 6]
print(l[-1:])


'''''''''or'''''''''

x=len(l)-1
print(l[x])




'''60. Write a Python program to find a tuple, the smallest second
index value from a list of tuples'''


x = [(4, 1), (1, 2), (6, 0)]
print(x[2])



'''61. Write a Python program to create a list of empty dictionaries. '''

n = 5
print(n*[{}])


l = [{} for _ in range(n)]
print(l)



'''62. Write a Python program to print a list of space-separated elements.'''


l = [1,2,3,4,5]
for x in l:
	print(x,end=' ')



'''63. Write a Python program to insert a given string at the beginning of all items in a list.
Sample list : [1,2,3,4], string : emp
Expected output : ['emp1', 'emp2', 'emp3', 'emp4']       '''



l = [1,2,3,4]
print(['emp{0}'.format(i) for i in l])



'''64. Write a Python program to iterate over two lists simultaneously.'''

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]
for (x,y) in zip(l1,l2):
	print(x, y)



'''65. Write a Python program to move all zero digits to end of a given list of numbers.'''


l = [3, 4, 0, 0, 0, 6, 2]
x=0
while True:
	if x in l:
		l.remove(x)
	else:
		break
print(l)



'''66. Write a Python program to find the list in a list of lists whose sum of 
elements is the highest.

Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
Expected Output: [10, 11, 12]

'''

l = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
print(max(l))



'''67. Write a Python program to find all the values in a list are greater than a 
specified number'''

list1 = [220, 330, 500]
list2 = [12, 17, 21]
print([x for x in list1 if x>=800 ])
print(all(x >= 200 for x in list1))
print(all(x <= 90 for x in list1))



'''68. Write a Python program to extend a list without append.

Sample data: [10, 20, 30]
[40, 50, 60]
Expected output : [40, 50, 60, 10, 20, 30]        '''


l = [10, 20, 30]
l1= [40, 50, 60]

print(l+l1)



'''
69. Write a Python program to remove duplicates from a list of lists. 
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]]
'''


l = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
l1=[]
for x in l:
	if x not in l1:
		l1.append(x)
print(l1)



'''
70. Write a Python program to find the items starts with specific character from a given list.

'''


l = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
specific_character = input('enter a specific character: ')
l1=[]
for x in l:
	if x[0]==specific_character:
		l1.append(x)
print(l1)



'''
71. Write a Python program to check whether all dictionaries in a list are empty or not.

Sample list : [{},{},{}]
Return value : True

Sample list : [{1,2},{},{}]
Return value : False
'''

l = [{},{},{}]
print(all(not x for x in l))
l1= [{1,2},{},{}]
print(all(not x for x in l1))



'''
72. Write a Python program to flatten a given nested list structure. 
Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
Flatten list:
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]   '''


l = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
l1=[]
for x in l:
	if type(x)==list:
		for i in x:
				l1.append(i)	
	else:
		l1.append(x)

print(l1)



'''
73. Write a Python program to remove consecutive duplicates of a given list.

Original list:
[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
After removing consecutive duplicates:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]            '''


l = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
l1 = list(set(l))
print(l1)

































































































































































































































































