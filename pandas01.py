#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 07:28:12 2024

@author: nyawuzakazi
"""

import pandas #this line imports the pandas library
#pandas is a powerful library in Python used for data manipulation and analysis

file = pandas.read_csv("country_data.csv") #this line reads the csv from a specified url and assigns the the resulting data to the variabke named 'file'

print(file) #prints the content of the file vaiable to the console - displays the data in a structured format, pandas typically represents data in a tabular format

print(file.info()) #summarizes the table.Tells you the amouunt of columns, their names, non-null count, and the data type. the bottom part tells if the data types were read in correctly.

print(file.describe()) #generates the descriptive statistics of the DataFrame or Series e.g the central tendency, dispersion, and shape of the distribution

file = pandas.read_csv("diab_data.csv")

print(file)

print(file.describe())

file = pandas.read_csv("housing_data.csv")

print(file)

print(file.describe())

file = pandas.read_csv("insurance_data.csv")

print(file)

print(file.describe())

file = pandas.read_csv("iris.csv")

print(file)

print(file.describe())