# basic logic in python

"""
function TABLE-DRIVEN-AGENT(percept ) returns an action
persistent: percepts, a sequence, initially empty
table, a table of actions, indexed by percept sequences, initially fully specified
append percept to the end of percepts
action = LOOKUP(percepts, table)
return action
"""

# The table driven-AGENT percept as a number
def table_driven_agent(percept):
    # percept = []
    table = {1:"Right",2:"Suck",3:"Left",4:"Suck"} # table as dictionary must be fully specified
    action = table.get(percept)
    return action

"""
The actions should be as follows there are only 4 possibilities
1. [A, Clean]: "Right"
2. [A, Dirty]: "Suck"
3. [B, Clean]: "Left"
4. [B, Dirty]: "Suck"
"""

import random
def test_table_driven_agent():
    list_of_percepts = ["[A, Clean]", "[A, Dirty]","[B, Clean]","[B, Dirty]"]
    print("Testing what should the agent do?\n")
    list_random = [random.randint(1,4) for x in range(20)]
    for x in range(15):
        idx = list_random[x]-1
        print("we have the percept %s" %list_of_percepts[idx])
        print("action = %s " %table_driven_agent(list_random[x]))

test_table_driven_agent()
