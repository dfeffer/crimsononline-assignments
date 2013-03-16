from pprint import pprint # pretty print output formatting
from question1 import (common_words, common_words_min, common_words_tuple, common_words_safe)
from question2 import parse_links_regex, parse_links_xpath
from question4 import GITHUB_URL

print "==testing question 1=="
print "common_words... ",
pprint(common_words("words.txt"))

print "common_words_min 2... ",
pprint(common_words_min("words.txt", 2))

print "common_words_min 5... ",
pprint(common_words_min("words.txt", 5))

print "common_words_min 9... ",
pprint(common_words_min("words.txt", 9))

print "common_words_tuple w/ min 5... ",
pprint(common_words_tuple("words.txt", 5))

print "common_words_safe... ",
pprint(common_words_safe("words_fail.txt", 5))
print


print "==testing question 2=="
print "regex... ",
pprint(parse_links_regex("crimson.html"))
pprint(parse_links_xpath("crimson.html"))
print


print "==testing question 3=="
import question3

print "creating Grid..."
grid = question3.BldgGrid()
print grid.bldgs

print "creating person 1 MALE..."
person1 = question3.Person("John", "Doe", "M")
print person1.name
print person1.gender
print person1.bldg
print person1.room

print "creating person 2 FEMALE..."
person2 = question3.Person("Jane", "Doe", 'F')

print "creating person 3 NOT M OR F..."
person3 = question3.Person("J", "Doe", 'T')

print "adding building1 to grid..."
building1 = question3.Building(grid)
print building1.ppl
print building1.location
print grid.bldgs

print "putting both people in building1..."
pprint(building1.enter(person1, 1))
pprint(building1.enter(person2, 2))

print "iterating over people in building1..."
print building1.ppl
for p in building1:
	pprint(building1.where_is(p))

print "person1 moving rooms..."
pprint(building1.enter(person1, 3))
pprint(building1.where_is(person1))

print "adding office 1 to grid..."
authorize = [person1]
office = question3.OfficeBuilding(grid, authorize, 5, 20)
print office.ppl
print office.location
print grid.bldgs
 
print "person1 trying to go to office without leaving building1..."
pprint(office.enter(person1, 12))

print "both leaving building1..."
pprint(building1.enter(person1, -1))
pprint(building1.enter(person2, -1))

print "person1 going to office AUTHORIZED..."
pprint(office.enter(person1, 1))

print "person2 going to office UNAUTHORIZED..."
pprint(office.enter(person2, 1))

print "iterating and checking who is in office and where..."
print office.ppl
for p in office:
	pprint(office.where_is(p))

print "creating home..."
home = question3.House(grid, 50, 50)
print home.ppl
print home.location
print grid.bldgs

print "person1 going home without leaving office..."
pprint(home.enter(person1))

print "person1 leaving office..."
pprint(office.enter(person1, -1))

print "going home..."
pprint(home.enter(person1))

print "checking to see if person1 is home..."
pprint(home.at_home(person1))

print "checking to see if person2 is home..."
pprint(home.at_home(person2))

print "searching grid..."
pprint(grid.searchGrid((50, 50)))

print "adding type 2 building2..."
building2 = question3.Building2(grid, 40, 40)
print building2.bldgdict
print building2.location
print grid.bldgs

print "person2 going to building2..."
pprint(building2.enter(person2, 1))
print building2.bldgdict
print person2.bldg

print "iterating over people in building2..."
print building2.bldgdict
for key in building2.bldgdict.iterkeys():
	pprint(key.name)
	pprint(building2.where_is(key))

print "leaving building2..."
pprint(building2.enter(person2, -1))


print "==testing question 4=="
print "github url: {}".format(GITHUB_URL)
print


print "==testing question 5=="
# ???
print