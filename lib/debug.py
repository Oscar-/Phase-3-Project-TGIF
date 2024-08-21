from activity import Activity, CONN, CURSOR
from feeling import Feeling, CONN, CURSOR
from person import Person, CONN, CURSOR
from result import Results, CONN, CURSOR
import ipdb


# People instances
person1 = Person("Oscar")
person2 = Person("Sebastian")
person3 = Person("Linda")
person4 = Person("Audrey")
person5 = Person("Jason")
person6 = Person("Stefan")
person7 = Person("Rachel")


person1.save()
person2.save()
person3.save()
person4.save()
person5.save()
person6.save()
person7.save()


feeling1 = Feeling("Happy") 
feeling2 = Feeling("Sad") 
feeling3 = Feeling("Excited") 
feeling4 = Feeling("Anxious") 
feeling5 = Feeling("Relaxed")

Feeling.create_table()
feeling1.save()
feeling2.save()
feeling3.save()
feeling4.save()
feeling5.save()


# Dark Humor Activities
activity1 = Activity("Smile creepily at strangers", feeling1.id, person1.id)       # Happy
activity2 = Activity("Write tragic poetry in the dark", feeling2.id, person2.id)   # Sad
activity3 = Activity("Plan world domination", feeling3.id, person3.id)             # Excited
activity4 = Activity("Imagine worst-case scenarios", feeling4.id, person4.id)      # Anxious
activity5 = Activity("Contemplate existence while napping", feeling5.id, person5.id)  # Relaxed
activity6 = Activity("Laugh maniacally in the mirror", feeling1.id, person6.id)    # Happy
activity7 = Activity("Practice your evil laugh", feeling4.id, person7.id)          # Anxious
activity8 = Activity("Dance on the grave of your fears", feeling5.id, person3.id)  # Relaxed
activity9 = Activity("Pretend to be a ghost in your own house", feeling2.id, person6.id)  # Sad
activity10 = Activity("Count the ways things could go wrong", feeling3.id, person7.id)  # Excited

Activity.create_table()
activity1.save()
activity2.save()
activity3.save()
activity4.save()
activity5.save()
activity6.save()
activity7.save()
activity8.save()
activity9.save()
activity10.save()

# Creating Results instances 
result1 = Results(person1.id, feeling1.id, activity1.id) 
result2 = Results(person2.id, feeling2.id, activity2.id) 
result3 = Results(person3.id, feeling3.id, activity3.id) 
result4 = Results(person4.id, feeling4.id, activity4.id) 
result5 = Results(person5.id, feeling5.id, activity5.id)

Results.create_table()
result1.save() 
result2.save() 
result3.save() 
result4.save() 
result5.save()

ipdb.set_trace()


