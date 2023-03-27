#search
import state
import frontier

def search(n):
    s=state.create(n)
    print(s)
    f=frontier.create(s)
    while not frontier.is_empty(f):
        s=frontier.remove(f)
        if state.is_target(s):
            return s
        ns=state.get_next(s)
        for i in ns:
            if state.is_target(i):
                return i
            frontier.insert(f,i)
    return 0

print(search([1,2,5,10]))
