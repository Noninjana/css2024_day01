#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 07:49:10 2024

@author: nyawuzakazi
"""

#Storing Data
B1 = 30
B2 = 40
B3 = 30 
B4 = 49

print(B1)
print(B2)

#Using Lists - store multiple values and defined by []
age = [30,40,30,49,22,35,22,46,29,25,39]
print(age)

print(age[0])
print(age[1])
print(age[2])

print(min(age))
print(max(age))
print(len(age))
print(sum(age))
average = (sum(age))/len(age)
print(average)

#Gender List
gender = ["M","M","F","M","F","F","F","M","M","F","M"]
print(gender[0])
print(gender[1])
print(gender[2])
print(gender[-1]) # print the last value in the set

#country list
country = ["South Africa","Botswana","South Africa","South Africa","Kenya","Mozambique","Lesotho","Kenya","Kenya","Egypt","Sudan"]
print(country)
print(country[0])
print(country[5])

#Data Storage with Lists
my_list = [42, -2021, 6.283,"tau", "node"]
print(my_list) 
print(my_list[:])

my_list.append("pi")
print(my_list)

my_list.insert(1,"pi2")
print(my_list)

my_list.remove("pi")
my_list.remove("pi2")
my_list.remove("tau")
print(my_list)
print(len(my_list))

# View a certain range of items:
print(my_list[0:3])

#Dictionaries

# d = {'key1': 'value1', 'key2': 'value2'...}
      