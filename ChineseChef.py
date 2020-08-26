from Chef import Chef

# Inheritance from class "Chef"
class ChineseChef(Chef):

    # Override a function from an inherited class
    def make_special_dish(self):
        print("The chef makes orange chicken")

    def make_fried_rice(self):
        print("The chef makes fried rice")