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
#        print '*',
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
        
##5:

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


##16:Please write a program which prints all permutations of [1,2,3]

#import itertools
#print(list(itertools.permutations([1,2,3])))

##17:write a program which accepts a string from console and print the 
##characters that have even indexes    
