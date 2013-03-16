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

class Person(object):
    def __init__(self, firstname, lastname, gender):
        # self, string, string, boolean
        print gender

        if not ((gender == "M") or (gender == 'F')):
            print("Please give either M or F for gender")
            # return

        self.name = firstname.capitalize() + lastname.capitalize()
        self.gender = gender
        self.bldg = False
        self.room = -1

class Building(object):
    def __init__(self, grid, xlocation=0, ylocation=0, cls="Building"):
        self.ppl = []
        self.count = 0
        self.location = (xlocation, ylocation)
        self.cls = cls
        grid.addBldg(self)
        
    def enter(self, person, room_no):
        if room_no == -1: #leave bldg
            if person in self.ppl:
                self.ppl.remove(person)
            person.room = -1
            person.bldg = False
            return
                
        for a in self.ppl:
            if a == person: #person already in bldg, just switching rooms
                a.room = room_no #update bldg list
                person.room = room_no #update person
                return

        if person.bldg == True: #person in diff bldg
            print("please leave your current building before entering this one")
            return

        person.room = room_no
        person.bldg = True
        self.ppl.append(person) #person going to bldg for first time

    def where_is(self, person):
        if person.bldg == False:
            print("This person could not be found in a building") 
            return

        for a in self.ppl:
            if a == person:
                if a.room != None: 
                    return a.room
                else:   
                    print("This person is not in a room in this building")
                    return
        
    def __iter__(self):
        return self

    def next(self):
        self.count += 1
        if self.count > len(self.ppl):
           raise StopIteration
            
        return self.ppl[self.count-1]

class OfficeBuilding(Building, object):
    def __init__(self, grid, approved, xlocation=0, ylocation=0, cls="OfficeBuilding"):
        self.ppl = []
        self.count = 0
        self.appr = approved
        self.location = (xlocation, ylocation)
        self.cls = cls
        grid.addBldg(self)

    def enter(self, person, room_no):
        if person in self.appr:
            super(OfficeBuilding, self).enter(person, room_no)
        else:
            print("Access denied: this person is not approved to enter")

class House(Building, object):
    def __init__(self, grid, xlocation=0, ylocation=0):
        self.cls = "House"
        super(House, self).__init__(grid, xlocation, ylocation, self.cls)
        
    def enter(self, person):
        if person.bldg == True:
            print("Please leave your building before trying to come home")
            return

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

class BldgGrid(object):
    # how can I put buildings on the grid if the grid doesn't exist yet?  
    # Should this be a global instead of a class?
    # I would pass in a grid parameter for each of the classes' init things

    def __init__(self):
        self.bldgs = []

    def addBldg(self, batiment):
        t = batiment.cls
        tup = (batiment.location, t)
        self.bldgs.append(tup)

    def searchGrid(self, (xlocation, ylocation)):
        loc = (xlocation, ylocation)
        for a in self.bldgs:
            if a[0] == loc:
                return a[1]
        print("There is not building at this location")

class Building2(Building, object):
    def __init__(self, grid, xlocation=0, ylocation=0, cls="Building2"):
        self.bldgdict = {}
        self.location = (xlocation, ylocation)
        self.count = 0
        self.cls = cls
        grid.addBldg(self)
        
    def enter(self, person, roomnumber):
        if roomnumber == -1: #leave bldg
            person.bldg = False
            for key, value in self.bldgdict.items():
                if value == person:
                    del self.blgdict[key]
            #delete this key, value

        for key in self.bldgdict.iterkeys(): #person in bldg, just switching rooms
            if key == person:
                self.bldgdict[key] = roomnumber
                return

        if person.bldg == True: #person in diff bldg
            print("please leave your current building before entering this one")
            return


        self.bldgdict[person] = roomnumber #put person in bldg
        person.bldg = True

    def where_is(self, person):
        if person.bldg == False:
            print("This person could not be found in a building") 
            return

        for key in self.bldgdict.iterkeys():
            if key == person:
                return self.bldgdict[key]

        print("This person is not in a room in this building")
        return

    def __iter__(self):
        return self

    def next(self):
        keyslist = self.bldgdict.keys()
        if self.count == len(keyslist):
           raise StopIteration
            
        self.count += 1
        return bldgdict[keyslist[self.count]]

