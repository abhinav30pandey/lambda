'''1. Write a Python program to calculate the length of a string. '''

s=input('enter your string: ')
print('the length of string is: ',len(s))



''' 2. Write a Python program to count the number of characters (character frequency)
in a string.
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}   '''

s=input('enter your string: ')
d={}
for x in s:
	if x in d:
		d[x] += 1
	else:
		d[x] = 1
print(d)


'''3. Write a Python program to get a string made of the first 2 and the last 2 chars from
a given a string. If the string length is less than 2, return instead of the empty string. 
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String      '''


str1 = input('enter a string: ')
if len(str1) >= 2:
	print( str1[:2] + str1[-2:] )
else:
	print('empty string')



'''4. Write a Python program to get a string from a given string where all occurrences
of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'  '''

str1 = 'restart'
char = str1[0]
str1 = str1.replace(char, '$')
str1 = char + str1[1:]
print(str1)




#5. Write a Python program to get a single string from two given strings, 
#separated by a space and swap the first two characters of each string. Go to the editor
#Sample String : 'abc', 'xyz'
#Expected Result : 'xyc abz' 

def chars_mix_up(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))



#6. Write a Python program to add 'ing' at the end of a given string 
#(length should be at least 3). If the given string already ends with 'ing' then add 'ly' 
#instead. If the string length of the given string is less than 3, leave it unchanged.
#Sample String : 'abc'
#Expected Result : 'abcing'
#Sample String : 'string'
#Expected Result : 'stringly'


s=input('enter the string: ').strip()

if len(s)==3:
	p=(s + 'ing')
	print(p)
elif len(s)<3:
	print(s)
elif s.find('ing'):
	print(s + 'ly')
else:
	print(s)



#7. Write a Python program to find the first appearance of the substring 'not' and 'poor' 
#from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring
#with 'good'. Return the resulting string. Go to the editor
#Sample String : 'The lyrics is not that poor!'
#'The lyrics is poor!'
#Expected Result : 'The lyrics is good!'
#'The lyrics is poor!'


def not_poor(str1):
  snot = str1.find('not')
  spoor = str1.find('poor')
  if spoor > snot and snot>0 and spoor>0:
    str1 = str1.replace(str1[snot:(spoor+4)], 'good')
    return str1
  else:
    return str1
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))


#8. Write a Python function that takes a list of words and return the longest word and
#the length of the longest one. Go to the editor
#Sample Output:
#Longest word: Exercises
#Length of the longest word: 9

l=eval(input('enter your list: '))
word_len = []
for x in l:
	word_len.append((len(x), x))
word_len.sort()
print(word_len[-1][0], word_len[-1][1])


'''9.Write a Python program to remove the nth index character from a nonempty string.'''

str = input('enter your string: ')
n = int(input('enter index to remove the character: '))
first_part = str[:n] 
last_part = str[n+1:]
print(first_part + last_part)


'''10 Write a Python program to change a given string to a new string where the first 
and last chars have been exchanged. 
Write a Python program to change a given string to a 
new string where the first and last chars have been exchanged'''

str1=input('enter youe string: ')
s1=str1[-1:] + str1[1:-1] + str1[:1]
print(s1)



#11. Write a Python program to remove the characters which have odd index values of a 
#given string.

s=input('enter the string: ')
s1=s[:len(s):2]
print(s1)



#12. Write a Python program to count the occurrences of each word in a given sentence

s=input('enter your string: ')
d={}
words=s.split()
for word in words:
	if word in d:
		d[word] += 1
	else:
		d[word] = 1
print(d)


'''13. Write a Python script that takes input from the user and displays that input back in
upper and lower cases'''

s=input('enter your string: ')
s1=s.upper()
s2=s.lower()
print(s1)
print(s2)



'''14... 15.....'''




'''16. Write a Python function to insert a string in the middle of a string'''


def insert_middle(str,word):
	return str[:2] + word + str[2:]

str=input('enter your str: ')
word=input('enter your words: ')
print(insert_middle(str,word))


'''17. Write a Python function to get a string made of 4 copies of the last two characters
of a specified string (length must be at least 2). Go to the editor
Sample function and result :
insert_end('Python') -> onononon
insert_end('Exercises') -> eseseses'''

str1 = input('enter the string: ')
result = str1[-1:-3:-1] * 4
print(result)

'''18. Write a Python function to get a string made of its first three characters 
of a specified string. If the length of the string is less than 3 then return the 
original string.
Sample function and result :
first_three('ipy') -> ipy
first_three('python') -> pyt'''

def first_three(str):
	if len(str) > 3:
		return str[0:3]
	else:
		return str
str = input('enter the string: ')
print(first_three(str))


'''19. Write a Python program to get the last part of a string before a specified character.
https://www.w3resource.com/python-exercises
https://www.w3resource.com/python  '''


str1='https://www.w3resource.com/python-exercises'
char1='-'
f = str1.index(char1)
cha = str1[:f]
print(cha)


'''20. Write a Python function to reverses a string if it's length is a multiple of 4.'''

str1=input('enter a string: ')
if len(str1) % 4 == 0:
	f=''.join(reversed(str1))
	print(f)

'''21. Write a Python function to convert a given string to all uppercase , if it contains
at least 2 uppercase characters in the first 4 characters.'''

str = input('enter upper_str: ')
num_upper = 0
for letter in str[:4]: 
	if letter.upper() == letter:
		num_upper += 1
if num_upper >= 2:
	print(str.upper())
print(str)



'''23.Write a Python program to remove a newline in Python'''

str1='Python Exercises\n'
print(str1)
print(str1.rstrip())


'''24. Write a Python program to check whether a string starts with specified characters.'''

str = input('enter your string: ')
char = input('enter your specified characters: ')
print(str)
if str[:3] in str:
	print('yes ! string:- {} is specified with specified characters:- {}'.format(str,char))


'''25. Write a Python program to create a Caesar encryption.'''

def encrypt(string, shift):
	cipher = ''
	for char in string:
		if char == ' ':
			cipher = cipher + char
		elif  char.isupper():
			cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
		else:
			cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)

	return cipher
 
string= input("enter string: ")
shift = int(input("enter shift number: "))
print("original string: ", text)
print("after encryption: ", encrypt(string,shift))




'''26. Write a Python program to display formatted text (width=50) as output.'''


import textwrap
sample_text = '''
  Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.
  '''
print()
print(textwrap.fill(sample_text, width=50))
print()



'''27.Write a Python program to remove existing indentation from all of the lines 
in a given text.'''

import textwrap
sample_text = '''
  Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.
  '''
print(textwrap.indent(sample_text,''''''))


'''28. Write a Python program to add a prefix text to all of the lines in a string.'''

import textwrap
sample_text = '''
  Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.
  '''
print(textwrap.indent(sample_text,'>'))



'''29                       '''




'''30. Write a Python program to print the following floating 
numbers upto 2 decimal places.'''

x = float(input('enter the float number: '))
print("Formatted Number: "+"{:.2f}".format(x));


'''31. Write a Python program to print the following floating numbers
upto 2 decimal places with a sign.'''


n = float(input('enter the float number: '))
if n > 0:
	print("Formatted Number: "+"+{:.2f}".format(n));
else:
	print("Formatted Number: "+"{:.2f}".format(n));



'''32. Write a Python program to print the following floating numbers 
	   with no decimal places'''

x = float(input('enter the float number: '))
print('formatted number: '+ '{:.0f}'.format(x))

'''33. Write a Python program to print the following integers with
	zeros the left of specified width.'''


x = float(input('enter the number: '))
print("Formatted Number: "+"0{:.2f}".format(x));




'''34        '''




'''35. Write a Python program to display a number with a comma separator.'''


number=input('enter a number: ')
num=','.join(number)
print(num)


'''36.Write a Python program to format a number with a percentage.'''

num =float(input('enter a number: '))
percentage = '{:.0%}'.format(num)
print(percentage)




'''38. Write a Python program to count occurrences of a substring in a string.'''

str= input('enter a string: ')
substr = input('enter a string: ')
pos=0
count=0
i = str.count(substr,pos,len(str))
print('the count occurence of a substring is: ',i)


'''39. Write a Python program to reverse a string.'''

str= input('enter a string: ')
print(str[::-1])


'''40. Write a Python program to reverse words in a string.'''

str= input('enter a string: ').split()

for word in str:
	word = word[::-1]
	print(word,end=',')


'''41. Write a Python program to strip a set of characters from a string.'''

str = input('enter a string: ')
char=('aeiou')
for c in str:
	if c not in char:
		print(c,end='')


'''42. Write a Python program to count repeated characters in a string. Go to the editor
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output :
o 4
e 3
u 2
h 2
r 2
t 2 '''

s='thequickbrownfoxjumpsoverthelazydog'
d={}
for x in s:
	if x in d:
		d[x] += 1
	else:
		d[x] = 1
print(d)

'''43. Write a Python program to print the square and cube symbol in the area of a rectangle 
and volume of a cylinder.
Sample output:
The area of the rectangle is 1256.66cm2
The volume of the cylinder is 1254.725cm3'''

length = float(input('enter the length: '))
width =  float(input('enter the width: '))
print('The area of the rectangle is {}'.format(length*width) + " cm2 ")
radius = float(input('enter the radius: '))
height = float(input('enter the height: '))
pi=3.14
print('The area of the rectangle is {}'.format(pi*radius*radius*height) + " cm3 ")

'''44. Write a Python program to print the index of the character in a string.
Sample string: w3resource
Expected output:
Current character w position at 0
Current character 3 position at 1
Current character r position at 2               '''



str = input('enter a string: ')
for index, char in enumerate(str):
    print("Current character", char, "position at", index )


'''45. Write a Python program to check whether a string contains all letters of the alphabet.'''

str = input('enter a string: ')
print(str.isalpha())


'''46.Write a Python program to convert a given string into a list of words. '''

str1 = input('enter your string: ')
print(str1.split(' '))


'''47. Write a Python program to lowercase first n characters in a string.'''

str1 = input('enter the string: ')
n = int(input('enter the value of n: '))
lower_case = str1[:n].lower() + str1[n:]
print(lower_case)

'''48. Write a Python program to swap comma and dot in a string. Go to the editor
Sample string: "32.054,23"
Expected Output: "32,054.23" '''

str1 = input('enter your string: ')
maketrans = str1.maketrans
str1 = str1.translate(maketrans(',.', '.,'))
print(str1)

'''49. Write a Python program to count and display the vowels of a given text'''


text = input('enter a string: ')
vowel = ('aeiouAEIOU')
c = 0
l=[]
for letter in text:
	if letter in vowel:
		l.append(letter)
		c+=1
print('display the vowels of a given text',l)
print('the count of vowel is: ',c)



'''50. Write a Python program to split a string on the last occurrence of the delimiter'''

str1 = 'a,b,c,d'
l = str1.rsplit(',',1)
print(l)


'''51................52...... '''



'''53. Write a Python program to find the first repeated character in a given string.'''

str1 = input('enter a string: ')
f = str1.find(str1[:1],1,len(str1))
print('the first repeated character {} at index {}'.format(str1[f],f))


'''54...........56'''




'''57.Write a Python program to remove spaces from a given string.'''

str1 = input('enter a string: ')
print(str1.replace(' ',''))


'''58. Write a Python program to move spaces to the front of a given string.'''

str1 = input('enter a string: ')
print(str1.replace(' ',''))


'''59. Write a Python program to find the maximum occurring character in a given string.'''

str1 = input('enter a string: ')
d = {}
for x in str1:
	if x in d:
		d[x] +=1 
	else:
		d[x] = 0
result = max(d, key = d.get) 
print ("The maximum occurring character in a given string : " + str(result))

'''60. Write a Python program to capitalize first and last letters of each 
word of a given string.'''

str1 = input('enter a string: ')
cap = (str1[0:1].upper()) + str1[1:-1] + (str1[-1:].upper())
print(cap)


'''61. Write a Python program to remove duplicate characters of a given string.'''

str=input('enter a string: ')
s=set(str)
print("Without Order:",s)
t=""
for i in str:
	if i in t:
		pass
	else:
		t=t+i
print("With Order:",t)


'''62. Write a Python program to compute sum of digits of a given string'''

str1 = input('enter a number: ')
total = 0
for x in str1:
    if x.isdigit():
        total += int(x)
print("Total:- ", total)


'''63. Write a Python program to remove leading zeros from an IP address.'''
ip= ("255.024.01.01")
subs = '0'
s=ip.replace(subs,'')
print(s)


'''64.............'''



'''65. Write a Python program to find all the common characters from two given lower
case strings.If there are no common letters print "No common characters"'''

str1 = input('enter a string: ').lower()
str2 = input('enter a string: ').lower()
l = []
for x in str1:
	if x in str2:
		l.append(x)
	else:
		print('no common characters {} & {}'.format(str1,str2))
print(l)


'''66..................'''


'''67. Write a Python program to remove all consecutive duplicates of a given string.'''

str1 = input('enter a string: ')
l = []
for x in str1:
	l.append(x)
	
print('afetr removeing all duplicates of string:',set(l)) 


'''68...............69........'''


'''70. Write a Python program to create a string from two given strings 
concatenating uncommon characters of the said strings'''


s1 = input('enter a characters: ')
s2 = input('enter a characters: ')
set1 = set(s1)
set2 = set(s2)
l=[]
common_chars = (set1 & set2)
for x in s1:
	if x not in common_chars:
		l.append(x)
for x in s2:
	if x not in common_chars:
		l.append(x)
print(''.join(l))



'''71. Write a Python program to move all spaces to the front of a given 
string in single traversal.'''


str1 = input('enter a string: ')
str2 = str1.replace(' ','')
print(str2)


'''72. Write a Python code to remove all characters except a 
specified character in a given string.
ex:-
Original string
Python Exercises
Remove all characters except P in the said string:p     '''


str1 = input('enter a original string: ')
substring = input('enter a specified character: ')
l = []
for x in str1:
	if x == substring:
		l.append(x)
	else:
		pass
print(''.join(l))

'''73. Write a Python program to count Uppercase, Lowercase, special character and
numeric values in a given string.'''


str1 = input('enter a string: ')
upper_ctr, lower_ctr, number_ctr, special_ctr = 0, 0, 0, 0
for i in range(len(str1)):
	if str1[i] >= 'A' and str1[i] <= 'Z':
		upper_ctr += 1

	elif str1[i] >= 'a' and str1[i] <= 'z':
		lower_ctr +=1

	elif str1[i] >= '0' and str1[i] <= '9':
		number_ctr +=1

	else:
		special_ctr +=1
print('count of special character is',special_ctr)
print('count of Upper character is: ',upper_ctr)
print('count of lower character is: ',lower_ctr)
print('count of numric value is: ',number_ctr)


'''74...............82....'''


'''83. Write a Python program to print four values decimal, octal,
hexadecimal (capitalized), binary in a single line of a given integer.  '''

i = int(input('enter a integer: '))
d = str(i)
o=str(oct(i))[2:]
h=str(hex(i))[2:]
b=str(bin(i))[2:]

print(d,'',o,'',h,'',b)


'''84. Write a Python program to swap cases of a given string.'''


str1 = input('enter a string: ')
str = ''
for x in str1:
	if x.isupper():
		str +=x.lower()
	else:
		str +=x.upper()
print(str)




'''85....................'''




'''86. Write a Python program to delete all occurrences of a specified 
character in a given string.'''

str1 = input('enter a string: ')
char = input('enter a string: ') 
if char in str1:
	s=str1.replace(char,'')
print('specified character:',s)


'''87. Write a Python program find the common values that appear in two given strings.'''

str1 = input('enter a string: ')
str2 = input('enter a string: ')
result = ""
for ch in str1:
	if ch in str2 and not ch in result:
		result += ch
print("Original strings:")
print(str1)
print(str2)
print("\nIntersection of two said String:") 
print(result)


'''88. Write a Python program to check whether a given string contains a
capital letter, a lower case letter, a number and a minimum length.

Sample Output:
Input the string: W3resource
['Valid string.']           '''

str1 = input('enter a string: ')
if str1.isalnum() and len(str1)<8:
	print(['Valid string.'])
else:
	print(['Invalid string.'])



'''89. Write a Python program to remove unwanted characters from a given string.'''

str1 = 'Pyth*^on Exercis^es'
str = ''
for x in str1:
	if x.isalpha():
		str +=x
print(str)

'''or.....'''

str1 = input('enter a string: ')

unwanted_chars = ["#", "*", "!", "^", "%"]

for i in unwanted_chars:
	str1 = str1.replace(i,'')
print(str1)



'''90. Write a Python program to remove duplicate words from a given string.'''

str1 = input('enter a string: ')
l = str1.split()
lst = []
for x in l:
	if x not in lst:
		lst.append(x)

print("Original String:-")
print(str1)
print("\nAfter removing duplicate words from the said string:-")
print(' '.join(lst))



'''91. Write a Python program to convert a given heterogeneous
list of scalars into a string.'''

lst = ['Red', 100, -50, 'green', 'w,3,r', 12.12, False]
for x in lst:
	s=''.join(str(x))
	print(s,end=',')



'''92........................'''



'''93. Write a Python program to extract numbers from a given string.'''

str1 = input('enter a string: ')
l=str1.split()
l1=[]
for num in l:
	if num.isdigit():
		l1.append(num)
print(l1)



'''94.............95......'''




'''96. Write a Python program to convert a given string to camelcase.'''

str1 = input('enter a string: ')
camel_case = str1.replace(' ','')
print(camel_case)



'''97. Write a Python program to convert a given string to snake case.'''

str1 = input('enter a string: ')
snake_case = str1.replace(' ','_')
print(snake_case)



'''98. Write a Python program to decapitalize the first letter of a given string.'''

str1 = input('enter a string: ')
s = str1[0].lower()
s1 = s + str1[1:]
print(s1)



'''99. Write a Python program to split a given multiline string into a list of lines.
Sample Output:
Original string: This
is a
multiline
string.
Split the said multiline string into a list of lines:
['This', 'is a', 'multiline', 'string.', '']                          '''

multiline_string = 'This\n is a\n multiline \n string'
l=multiline_string.split('\n')
print(l)




'''100.......................'''




'''101. Write a Python program to add two strings as they are numbers (Positive integer values). Return a message if the numbers are string. Go to the editor
Sample Output:
42
Error in input!
Error in input!              '''

str1 = input('enter a string: ')
for x in str1:
	if x is not str:
		print('Error in input!')
		






















































































