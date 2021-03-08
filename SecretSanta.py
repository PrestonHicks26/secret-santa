# similar to doubly linked list, meaning has both 'next' and 'previous'
# each node represents a person taking part in exchange
# 'next' is written as 'giving,' the person that node n is giving a present to
# 'previous' is written as 'receiving,' the person that node n is receiving a present from
# code based on implementation of linked list given in
# https://realpython.com/linked-lists-python/#implementing-your-own-linked-list

import random
import os


#legacy class, leaving in case I want to try to implement the program differently
class Node:
    def __init__(self, name):
        self.name = name
        self.giving = None
        self.receiving = None


    def __repr__(self):
        return self.name


class SecretSanta:
    # get people involved, create hat list, group list, and dictionary
    def __init__(self):
        self.hat = []
        self.group = []
        self.assignments = {}
        self.more = True
        self.name = ""
        while self.more:
            print("Enter a name. If you are finished entering names, then enter 'n'")
            name = input()
            if name == "n":
                self.more = False
                break
            self.hat.append(name)
            self.group.append(name)


    def __repr__(self):
        rep = 'SecretSanta('+str(self.hat)+','+str(self.group)+','+str(self.assignments)+')'
        return rep


    def pull(self):
        copyHat = self.hat.copy()
        for person in self.group:
            subHat = []
            for card in copyHat:
                if card != person:
                    subHat.append(card)
            if not subHat:
                subHat.append("EMPTY")
            choice = random.choice(subHat)
            self.assignments[person] = choice
            if choice != "EMPTY":
                copyHat.remove(choice)


    def reportRecipients(self):
        for i in range(len(self.group)):
            print("{}'s recipient will now be announced:".format(self.group[i]))
            input("(Enter anything to continue)")
            print()
            print("You will be giving a present to {}!".format(self.assignments.get(self.group[i])))
            input("(Enter anything to clear screen)")
            self.clear()
            if i == len(self.group)-1:
                break
            input("(Enter anything when the next person is ready)")
            print()
        print("Everyone now has a Secret Santa Partner!")


    #note this only works in terminal or cmd, to clear in IDE, just print a ton of newlines
    def clear(self):
        IDE = True
        if not IDE:
            #for windows
            if os.name == 'nt':
                os.system('cls')
            #for mac and linux
            else:
                os.system('clear')
        else:
            print ("\n"*100)
