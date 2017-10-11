# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 10:39:25 2017

@author: Shrishailya Bhinge
"""

###################1:Runtime Exception##############
#try:
#    dividend = int(input("Please enter the dividend: "))
#    divisor = int(input("Please enter the divisor: "))
#    print("%d / %d = %f" % (dividend, divisor, dividend/divisor))
#except ValueError:
#    print("The divisor and dividend have to be numbers!")
#except ZeroDivisionError:
#    print("The dividend may not be zero!")
######################2:pattern#####################
#def pat(n):
#    for i in range(1, n):
#        for j in range(65, 65+i):
#            a = chr(j)
#            print a,
#            
#        print
#
#n=int(raw_input("Enter Number Of rows:"))
#n=n+1
#pat(n)
################3:Write a program to Sort a List of Tuples in##### 
#def last(n): return n[-1]
#
#def sort_list_last(tuples):
#  return sorted(tuples, key=last)
#
#print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

######Increasing Order by the Last Element in Each Tuple######

################4:Write a program to Find the Sum of Digits in a Number######

#number=int(input("Enter a number:"))
#total=0
#while(number>0):
#    digit=number%10
#    total=total+digit
#    number=number//10
#print("The total sum of digits is:",total)

##############5:Write a Python program to find a missing number from a list###
#def missnumbers(num_list):
#      original_list = [x for x in range(num_list[0], num_list[-1] + 1)]
#      num_list = set(num_list)
#      return (list(num_list ^ set(original_list)))
#
#print(missnumbers([1,2,3,4,6,7,10]))

##############6:Finding name comes before @' i.e.username##############
#import re
#
#def Find(pat,text):
#    match=re.search(pat,text)
#    
#    if match:
#        print match.group()
#    else:
#        print 'Not Found'
#    
#Find(r"[\w\d.]+@","shreebhinge@gmail.com")
#strip@ n save it.

##############7.Write a program to display an user-defined Exception##########
#class InvalidAgeError(Exception):
#          def __init__(self,message):
#            self.message=message
#            
#def ageCheck(age):
#    try:
#        if age < 0 or age > 125:
#        
#            raise InvalidAgeError("Enter Corret Age in between 0 to 125")
#        else:
#            print "You're allow to proceed further"
#            
#    except InvalidAgeError,e:
#            print(e.message)
#
#age=int(raw_input("Enter User Age:"))
#ageCheck(age)

#########8:
#########9:Write a PYTHON program to check the validity of a password chosen by a user.
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
########10:Write a program to accept Date & Time in IST format and convert it to US format(EST)
#from datetime import datetime
#from pytz import timezone
#
#fmt = "%Y-%m-%d %H:%M:%S %Z%z"
#
## Current time in IST
#now_ist = datetime.now(timezone('GMT+5.5'))
#print now_ist.strftime(fmt)
#
## Convert to US/Pacific time zone
#now_usest = now_ist.astimezone(timezone('US/Eastern'))
#print now_usest.strftime(fmt)
#########11:Write a Python program to find whether it contains an additive 
##sequence or not


##12: WAP to implement logging 


##13:Write a Python program where you take any positive integer n, if n is even, 
#divide it by 2 to get n / 2. If n is odd, multiply it by 3 and add 1 to obtain 
#3n + 1. Repeat the process until you reach 1.

#number=int(raw_input("Enter a number:"))
#print number,
#
#while number!=1:
#    
#    if number%2==0:
#        number/=2
#    else:
#        number=number * 3 + 1
#        
#    print number,

#########14:Write a Python program to check if a given positive integer is a power of two
#number = False
#
#def power_of_two(n):
#    for i in range(n+1):
#        if n==2**i:
#            number = True
#            break
#        else:
#            number = False
#            
#    if(number == True):
#        print ("Entered Number is Power Of Two")        
#    else:
#        print ("Entered Number is not Power Of Two")
#        
#n=int(raw_input("Enter a number:"))
#power_of_two(n)

##15:.Write a program to Sort a List of Tuples in Increasing Order by the Last Element in Each Tuple

#def last(n): return n[-1]
#
#def sort_list_last(tuples):
#  return sorted(tuples, key=last)
#
#
#print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

#######16:Write a Program to Count the Number of Lines in a Text File

#f=open("file.txt",'r')
#fi=f.read()
#count=fi.splitlines()
#print(len(count))

####17.Define a class named Circle which can be constructed by a radius. 
####The Circle class has a method which can compute the area.
#import math
#area=0
#class Area(object):
#    
#    def __init__(self,radius):
#        self.radius=radius
#    
#    def circle_area(self,radius):
#        area = math.pi*self.radius**2
#        return area
#
#def main():
#   circle1 = Area(5)
#   a=circle1.circle_area(5)
#   print a
#
#main()


##21:Write a Program to Read the Contents of a File in Reverse Order

#for line in open("file.txt", 'r').readlines()[::-1]:
#    print line[::-1].replace('\n', '')

##22:Write a program that accepts a sentence and calculate the number of letters and digits.
#st = raw_input("Input a string:")
#digit=0
#letter=0
#for c in st:
#    if c.isdigit():
#        digit=digit+1
#    elif c.isalpha():
#        letter=letter+1
#    else:
#        pass
#print("Letters", letter)
#print("Digits", digit)

##23:Write a Program to Read a String from the User and Append it into a File
#file3=open("file.txt","a")
#c=raw_input("Enter string to append: \n");
#file3.write("\n")
#file3.write(c)
#file3.close()
#
#print("Contents of appended file:");
#for line in open("file.txt", 'r').readlines()[::]:
#    print line[::]
#file3.close()

##24.Write a program which accepts a sequence of comma-separated numbers from 
#console and generate a list and a tuple which contains every number.
#li=raw_input("Enter elements for list:")
#li=li.split(",")
#print li
#
#tu=tuple(li)
#print tu

##25:
#dic = {}
#
#param = input("Please enter number:")
#
#for i in range(1, int(param)+1 ):
#    dic[i] = i * i
#
#print(dic)

#from pytz import all_timezones
#
#print len(all_timezones)
#for zone in all_timezones:
#    
#        print zone