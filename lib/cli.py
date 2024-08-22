from feeling import Feeling
from person import Person
from activity import Activity
from result import Results
from helpers import (
    # print_person,
    print_cur_person,
    # print_feeling,
    # print_all_feelings,
    print_all_feelings_for_person,
    # print_activity,
    print_all_activities,
    print_all_activities_for_person
)

cur_feeling = None
cur_activity = None
cur_person = None

def set_cur_person(person_id):
    global cur_person
    person_id = int(person_id)  # Ensure person_id is an integer
    cur_person = Person.find_by_id(person_id)
    
    if cur_person:
        return print_cur_person()
    else:
        print(f"Person with ID {person_id} not found.")

def set_cur_feeling(feeling_id):
    global cur_feeling
    feeling_id = int(feeling_id)  # Ensure feeling_id is an integer
    cur_feeling = Feeling.find_by_id(feeling_id)
    if cur_feeling:
        print(f"Current feeling set to: {cur_feeling.feeling_name}")
    else:
        print(f"feeling with ID {feeling_id} not found.")

def set_cur_activity(activity_id):
    global cur_activity
    activity_id = int(activity_id)  # Ensure feeling_id is an activity
    cur_activity = Activity.find_by_id(activity_id)
    if cur_activity:
        print(f"Current activity set to: {cur_activity.activity_name}")
    else:
        print(f"activity with ID {activity_id} not found.")

def get_choice():
    while True:
        try:
            choice = int(input('Enter choice\n'))
            return choice
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    while True:
        menu()
        choice = input('Enter choice\n')
        if int(choice) == 0:
            print('Exiting...')
            break  # Exit the main loop
        elif int(choice) == 1:
            sub_main()

def sub_main():
    while True:
        print("Who are you?")
        print("1. Oscar")
        print("2. Sebastian")
        print("3. Linda")
        print("4. Audrey")
        print("5. Jason")
        print("6. Stefan")
        print("7. Rachel")
        print("8. Manage Persons")
        print("0. Back to main menu")
        choice = get_choice()
        if int(choice) == 0:
            break  
        elif int(choice) in range(1, 8):
            set_cur_person(choice)
            sub2_main()
        elif int(choice) == 8:
            manage_persons_menu()
        else:
            print("Invalid choice. Please try again.")

def sub2_main():
    while True:
        if not cur_person:
            choice = input("No person selected. Please select a person first.")
            set_cur_person(choice)

        else:
            print(f"How are you feeling today, {cur_person.name}?")
            print("1. Happy")
            print("2. Sad")
            print("3. Excited")
            print("4. Anxious")
            print("5. Relaxed")
            print("0. Back to previous menu")
            choice = input('Enter choice\n')
            if int(choice) == 0:
                break 
            elif int(choice) in range(1, 6):
                set_cur_feeling(choice)
                sub3_main()
            elif int(choice) == 2:
                print_all_activities()
            elif int(choice) == 3:
                if cur_person:
                    print_all_feelings_for_person(cur_person.id)
                else:
                    print("No person selected. Please select a person first.")
            elif int(choice) == 4:
                if cur_person:
                    print_all_activities_for_person(cur_person.id)
                else:
                    print("No person selected. Please select a person first.")
            else:
                print("Invalid choice. Please try again.")

def sub3_main():
    while True:
        if not cur_feeling:
            choice = input("No feeling selected. Please select a feeling first.")
            set_cur_feeling(choice)
            return 
        else:
            print(f"{cur_person.name}, since you are feeling {cur_feeling.feeling_name}, choose one of the following activities.")
            print("1. Smile creepily at strangers")
            print("2. Write tragic poetry in the dark")
            print("3. Plan world domination")
            print("4. Imagine worst-case scenarios")
            print("5. Contemplate existence while napping")
            print("6. Laugh maniacally in the mirror")
            print("7. Practice your evil laugh")
            print("8. Dance on the grave of your fears") 
            print("9. Pretend to be a ghost in your own house")
            print("10. Count the ways things could go wrong")
            print("0. Back to previous menu")
            choice = input('Enter choice\n')
            if int(choice) == 0:
                break 
            elif int(choice) in range(1, 11):
                set_cur_activity(choice)
                sub4_main()
                
def sub4_main():
    while True:
        if not cur_activity:
            choice = input("No activity selected. Please select an activity first.")
            set_cur_activity(choice)
            return
        else: 
            print("Great choice! Thanks for playing.")
            print("0. Back to previous menu")
            choice = input('Enter choice\n')
            if int(choice) == 0:
                break  
        
def select_feeling():
    print("Select a feeling by number:")
    feelings = Feeling.get_all()
    for index, feeling in enumerate(feelings, start=1):
        print(f"{index}. {feeling.feeling_name}")
    
    try:
        feeling_choice = int(input("Enter choice:\n"))
        if 1 <= feeling_choice <= len(feelings):
            selected_feeling = feelings[feeling_choice - 1]
            print(f"You selected: {selected_feeling.feeling_name}")
            handle_selected_feeling(selected_feeling)
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def handle_selected_feeling(feeling):
    # Example logic: Display feeling details
    print(f"Details for feeling: {feeling.feeling_name}")
    activities = Activity.get_activities_by_feeling(feeling.id)
    if activities:
        print("Activities related to this feeling:")
        for activity in activities:
            print(f"- {activity.activity_name}")
    else:
        print("No activities found for this feeling.")        

def menu():
    print(f"""
        Welcome to TGIF!
        Enter 0 to exit 
        Enter 1 to start quiz
        """)
    
def sub_menu():
    print(f"""
      Great choice! Thanks for playing. 
        """)
    
def manage_persons_menu():
    while True:
        print("""
        Manage Persons:
        1. Create a new person
        2. View all persons
        3. Update a person
        4. Delete a person
        0. Back to main menu
        """)
        choice = get_choice()
        if choice == 0:
            break
        elif choice == 1:
            create_person()
        elif choice == 2:
            view_all_persons()
        elif choice == 3:
            update_person()
        elif choice == 4:
            delete_person()
        else:
            print("Invalid choice. Please try again.")

def create_person():
    name = input("Enter the person's name: ")
    new_person = Person(name=name)
    new_person.save()
    print(f"Person '{name}' created with ID {new_person.id}.")

def view_all_persons():
    persons = Person.get_all()
    if persons:
        for person in persons:
            print(f"ID: {person.id}, Name: {person.name}")
    else:
        print("No persons found.")

def update_person():
    person_id = int(input("Enter the ID of the person to update: "))
    person = Person.find_by_id(person_id)
    if person:
        new_name = input(f"Enter the new name for {person.name}: ")
        person.name = new_name
        person.save() 
        print(f"Person ID {person_id} updated to '{new_name}'.")
    else:
        print(f"Person with ID {person_id} not found.")

def delete_person():
    person_id = int(input("Enter the ID of the person to delete: "))
    person = Person.find_by_id(person_id)
    if person:
        person.delete()
        print(f"Person ID {person_id} deleted.")
    else:
        print(f"Person with ID {person_id} not found.")

if __name__ == "__main__":
    main()

