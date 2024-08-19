from activity import Activity, CONN, CURSOR
from feeling import Feeling, CONN, CURSOR
from person import Person, CONN, CURSOR
import ipdb


feeling1 = Feeling("Happy") 
feeling2 = Feeling("Sad") 
feeling3 = Feeling("Excited") 
feeling4 = Feeling("Anxious") 
feeling5 = Feeling("Relaxed")

person1 = Person("Alice") 
person2 = Person("Bob") 
person3 = Person("Charlie") 
person4 = Person("Diana") 
person5 = Person("Ethan")

Feeling.create_table()
feeling1.save()
feeling2.save()
feeling3.save()

Person.create_table()
person1.save()

# activity1 = Activity("Jogging", feeling1, person2) 
# activity2 = Activity("Reading", feeling2, person3) 
# activity3 = Activity("Dancing", feeling3, person1) 
# activity4 = Activity("Meditation", feeling4, person5) 
# activity5 = Activity("Watching a Movie", feeling5, person4)


ipdb.set_trace()


