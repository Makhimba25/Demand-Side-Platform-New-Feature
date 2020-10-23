#!/usr/bin/env python
# coding: utf-8

import pandas as pd #pandas library for data analysis
import numpy as np #numerical python
import matplotlib.pyplot as plt

%matplotlib inline
plt.style.use('ggplot') #styling for creating pretty plots
seg = pd.read_csv('Fake Segment Report.csv') #imports fake segment level report with conversions by mmuid

#TRADER SEGMENT LEVEL REPORTING:

#Shows trader important info like which segments have the most conversions
seg['Segment Name'].value_counts().head().plot(kind='bar',color='hotpink')


#Shows how many users fall into more than one segment
seg.groupby(['mm_uuid'])[['Segment Name']].nunique().sort_values(by='Segment Name',ascending=False)
 
#Sets all duplicated users to 1 so that conversions are not double counted for users that fall within more than 1 segment.

def dedupe(x):
    if x>1:
        y=1
    else:
        x=1
    return y

seg['Segment Name'].apply(dedupe)

#TRADER SEGMENT OPTIMIZATION: 

#SOLUTION 1: Trader ranks segments based on performance and T1 uses waterfall logic to bid 

#Segments assigned and T1 asks what priority trader would like to assign each segment
#Trader ranks each segment using an integer

Windows= int(input("Priority #"))
Ladders= int(input("Priority #"))
DoorLocks= int(input("Priority #"))
ExtDoors=int(input("Priority #"))

Assigned_Segments=Windows+Ladders+DoorLocks+ExtDoors

#T1 loops through all assigned segments based on Priority level
#At the beginning of the campaign before top performers are establsihed trader sets all segment priorities to 1.
#If priority is equal to 1, T1 bids there first.

def priority(a): #defining priority 
     #next bid level is equal to priority level plus 1
    while priority ==1:
        bid=1
        return bid #bid here first since priority is 1
    if win!=1:
        bid=a+1 #if bid is not won keep bidding on next segment in priority waterfall.
    return bid 
            
Assigned_Segments(priority(a)) #Calls the bid logic function for all assigned segments


#SOLUTION 2: Trader sets performance threshold and T1 ranks segments based on how they compare to threshold

#Campaign goal is ROI

#ROI's for Segments
Windows= 20
Ladders= 10
DoorLocks= 5
ExtDoors= 35

#Threshold for ROI set by trader
threshold= 30

#All segments assigned to strategy
segments=[Windows,Ladders,DoorLocks,ExtDoors]


def bid(segment): #which segment to bid in?
    priority=segment/threshold #priority is relationship between threshold and segment
    for segment in segments: #within applied segments, used for loop because there is a set number of segments.
        if  priority >=1: #when priority is greater than 1 meaning segment ROI is greater than threshold
            return bid first #bid in these segments first
        else priority < 1: #otherwise if priority is less than 1, bid in these segments last since they're lower performing
            return bid last 
bid_priority=bid(segment) #set priority in bidding to whatever function generates.


