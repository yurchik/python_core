class Parent:

    def print_last_name(self):
        print('Yurchenko')


class Child(Parent):

    def print_first_name(self):
        print('Alexandr')

    def print_last_name(self):
        print('Petrusenko')

child1 = Child()

child1.print_last_name()
child1.print_first_name()