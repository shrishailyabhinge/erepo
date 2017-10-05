#!/usr/bin/python
"""
Spyder Editor

This is a temporary script file.
"""
#import re
#
#def Find(pat,text):
#    match = re.search(pat,text)
#    if match:
#        print match.group()
#    else:
#        print 'not found'
#        
##Find(r'[\w.]+@[\w.]+','blah nick.p.p@gmail.com yatta @')
#Find(r'c.@*$l','c.@*$lled piig much better')
#var = raw_input()
#var1= raw_input()
#var2= raw_input()
#var3= raw_input()
#if var=='shree' and var1=='bhinge':
#    print 'SUCESSFUL'
#elif var2=='pappu' and var3=='chaudhari':
#    print 'sucessful'
#else:
#    print 'OMG'

#for letter in 'Python':
#    print 'current letter',letter
#    
#fruits=['banana','apple','mango','watermelon']
#
#for index in range(len(fruits)):
#    print "Current Fruits:", fruits[index]

#for num in range(10,20):
#    for i in range(2,num):
#        if num%i==0:
#            print 'Not a prime number',num
#            break
#        else:
#            print 'prime number',num
#            break=0   
#i=0     
#while (i<9) and i!=7: print (i)
#   
#print "Good Bye"
#var = 10                    # Second Example
#while var > 0:              
#   var = var -1
#   if var == 5:
#str = "this is\tstring example....wow!!!";
#
#print "Original string: " + str
#print "Defualt exapanded tab: " +  str.expandtabs()
#print "Double exapanded tab: " +  str.expandtabs(16)
#      continue
#   print 'Current variable value :', var
#print "Good bye!"
#a='shree'
#b=a
#a=a+a
#print(a)
#print(b)
#var= 'shree'
#print var[:5]+"bhinge"
#####################String Operations###########
#var ="shree bhinge shree" 
#print var.count('shr', 0,len(var))
#str = "this is string example....wow!!!";
#suffix = "is";
#print str.endswith(suffix)
#print str.endswith(suffix, 2, 4)
#str = "this-is-a-string-example....wow";
#print "Min character: " + min(str)
#str = "this is string example....wow!!! this is really string"
#print str.replace("is", "was")
#print str.replace("is", "was", 2)

#str1 = "this really is a string example....wow is!!!";
#str2 = "is";
#
#print str1.rfind(str2)
#
#print str1.rfind(str2, 0, 10)
#print str1.rfind(str2, 10, 0)
#
#print str1.find(str2)
#print str1.find(str2, 0, 10)
#print str1.find(str2, 10, 0)

#str = "     this is string example....wow!!!     !";
#print str.rstrip()
#str = "88888888this is string example....wow!!!88        8";
#print str.rstrip('8')

#str = "Line1-abcdef \nLine2-abc \nLine4-abcd \nLine5-vasgv";
#print str.split()
#print str.split(' ', 2 )

#str = "This is string example....wow!!!";
#print str.swapcase()

#a='This is my string'
#print a[::-1]

#value = "apple"
#
## Get last two characters.
#end = value[-2:]
#print(end)

#a=range(1,11)
#print (a)
#
#a.append(11)
#print (a)
#
#print a[-4:11]
#
#names= ['Bob','John','Sue']
#print names[0]
#
#list(range(4,11))
#print [x*2 for x in range(1,10)]
#
#evens=[x for x in range(1,20) if x%2== 0]
#
#c=[z for z in a if z>=8]
#print c

#a = ['abc',10,'def',12]
#b = ['abc',10,'def',12]
#
#print cmp(b,a)

#list1, list2 = [123, 'xyz'], [456, 'abc']
#
#print cmp(list1, list2)
#print cmp(list2, list1)
#list3 = list2 + [786];
#print cmp(list2, list3)

#s = [123,'shree',456,'bhinge',123]
#print s.index(123)

#aList = [123, 'xyz', 'zara', 'abc']
#aList.insert( 3, 2009)
#print "Final List : ", aList

#aList = [123,'zzz123', 'xyz', 'zara', 'abc', 'xyz'];
#
#aList.sort();
#print "List : ", aList

#aList = [123, 'xyz', 'zara', 'abc'];
#aTuple = tuple(aList)
#
#print "Tuple elements : ", aTuple

#dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
#
#dict['Age'] = 8; # update existing entry
#dict['School'] = "DPS School"; # Add new entry
#
#
#print "dict['Age']: ", dict['Age']
#print "dict['School']: ", dict['School']

#a = "nitin"
#b = a[::-1]
#if a == b:
#    print "palindrome"
#else:
#    print "not palindrome"

####Passing By value####
#def printme(str):
#    "My First Function Program"
#    str5="bhinge"
#    str=str + str5
#    print str5
#    print str
#    return str5
#
#str6=printme("shrishailya\t")
#
#print str6
#print "Termination Completed"


####Passing By Referrence####
#def printme(str):
#    "My First Function Program"
#    str5="bhinge"
#    str=str + str5
#    print str5
#    print str
#    return str5
#
#str="shrishailya\t"
#str6=printme(str)
#
#print str6
#print "Termination Completed"

# Function definition is here
#def printinfo( arg1, *vartuple ):
#   "This prints a variable passed arguments"
#   print "Output is: "
#   print arg1
#   for var in vartuple:
#      print "Hi I'm In For Loop" 
#      print var
#   return;
#
## Now you can call printinfo function
#printinfo( 10 )
#printinfo( 70, 60, 50 )

#def f1():
#    print('f1()')
#    
#f1()
##f2()
#
#def f2():
#    print("f2()")

#def factorial(n):
#    print("factorial has been called with n = " + str(n))
#    if n == 1:
#        return 1
#    else:
#        res = n * factorial(n-1)
#        print ("intermediate result for ", n, " * factorial(" ,n-1, "): ",res)
#        return res	
#
#print(factorial(5))


#def factorial(n):
#    
#    if n == 1:
#        return 1
#    else:
#        res = n * factorial(n-1)
#        return res
#	
#n=input()
#print(factorial(n))

#mylist=[1,2,3,4,5,6,7,8,9]
#new_list= list(map(lambda x: x * 2,mylist))
#print mylist
#print (new_list)

#my_list=[1,2,3,4,5,6,7,8,9]
#new_list= list(filter(lambda x: (x%2 == 0), my_list))
#print (my_list)
#print (new_list)



#from string import maketrans   # Required to call maketrans function.
#
#intab = "aeiou"
#outtab = "12345"
#trantab = maketrans(intab, outtab)
#
#str = "this is string example....wow!!!"
#print str.translate(trantab)

#import random
#print random.randint(0, 5)

#import random
#print int(random.random() * 100)

#import random
#print random.choice( ['red', 'black', 'green'] )

#from random import shuffle
#x = [[i] for i in range(10)]
#shuffle(x)
#print x

#import random
#for i in range(3):
#    print random.randrange(0, 101, 5)

print "Commit Changes"
print "Commit Changes 2 time"
