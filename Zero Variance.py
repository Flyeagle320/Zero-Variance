# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 16:03:46 2022

@author: Rakesh
"""
#importing Package for data manipulation##
import pandas as pd
##loading dataset##
z = pd.read_csv('D:/DATA SCIENCE ASSIGNMENT/DataSets-Data Pre Processing/DataSets/Z_dataset.csv')

##lets drop Id i.e Id is nothing but index#

z.drop(z.columns[0] , axis = 1 ,inplace=True)

z.info() ##to see null or NA in data types##

z.describe() ##mean , min , max  ##

##Graphical representation##
import matplotlib.pyplot as plt

#histogram for square length#

plt.hist(z['square.length'])

#histogram for square breadth#

plt.hist(z['square.breadth'])
#histogram for rec.length#
plt.hist(z['rec.Length'])

#histogram for rec breadth#
plt.hist(z['rec.breadth'])
#histogram for colours#
plt.hist(z['colour'])

##lets find outlier in Z using boxplot##

z.columns
boxplot=z.boxplot(column=['square.length' ,'square.breadth' , 'rec.Length' , 'rec.breadth'])

##in histogram we can see there is outlier in square breadth##

## lets see unique value in each column#
counts =z.nunique()

counts

##variance for each columns##
z.var()

##in this data square breadth variance = 0.1
##it indicate all the data in square breadth is identical
#lets drops it #
z.drop(["square.breadth"],axis = 1 , inplace= True)





