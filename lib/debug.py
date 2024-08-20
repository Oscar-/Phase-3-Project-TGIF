from activity import Activity, CONN, CURSOR
from feeling import Feeling, CONN, CURSOR
from person import Person, CONN, CURSOR
from result import Results, CONN, CURSOR
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
feeling4.save()
feeling5.save()


Person.create_table()
person1.save()
person2.save()
person3.save()
person4.save()
person5.save()

Results.create_table()

activity1 = Activity("Jogging", feeling1.id, person2.id) 
activity2 = Activity("Reading", feeling2.id, person3.id) 
activity3 = Activity("Dancing", feeling3.id, person1.id) 
activity4 = Activity("Meditation", feeling4.id, person5.id) 
activity5 = Activity("Watching a Movie", feeling5.id, person4.id)


Activity.create_table()


ipdb.set_trace()


