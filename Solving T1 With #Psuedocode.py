#!/usr/bin/env python
# coding: utf-8

# In[92]:




#PART 1: Waterfall logic 

#1. Pull raw report and loop through and only count conversions 
#once based on criteria which is time. so if user is in segment a 
#and segment b, whichever conversion or segment was engaged first. 
#which segment did t1 search through first and at what times/2. 
#while user is in segment a, stop counting gif you see them in 
#another segment, kinda how dictionary terms cant be repeated. 
#OR while user is in segment a, only count them for the cheapest 
#segmetn. if segments are same price, return to previous logic OR 
#use priority logic, so that its impossible to bid within muplitple
#segments at same time for same user. if user is in segment A, bid. 
#If user converts in segment a, stop bidding. Using sample report, only 
#count users who converted in the first segment on the first day/time they 
#converted.Using mock data report and Python Pandas, while statements
#user_converion= time.conversion.
#segmentwhile user is in segment_a:    
#print(user_conversion)   
#stop counting after user is counted once
#n+=1#user cannot exist anymore

#PART 2
#take it a step furhter and give traders the ability to control the waterfall.
#If performance is >X, bid here first.

#PART3


# In[ ]:






# In[ ]:





# fake_seg_report.drop_duplicates(subset=False,inplace=True) 
# len1=len(fake_seg_report)
# print(len1)

# In[ ]:





# In[55]:


#Solution 2: 
#control bidding on users who fall into multiple segments.
#Part 1-During bidding
#seg_1=
#audience waterfall logic
#User input order of segments.
#bid 1:
#segment 1->if win, return imp.
#segment 1->if lose, keep bidding->segment 2->segment 3
#while bidding
#seg1=cheapest or #seg2=user selected
#loop through in specific order
#1. If MMUID1 is in segment a, bid. 
#2. If MMUID1 is in segment b, don't bid.

# trader set threshold(ex. )
#part  allow traders to control logic

#if seg perf is above x, return bid then move on to seg 1
#if seg perf is below x, return don't bid
#if seg perf is 
#top seg = user input first
# logic= dsp bids in top seg 1st then if doesnt win then go to 2nd best
#then 3rd best
#while seg is above X bid seg 1:
#



#TRADER SEGMENT OPTIMIZATION: 

#SOLUTION 1: Trader ranks segments based on performance

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
        bid=a+1 #if bid is not won keep bidding on next segment in priority ranking.
    return bid 
            
Assigned_Segments(priority(a)) #Calls the bid logic function for all assigned segments


#SOLUTION 2: Trader sets performance threshold and T1 ranks segments based on how they compare to threshold

#Campaign goal is ROI
#ROI's for Segments
Windows= 20
Ladders= 10
DoorLocks= 5
ExtDoors= 35

#threshold for ROI set by trader
threshold= 30

#all segments assigned to strategy
segments=[Windows,Ladders,DoorLocks,ExtDoors]


def bid(segment): #which segment to bid in?
    priority=segment/threshold #priority is relationship between threshold and segment
    for segment in segments: #within applied segments
        if  priority >=1: #when priority is greater than 1 meaning segment ROI is greater than threshold
            return bid first #bid in these segments first
        else priority < 1: #otherwise if priority is less than 1, bid in these segments last since they're lower performing
            return bid last 
bid_priority=bid(segment) #set priority in bidding to whatever function generates.
