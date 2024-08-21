from feeling import Feeling
from person import Person
from activity import Activity
from result import Results
from helpers import (
    print_person,
    print_cur_person,
    # set_cur_person,
    # cur_person,
    print_feeling,
    print_all_feelings,
    print_all_feelings_for_person,
    print_activity,
    print_all_activities,
    print_all_activities_for_person
)
# import helpers

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
        # choice = input('Enter choice\n')
        if int(choice) == 0:
            break  # Return to the previous menu
        elif int(choice) in range(1, 8):
            # Set the current person based on choice
            set_cur_person(choice)
            sub2_main()
        else:
            print("Invalid choice. Please try again.")

def sub2_main():
    while True:
        # print(f"Debug: cur_person = {cur_person}") #helpers import
        if not cur_person:
            choice = input("No person selected. Please select a person first.")
            set_cur_person(choice)
            # sub_main()
            # continue

        else:
            print(f"How are you feeling on this Friday, {cur_person.name}?")
            print("1. View All Feelings")
            print("2. View All Activities")
            print("3. View Feelings for Current Person")
            print("4. View Activities for Current Person")
            print("0. Back to previous menu")
            choice = input('Enter choice\n')
            if int(choice) == 0:
                break  # Return to the previous menu
            elif int(choice) == 1:
                print_all_feelings()
                select_feeling()
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

if __name__ == "__main__":
    main()
