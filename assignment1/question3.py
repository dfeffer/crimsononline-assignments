"""question 3

a)  Implement classes representing people and buildings. People should support
    name and gender, seamlessly verifying that gender is either M or F (if it
    isn't, what's the best way to inform the calling code that a mistake was
    made?) and enforcing capitalization of both first name and last name.

b)  Buildings should support a function enter that takes a person and a room
    number. The building should then keep track of anyone who enters/leaves the
    building and respond to some type of where_is(person) query with the room
    number that person is in. Ensure, naturally, that no one can be in more
    than one building at a time.

c)  Make the building class iterable over the people in it. That is, make it
    possible to write a for loop of the form:
        for person in building:
            ...

d)  Implement a class that represents an office building, an object that
    behaves the same as a building but only allows people to enter if they are
    on a list of employees passed in when the OfficeBuilding is instantiated.
    You may want to look up the super function in the Python documentation
    concerning classes.

e)  Implement a class that represents a house. The House class should implement
    enter to take only a Person object, and the House class should not support
    where_is at all. It should instead support at_home(Person), a function that
    returns a Boolean.

f)  Modify all buildings, houses included, to remember their location as an
    (x, y) tuple. Then make it possible to call some function that takes such
    a tuple and returns the building object at that tuple or None if no
    building exists at that location. You may choose whether any given location
    can only hold one building or multiple buildings, but you need to handle
    this corner case in some logical fashion.

g)  With a minimum of code duplication, modify the Building class so that
    bldg[roomnumber] = person accomplishes the same thing as
    bldg.enter(person, roomnumber). Be careful with how you do this if you
    chose to inherit any classes from Building (which you should have).
"""

class Person:
    def __init__(self, firstname, lastname, gender):
        # self, string, string, boolean
        self.name = firstname.capitalize() + lastname.capitalize()
        self.gender = gender
        self.bldg = False
        self.room = -1

class Building:
    def __init__(self, xlocation=0, ylocation=0):
        self.ppl = []
        self.count = 0
        self.location = (xlocation, ylocation)


    def enter(self, person, room_no):
        if room_no = -1: #leave bldg
            if person in self.ppl:
                self.ppl.remove(person)
            person.room = -1
            person.bldg = False
                break
                
        for a in self.ppl:
            if a == person: #person already in bldg, just switching rooms
                a.room = room_no #update bldg list
                person.room = room_no #update person
                    break

        if person.bldg = True: #person in diff bldg
            print("please leave your current building before entering this one")
                break

        person.room = room_no
        person.bldg = True
        self.ppl.append(person) #person going to bldg for first time

    def where_is(self, person):
        if person.bldg == False:
            print("This person could not be found in a building") 
                break

        for a in self.ppl:
            if a == person:
                if a.room != None: 
                    return a.room
                else:   
                    print("This person is not in a room in this building")
                        break
        
    def __iter__(self):
        return self

    def next(self):
        if self.count == len(self.ppl):
           raise StopIteration
            
        self.count += 1
        return self.ppl[count]

class OfficeBuilding(Building):
    def __init__(self, approved, xlocation=0, ylocation=0):
        self.ppl = []
        self.count = 0
        self.appr = approved
        self.location = (xlocation, ylocation)

    def enter(self, person, room_no):
        if person in self.appr:
            super.enter(self, person, room_no)
        else:
            print("Access denied: this person is not approved to enter")

class House(Building):
    def __init__(self, xlocation=0, ylocation=0):
        super(House, self).__init__() #do I have to pass in args?

    def enter(self, person):
        if person.bldg == True:
            print("Please leave your building before trying to come home")
                break

        if not person in self.ppl: 
            self.ppl.append(person)
            person.bldg = True

        #no way to leave the house

    def where_is(self, person):
        pass

    def at_home(self, person):
        if person in self.ppl:
            return True
        return False

class BldgGrid:
    # how can I put buildings on the grid if the grid doesn't exist yet?  
    # Should this be a global instead of a class?
    # I would pass in a grid parameter for each of the classes' init things

    def __init__(self):
        self.bldgs = []

    def addBldg(self, batiment):
        t = type(batiment)
        tup = batiment.location, t
        self.bldgs.append(tup)

    def searchGrid(self, batiment):
        loc = batiment.location
        for a in self.bldgs:
            if a[0] == loc:
                return a[1]
        print("There is not building at this location")

class Building2(Building):
    def __init__(self):
        bldgdict = {}

    def enter(self, person, roomnumber):
        if room_no = -1: #leave bldg
            person.bldg = False
            for key, value in bldgdict.items():
                if value == person:
                    del blgdict[key]
            #delete this key, value

        for key, value in bldgdict: #person in bldg, just switching rooms
            if value == person:
                key = roomnumber
                    break

        if person.bldg = True: #person in diff bldg
            print("please leave your current building before entering this one")
                break

        bldgdict[roomnumber] = person #put person in bldg
        
    def where_is(self, person):
        if person.bldg == False:
            print("This person could not be found in a building") 
                break

        for key, value in bldgdict:
            if value == person:
                return key

        print("This person is not in a room in this building")
            break


