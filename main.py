#Secret Santa Program
#Requirements:
#Allow user to input variable number of names
#Only display gift recipient to user
#Only accept groups of at least 2

import SecretSanta


santa = SecretSanta.SecretSanta()
unassigned = True
while unassigned:
    santa.pull()
    if not santa.assignments.get(santa.group[len(santa.group) - 1]) == "EMPTY":
        unassigned = False
santa.reportRecipients()



