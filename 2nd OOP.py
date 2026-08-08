class poop_employee:
    def __init__(self):
        print("poop employee made 💩")

    def __del__(self):
        print("poop in toilet 🚽")


def create_obj():
    print("Making totally normal employee")
    employee_of_poop = poop_employee()
    print("Totally normal employee made")
    print("That will be $1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
    return employee_of_poop


print("Calling create_obj function...")
employee_of_poop = create_obj()
print("Program end")
