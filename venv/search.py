#search

import state
import frontier

def search(n):
     s=state.create(n)
     print(s)#the print function was here
     f=frontier.create(s)
     #the problem with the function was when we were printing the frontier state
     #we were printing the begining state and the end state only
     #so i fixed it by printing the state in the while loop
     #and now it prints the whole path of the state
     while not frontier.is_empty(f):
         s=frontier.remove(f)

         #while not frontier.is_empty(f):
         #    frontier.remove(f)

         if state.is_target(s):
             return s


         #i moved the print function here
         #print(s)
         #we also added the frontier create and frontier remove functions
         #so the prints will show the steps in a acuret way - but , is it what the problem is???????

         ns=state.get_next(s)
         for i in ns:
             if state.is_target(i): # this check can be deleted but it will make the function cost O(frontier) more and there are boundery cases it's needed
                 return i
             frontier.insert(f,i)


     return 0

print(search([1,2,5,10]))

#an explanation for the huristic function:
#the huristic function is the sum of the crossing times of the people on the left side
#and the time it takes to get to the riught side
#plus the crossing time of the flashlight
#its purpose it's to provide us an estimate cost
#the huristic is admissible



