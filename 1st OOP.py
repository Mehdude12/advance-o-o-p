class OOP:
    def __init__(self):
        self.thy_name = ""

    def la_input(self):
        self.thy_name = input("Please enter a word: ")

    def la_output(self):
        print(f" The word is: {self.thy_name.upper()}")


capital_of_la_kingom = OOP()
capital_of_la_kingom.la_input()
capital_of_la_kingom.la_output()
