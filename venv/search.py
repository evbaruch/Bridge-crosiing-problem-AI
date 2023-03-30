#search

import state
import frontier

def search(n):
     s=state.create(n)
     #the print function was here
     f=frontier.create(s)
     #the problem with the function was when we were printing the frontier state
     #we were printing the begining state and the end state only
     #so i fixed it by printing the state in the while loop
     #and now it prints the whole path of the state
     while not frontier.is_empty(f):
         s=frontier.remove(f)
         #i moved the print function here
         print(s)
         #we also added the frontier create and frontier remove functions
         #so the prints will show the steps in a acuret way


         while not frontier.is_empty(f):
             frontier.remove(f)
         frontier.remove(f)
         if state.is_target(s):
             return s
         ns=state.get_next(s)
         for i in ns:
             if state.is_target(i):
                 return i
             frontier.insert(f,i)


     return 0

print(search([1,2,5,10, 15,8]))

#an explanation for the huristic function:
#the huristic function is the sum of the crossing times of the people on the left side
#and the time it takes to get to the riught side
#plus the crossing time of the flashlight




