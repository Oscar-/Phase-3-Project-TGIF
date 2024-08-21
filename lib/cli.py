from feeling import Feeling
from person import Person
from activity import Activity
from result import Results
from helpers import (
    print_person,
    print_cur_person,
    print_feeling,
    print_all_feelings,
    print_all_feelings_for_person,
    print_activity,
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
        print(f"Current person set to: {cur_person.name}")
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
        print("0. Back to main menu")
        choice = get_choice()
        
        if int(choice) == 0:
            break  # Return to the previous menu
        elif int(choice) in range(1, 9):
            # Set the current person based on choice
            set_cur_person(choice)
            sub2_main()
        else:
            print("Invalid choice. Please try again.")

def sub2_main():
    while True:
 
        if not cur_person:
            choice = input("No person selected. Please select a person first.")
            set_cur_person(choice)
           

        else:
            print(f"How are you feeling on this Friday, {cur_person.name}?")
            print("1. Happy")
            print("2. Sad")
            print("3. Excited")
            print("4. Anxious")
            print("5. Relaxed")
            print("0. Back to previous menu")
            choice = input('Enter choice\n')
            if int(choice) == 0:
                break  # Return to the previous menu
            elif int(choice) in range(1, 6):
                set_cur_feeling(choice)
                sub3_main()
                # select_feeling()
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
                break  # Return to the previous menu
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
                break  # Return to the previous menu

         
def menu():
    print(f"""
        Welcome to TGIF!
        Enter 0 to exit 
        Enter 1 to start quiz
        """)

if __name__ == "__main__":
    main()
