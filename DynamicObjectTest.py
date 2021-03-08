#testing code to create objects with dynamically generated names
#https://stackoverflow.com/questions/21598872/how-to-create-multiple-class-objects-with-a-loop-in-python


class Number:
    def __init__(self, number):
        self.number = number

    def getNumber(self):
        return self.number


#using list
def ObjectsList():
    objects = []
    for i in range(10):
        objects.append(Number(i+1))
    for i in range(10):
        print(objects[i].getNumber())
    print(objects[0].getNumber()+objects[1].getNumber())

#using dictionary
def ObjectsDictionary():
    objects = {}
    for i in range(10):
        objects['obj{}'.format(i+1)] = Number(i+1)
    print(objects['obj1'].getNumber())


ObjectsList()
ObjectsDictionary()