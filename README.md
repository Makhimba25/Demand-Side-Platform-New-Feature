**SOLVING T1 WITH PSUEDOCODE

**REALITY

As a trader, it can take hours to set up and manage a campaign that uses a large number of audience segments (1P, 3P, AS) because they need to be broken out into their own strategies within T1 in order to see individual audience performance and control spend by audience. For example, if a client wants to target 30 audiences, we need to set up 30 strategies in T1 and adjust spend across those audiences based on performance each day.

The ability to pull segment reporting and then use it to make optimizations  cuts down on the number of strategies needed so that  traders can set up, pace and optimize a campaign that uses multiple segments in under 5 minutes.





**PROBLEM 1

Although there are ways to get a segment report within MM, T1 does not have a direct segment level reporting feature. This is because impressions, spend and conversions are not deduped if a user falls into more than one segment.

* SOLUTION 1:

1. Use Pandas group by function, to filter by mmuid and then count the number of uniques within a segment for each user. This means that the user falls into a particular segment X amount of times. 
2. Using def function, define a dedupe function with conditionals so that if the user count within a segment is above 1, set the value to one in the dataframe being used. This means that all users will only be counted within one segment. 
3. Using numerical python and pyplot, show a bar graph of the segments that drove the most conversions so that traders can easily visualize what the top performers for their campaign is.


**PROBLEM 2: 

Once trader gets segment level reporting, the only way to optimize off of top performers vs low performers is to break out strategies.

* SOLUTION 1: Trader Dictates Priority

Without having to breakout strategies, trader can rank segments based on performance then T1 will use waterfall logic to bid on users based on the ranking of the segment they are in.

1. User input order of segments.
2. Bid 1 is in Segment 1. 
3. If Segment 1 wins the impression then keep bidding in Segment 1 until spend is maxed out there. *Note-Since the top performing segments are usually low scale ones, all of the daily spend won't go to one segment. 
4. If Segment 1 is maxed out keep bidding except this time go to Segment 2 then Segment 3 and so on. 
5. Once we reach the end of the waterfall, start over at Segment 1. 


* SOLUTION 2: Trader Dictates Threshold and T1 Generates Priority based on threshold

Waterfall logic 












#control bidding on users who fall into multiple segments.
#Part 1-During bidding
#seg_1=
#audience waterfall logic

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



