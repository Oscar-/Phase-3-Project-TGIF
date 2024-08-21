from feeling import Feeling 
from person import Person
from activity import Activity
from result import Results 
from helpers import(
    print_all_persons,
    print_cur_person,
    print_person,
    set_cur_person,
    print_feeling,
    print_all_feelings,
    print_all_feelings_for_person,
    print_activity,
    print_all_activities
)


global cur_person 
cur_person = None 
cur_feeling = None
cur_activty = None 

def main():
    while True:
        print(f"""
        Welcome to TGIF!
        Enter 0 to exit 
        Enter 1 to start quiz
        """)
        choice = input('Enter choice\n')
        if(int(choice) == 0):
            print('Exiting...')
            exit()
        elif(int(choice) == 1):
            sub_main()
            break
            


            

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
    
        choice = input('Enter choice\n')
        if(int(choice) == 1):
            sub2_main()
            break
            

                        
        # elif(int(choice) == 2):
            
0

        # elif(int(choice == 3)):
        
        # elif(int(choice == 4)):
        
        # elif(int(choice == 5)):
        
        # elif(int(choice == 6)):
        
        # elif(int(choice == 7)):
 
def sub2_main():
    while True: 
        print("How are you feeling?")
        print('1. Happy')
        print('2. Sad')
        print('3. Excited')
        print('4. Anxious')
        print('5. Relaxed')
        break 

      
# def menu():
   

if __name__ == "__main__":
    main()




