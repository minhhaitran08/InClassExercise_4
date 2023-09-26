"""
This program will generate x number of unique, randomized list of integers.
Number of lists (draws) will be inputted by users. 
Generated numbers will be stored in a list and compared with the newly 
generated number and make sure that there is no duplicate.
"""
import random

def random_generator():
    #Store number of draw wanted from user
    num_draw = int(input('Please enter number of draw:')) 
    cur_draw = 0 #first draw
    drawlist_late = [] #Track the latest draw
    
    #Track the number of draws
    while cur_draw < num_draw:
        #Result List contain choosen number in the current draw
        drawlist_curr = []
        #Track number of lucky numbers added to the result list
        num_curr=0
        while num_curr < 6:
            #Randomly created a number
            num = random.randint(1,49)
            #Check if the generated number have been added in the the previous
            #list or current list
            #If NO added to the result drawlist_curr
            #If YES re-run the loop to generate a new number
            if num not in (drawlist_late and drawlist_curr):
                drawlist_late.append(num)
                drawlist_curr.append(num)
                num_curr = num_curr + 1
        #Print out the current draw and move on to the new one
        print ("This is draw number:",cur_draw+1,"\n",drawlist_curr)
        #Update drawlist_late to the lastest draw
        drawlist_late = drawlist_curr.copy()
        cur_draw = cur_draw + 1
    