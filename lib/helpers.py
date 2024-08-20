from person import Person
from feeling import Feeling
from activity import Activity
from result import Results


# ✅ 2. A function `print_owner(id)` that finds the owner with id `id` and prints it out.
def print_person(id):
    persons = Person.find_by_id(id)
    for person in persons:
        print(f'{person.id}')

# # ✅ 3. A function `print_pet(id)` that finds the pet with id `id` and prints it out.
# def print_pet(id):
#     pass

# ✅ 4. A function `print_all_persons()` that prints all persons
def print_all_persons():
    # get all the owners 
    persons = Person.get_all()
    for person in persons:
        print(f'{person.name}')

# # ✅ 5. A function `print_all_pets_for_owner(id)` that prints all pets for the owner with the id `id`
# def print_all_pets_for_owner(id):
#     pets = Pet.get_owner_pets(id)
#     for pet in pets:
#         print(f'{pet.id}. {pet.name}')

# # ✅ 6. A function `print_all_apps_for_owner(id)` that prints all appointments for all the pets for owner with id `id`
# def print_all_apps_for_owner(id):
#     pass

# # ✅ 7. A function `print_apps_for_one_pet(id)` that prints all the appointments for the pet with id `id`
# def print_apps_for_one_pet(id):
#     pass

# # ✅ 8. A function `exit_program()` that prints will exit our cli
# def exit_program():
#     pass

import ipdb; ipdb.set_trace()