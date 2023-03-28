'''
The state is a list of three items:
1. Who is on the left side? each person is represented by its crossing time. 0=flashlight
2. Who is on the right?
3. A list of moves. Every move is a list the persons(crossing times)
   that crossed the bridge
start: all people on the left side
target: all people on the right
'''

import copy

#l is a list of the crossing times. the init. state is a list of crossing times
#+ 0 for the flashlight (all initially on the left side),
#and empty list=pers on the right and another empty list=moves so far.
def create(l):
    return[l+[0],[],[]]

#Returns a list of states one cross away from state x (the children of x)

def get_next(x):

    # your code here
    # x is a state
    # return a list of states
    # each state is a list of three items:
    # 1. Who is on the left side? each person is represented by its crossing time. 0=flashlight
    # 2. Who is on the right?
    # 3. A list of moves. Every move is a list the persons(crossing times) that crossed the bridge
    # start: all people on the left side
    # target: all people on the right

    ns = [] #ns is the list of next states
    if x[0] == []: #if the flashlight is on the left side
        return 0
    if 0 in x[1]: #if the flashlight is on the right side
        for i in x[1]: #for all the people on the right side
            if i != 0: #that are not the flashlight
                y = create(x[0].copy()+[i]) #create a new state
                y[1] = x[1].copy()
                y[1].remove(i) #remove the people from the right side
                y[1].remove(0) #remove the flashlight from the right side
                y[2] = x[2].copy()+ [[i,0]] #create a new state
                ns += [y] #add the new state to the list of next states
    else: #if the flashlight is on the left side
        for i in x[0]:  #for all the people on the left side
            for k in x[0][x[0].index(i)+1:]: #for all the people on the left side
                if i != 0 and k != 0: #that are not the flashlight
                    y = [x[0].copy(),x[1].copy()+[i,k,0],x[2].copy()+[[i,k]]] #create a new state
                    y[0].remove(k) #remove the people from the left side
                    y[0].remove(i) #remove the people from the left side
                    y[0].remove(0) #remove the flashlight from the left side
                    ns += [y] #add the new state to the list of next states





    return ns
                           

#Gets x (a state) and returns the length of the path to that state.
def path_len(x):
    pl=0           #pl sums the path length
    for i in x[2]: #for all the moves:
        pl+=max(i) #  sum into pl the max. crossing time of the 1 or 2 pers. crossing
    return pl

#returns True iff state x is the target.
#x is the target iff no one is on the left side.
def is_target(x):
    return x[0]==[]

def hdistance(s):
    if s[0] == []:
        return 0                   # the heuristic value of s
    h = 0
    x = sorted(s[0])
    if x[0] == 0:
        x = x[1:]
    for i in range(len(x)-1, -1, -2):
        h += x[i]
    return h

