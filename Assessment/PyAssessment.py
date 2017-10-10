# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 10:39:25 2017

@author: Shrishailya Bhinge
"""

###################1:Runtime Exception##############
#t=int(raw_input())
#
#while t:
#    a,b=map(long,raw_input().split())
#    l=a*b
#    print l
#    t=t-1

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
#lstrip@ n save it.

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
#########9:
########10:
#########11:Write a Python program to find whether it contains an additive 
##sequence or not
#class Solution(object):
#
#    def is_additive_number(self, num):
#        length = len(num)
#        for i in range(1, int(length/2+1)):
#            for j in range(1, int((length-i)/2 + 1)):
#                first, second, others = num[:i], num[i:i+j], num[i+j:]
#                if self.isValid(first, second, others):
#                    return True
#        return False
#
#    def isValid(self, first, second, others):
#        if ((len(first) > 1 and first[0] == "0") or
#                (len(second) > 1 and second[0] == "0")):
#            return False
#        sum_str = str(int(first) + int(second))
#        if sum_str == others:
#            return True
#        elif others.startswith(sum_str):
#            return self.isValid(second, sum_str, others[len(sum_str):])
#        else:
#            return False
#
#if __name__ == "__main__":
#    print(Solution().is_additive_number('66121830'))
#    print(Solution().is_additive_number('51123'))
#    print(Solution().is_additive_number('235813'))

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

