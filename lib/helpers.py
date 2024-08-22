from person import Person
from feeling import Feeling
from activity import Activity
from result import Results
from __init__ import CURSOR, CONN


cur_person = None


def print_cur_person():
    # global cur_person
    if cur_person:
        return (f'Current person set to: {cur_person.name}.')
    else:
        return (f'No current person set')

def print_person(id):
    person_instance = Person.find_by_id(id)
    if person_instance:
        print(f'Name: {person_instance.name}')
    else:
        print(f'Person with ID {id} not found')

def print_all_persons():
    persons = Person.get_all()
    if persons:
        for person in persons:
            print(f'Name: {person.name}')
    else:
        print('No persons found')

def print_feeling(id):
    feeling_instance = Feeling.find_by_id(id)
    if feeling_instance:
        print(f'ID: {feeling_instance.id}, Feeling Name: {feeling_instance.feeling_name}')
    else:
        print(f'Feeling with ID {id} not found')
    
def print_all_feelings():
    feelings = Feeling.get_all()
    if feelings:
        for feeling in feelings:
            print(f'ID: {feeling.id}, Feeling Name: {feeling.feeling_name}')
    else:
        print('No feelings found')

def print_all_feelings_for_person(person_id): 
    person_id = int(person_id) # Ensure person_id is an integer 
    feelings = Feeling.get_feelings_for_person(person_id) # Use the correct variable 
    for feeling in feelings: 
        print(f'{feeling.id}. {feeling.feeling_name}') # Use the correct attribute name

def print_activity(id):
    activity_instance = Activity.find_by_id(id)
    if activity_instance:
        print(f'ID: {activity_instance.id}, Activity Name: {activity_instance.activity_name}')
    else:
        print(f'Activity with ID {id} not found')
        
def print_all_activities():
    activities = Activity.get_all()
    if activities:
        for activity in activities:
            print(f'Activity: {activity.activity_name}')
    else:
        print('No activities found')

def print_activity(id):
    activity_instance = Activity.find_by_id(id)
    if activity_instance:
        print(f'ID: {activity_instance.id}, Activity Name: {activity_instance.activity_name}')
    else:
        print(f'Activity with ID {id} not found')

def print_all_activities():
    activities = Activity.get_all()
    if activities:
        for activity in activities:
            print(f'Activity: {activity.activity_name}')
    else:
        print('No activities found')

def print_all_activities_for_person(person_id):
    activities = Activity.get_activities_for_person(person_id)
    if activities:
        for activity in activities:
            print(f'Activity ID: {activity.id}, Name: {activity.activity_name}, Feeling ID: {activity.feeling_id}')
    else:
        print(f'No activities found for person with ID {person_id}.')


def print_activities_for_feeling(feeling_id):
    # Retrieve the feeling by ID
    feeling = Feeling.find_by_id(feeling_id)
    
    if not feeling:
        print(f"Feeling with ID {feeling_id} not found.")
        return
    
    # Retrieve activities associated with the feeling
    activities = Activity.get_activities_by_feeling(feeling_id)
    
    if activities:
        print(f"Activities related to the feeling '{feeling.feeling_name}':")
        for activity in activities:
            print(f"- {activity.activity_name}")
    else:
        print(f"No activities found for the feeling '{feeling.feeling_name}'.")
    




# import ipdb; ipdb.set_trace()