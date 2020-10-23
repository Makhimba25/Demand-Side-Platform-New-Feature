**SOLVING T1 WITH PSUEDOCODE

**REALITY

As a trader, it can take hours to set up and manage a campaign that uses a large number of audience segments (1P, 3P, AS) because they need to be broken out into their own strategies within T1 in order to see individual audience performance and control spend by audience. For example, if a client wants to target 30 audiences, we need to set up 30 strategies in T1 and adjust spend across those audiences based on performance each day.

The ability to pull segment reporting and then use it to make optimizations  cuts down on the number of strategies needed so that  traders can set up, pace and optimize a campaign that uses multiple segments in under 5 minutes.





**PROBLEM 1

T1 Doesn't Have Segment Level Reporting because impressions, conversions and ...are not deduped if user falls into more than one segment.

#SOLUTION:

**PROBLEM 2:
#SOLUTION 1:
#SOLUTION 2:

Waterfall logic 











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



