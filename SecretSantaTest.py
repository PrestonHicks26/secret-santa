import SecretSanta

santa = SecretSanta.SecretSanta()
averageTries = 0
trials = 1000
for i in range(trials):
    unassigned = True
    tries = 0
    while unassigned:
        santa.pull()
        tries += 1
        print(repr(santa))
        if not santa.assignments.get(santa.group[len(santa.group) - 1]) == "EMPTY":
            unassigned = False
    averageTries += tries
    print("It took {} tries to properly assign each participant a recipient.".format(tries))
    print("")
averageTries = averageTries/trials
print("It took an average of {} tries to properly assign each participant a recipient.".format(averageTries))
