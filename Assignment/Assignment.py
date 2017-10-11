# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 11:24:04 2017

@author: Shrishailya Bhinge
"""
##1:Write a Python program to find those numbers which are divisible by 7 
##and multiple of 5, between 1500 and 2700 (both included)
#empty_list=[]
#for x in range(1500, 2700):
#    
#    if (x%7==0) and (x%5==0):
#        
#        empty_list.append(str(x))
#        
#print (','.join(empty_list))

##2:Write a Python program to convert temperatures to and from celsius, fahrenheit.
#fah=0
#def cel_to_fah(celcius):
#    
#    fah = (celcius*1.8) + 32
#    print fah
#    
#celcius=float(raw_input("Enter Temprature:"))
#cel_to_fah(celcius)

##3:Pattern using nested for loop

#for i in range(0,5):
#    for j in range(0,i+1):
#            print "*",
#    print
#    
#for k in range(5,1,-1):
#    for z in range(1,k):
#        print "*",
#    print     


##4:Write a Python program to get the Fibonacci series between 0 to 50

#t1=0
#t2=1
#n=50
#nextTerm=t1+t2
#print t1
#print t2
#
#while nextTerm<=n:
#
#    print nextTerm
#    t1=t2
#    t2=nextTerm
#    nextTerm=t1+t2
        
##5:Password Validation
#import re
#p= raw_input("Input your password:")
#x = True
#while x:  
#    if (len(p)<6 or len(p)>12):
#        break
#    elif not re.search("[a-z]",p):
#        break
#    elif not re.search("[0-9]",p):
#        break
#    elif not re.search("[A-Z]",p):
#        break
#    elif not re.search("[$#@]",p):
#        break
#    elif re.search("\s",p):
#        break
#    else:
#        print("Valid Password")
#        x=False
#        break
#
#if x:
#    print("Not a Valid Password")
##6:Write a Python program to print alphabet pattern 'A'.
#
#result_str="";    
#for row in range(0,7):    
#    for column in range(0,7):     
#        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):    
#            result_str=result_str+"*"    
#        else:      
#            result_str=result_str+" "    
#    result_str=result_str+"\n"    
#print(result_str);


##7:Write a Python program to print alphabet pattern 'D'
#
#result_str="";    
#for row in range(0,7):    
#    for column in range(0,7):     
#        if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 5)) or (column == 5 and row != 0 and row != 6)):  
#            result_str=result_str+"*"    
#        else:      
#            result_str=result_str+" "    
#    result_str=result_str+"\n"    
#print(result_str);

##
##8:Write a Python program to print alphabet pattern 'E'.
#
#result_str="";    
#for row in range(0,7):    
#    for column in range(0,7):     
#        if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 6)) or (row == 3 and column > 1 and column < 5)):  
#            result_str=result_str+"*"    
#        else:      
#            result_str=result_str+" "    
#    result_str=result_str+"\n"    
#print(result_str);


##9:Write a Python program to print alphabet pattern 'G'.
#
#result_str="";    
#for row in range(0,7):    
#    for column in range(0,7):     
#        if ((column == 1 and row != 0 and row != 6) or ((row == 0 or row == 6) and column > 1 and column < 5) or (row == 3 and column > 2 and column < 6) or (column == 5 and row != 0 and row != 2 and row != 6)):  
#            result_str=result_str+"*"    
#        else:      
#            result_str=result_str+" "    
#    result_str=result_str+"\n"    
#print(result_str);


##10. Write a Python program to print alphabet pattern 'L'.
#
#result_str="";    
#for row in range(0,7):    
#    for column in range(0,7):     
#        if (column == 1 or (row == 6 and column != 0 and column < 6)):  
#            result_str=result_str+"*"    
#        else:      
#            result_str=result_str+" "    
#    result_str=result_str+"\n"    
#print(result_str);


##11:Write a Python program to print alphabet pattern 'M'.
#
#result_str="";    
#for row in range(0,7):    
#    for column in range(0,7):     
#        if (column == 1 or column == 5 or (row == 2 and (column == 2 or column == 4)) or (row == 3 and column == 3)):  
#            result_str=result_str+"* "    
#        else:      
#            result_str=result_str+"  "    
#    result_str=result_str+"\n"    
#print(result_str);

##12:Write a Python program to calculate a dog's age in dog's years
#human_age=int(raw_input("Input a dog's age in human years:"))
#
#if human_age <= 2:
#    dogs_age=human_age *10.5
#    print ("The dog's age in dog's years is:%d"%dogs_age)
#else:
#    dogs_age=(human_age-2)*4 +21
#    print ("The dog's age in dog's years is:%d"%dogs_age)

##13:Write a Python program to check whether an alphabet is a vowel or consonant.
#   
#guess = raw_input(':')[0]
#
#if guess in ('a','A','e','E','i','I','o','O','u','U'):
#    print ("%s is a vowel."%guess)
#else:
#    print ("%s is a consonants."%guess)

##14:Write a Python program to get next day of a given date. 

#year = int(input("Input a Year: "))
#
#if (year % 4 == 0):
#    leap= True
#else:
#    leap = False
#    
#month = int(input("Input a month [Jan to Dec]: "))
#
#if month in (1,3,5,7,8,10,12):
#    month_days=31
#
#elif month == 2:
#    if leap:
#        month_days = 29
#    else:
#        month_days = 28
#else:
#    month_days = 30
#
#day = int(input("Input a day [1 to 31]: "))
#
#if day < month_days:
#    day =day+ 1
#else:
#    day = 1
#    if month == 12:
#        month = 1
#        year =year + 1
#    else:
#        month =month + 1
#print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))

##15: Write a program to solve a classic ancient Chinese puzzle:
##We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
##How many rabbits and how many chickens do we have? 

#def solve(numheads,numlegs):
#
#    ns='No solutions!'
#    for i in range(numheads+1):
#        j=numheads-i
#        if 2*i+4*j==numlegs:
#            return i,j
#    return ns,ns
#
#
#numheads=35
#numlegs=94
#solutions=solve(numheads,numlegs)
#print (solutions)


##16:Please write a program which prints all permutations of [1,2,3]

#import itertools
#print(list(itertools.permutations([1,2,3])))

##17:write a program which accepts a string from console and print the 
##characters that have even indexes    
#st=raw_input("Enter a string:")
#res=""
#
#for i in range(0,len(st)):
#    if i%2==0:
#        res+=st[i]
#print res

##18:write a program which accepts a string from console and print it in reverse order.

#st=raw_input("Enter a string:")
#
#print st[::-1]


##19:WAP which count and print the numbers of each character in a string input by console.
#st=raw_input("Enter a sentence:")
#words = st.split()
#
#freq = []
#for w in words:
#    freq.append(words.count(w))

##20. Define a class Person and its two child classes: Male and Female. All classes have a method 
#"getGender" which can print "Male" for Male class and "Female" for Female class.
#(Inheritance is applicable)


##21:WAP to print this list after removing all duplicate values with original order reserved.
#seq=[12,24,35,24,88,120,155,88,120,155]
#def f2(seq): 
#   
#   checked = []
#   for e in seq:
#       if e not in checked:
#           checked.append(e)
#   return checked
#print f2(seq)

##22:By using list comprehension, please write a program to print the list after removing the v0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
#st=[12,24,35,70,88,120,155]
#l = st[0::2]
#print l
#some_list[start:stop:step]

#st=[12,24,35,70,88,120,155]
#x=[ [st[x] for x in range(0,len(st)) if x%2!=0 ] ]
#st =list(x)
#print st

##23:Write a binary search function which searches an item in a sorted list. 
##The function should return the index of element to be searched in the list.

#def binarySearch (ar, l, r, x):
# 
#    if r >= l:
# 
#        mid = l + (r - l)/2
# 
#        if ar[mid] == x:
#            return mid
#         
#        elif ar[mid] > x:
#            return binarySearch(ar, l, mid-1, x)
# 
#        else:
#            return binarySearch(ar, mid+1, r, x)
# 
#    else:
#        return -1
# 
#ar = raw_input("Enter elements:").split(" ")
#x = raw_input("Enter element to search:")
# 
#index = binarySearch(ar, 0, len(ar)-1, x)
# 
#if index == -1:
#    print "Element is not in array"
#else:
#    print "Element is present at index %d" % index


##24:WAP which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

#st="2 cats 3 dogs"
#s=[]
#
#for i in range(0,len(st)):
#    if st[i].isdigit():
#        s.append(st[i])
#print s

##25:Only Company name
#import re
#
#def Find(pat,text):
#    match=re.search(pat,text)
#    
#    if match:
#        print match.group(1)
#    else:
#        print 'Not Found'
#    
#Find(r"@([\w]+)","shreebhinge@gmail.com")

##26:Define a custom exception class which takes a string message as attribute

#class ValueTooSmallError(Exception):
#    
#   pass    
#class ValueTooLargeError(Exception):
#   
#   pass
#
#while True:
#   try:
#       i_num = int(input("Enter a number: "))
#       number = int(input("Enter a number: "))
#       if i_num < number:
#           raise ValueTooSmallError
#       elif i_num > number:
#           raise ValueTooLargeError
#       break
#   except ValueTooSmallError:
#       print("This value is too small, try again!")
#       print()
#   except ValueTooLargeError:
#       print("This value is too large, try again!")
#       print()
#
#print("Congratulations! You guessed it correctly.")

##27:Write a program to generate and print another tuple whose values are even numbers 

#numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9,10)
#number1=()
#for x in numbers:
#    if x%2==0:
#        number1=x
#        print number1
        
##28:A website requires the users to input username and password to register.
#import re
#
#m = re.compile(r'(?=.*?\d)*|(?=.*?[A-Z])*|(?=.*?[a-z])*|(?=.*?[$#@])*|[A-Za-z\d].{6,12}$')
#a=True
#while a:
#    
#    pas= raw_input("Input your password:")
#    
#    if(len(pas)>5 and len(pas)<13):
#        
#       if m.match(pas):
#            print "valid Password"
#            break
#       else:
#           print "Invalid Password"
#           break
#    else:
#        print "Length could not be less than 6 or more than 12"
#        break


#^[a-zA-Z]\w{3,14}$
##29:WAP that computes the net amount of a bank account based a transaction log from console input
#tot = 0
#
#while True:
#	line = raw_input("> ").split()
#	if not line:
#		break;
#		
#	amount = int(line[1])
#	if line[0] == 'D':
#		tot += amount
#	elif line[0] == 'W':
#		tot -= amount
#
#print tot