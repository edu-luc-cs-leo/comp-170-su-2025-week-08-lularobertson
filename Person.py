from Birthday import Birthday


class Person:

    def __init__(self, first_name, last_name):
        """A person is defined by a first and last name, a birthday in the 
        form (month, day), and a city they live in. Additional fields may 
        be added here later. A new object requires only a first and last 
        name to instatiate. The remaining fields can be set later using 
        the corresponding mutator methods."""
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = None
        self.city = None

    def introduce(self):
        """Simple way for a person object to introduce itself."""
        print(
            f"Hello, my name is {self.first_name} and my birthday is on {self.say_birthday()}"
        )

    def set_birthday(self, month, day):
        """Mutator for birthday. Uses our very own Birthday class."""
        self._birthday = Birthday(month, day)

    def say_birthday(self):
        day = self._birthday.get_day()
        month_number = self._birthday.get_month() # accessor
        month = self.get_month(month_number) #accessor
        suffix = self.get_suffix(day)
        return f"{day}{suffix} of {month}"
    
    def get_month(self, month):
        month_word = ""
        return {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}.get(month)
    
    def get_suffix(self, day):
        return {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")

    def set_city(self, city):
        """Mutator for city."""
        self.city = city

    def get_first_name(self):
        """Accessor for first name"""
        return self.first_name

    def get_last_name(self):
        """Accessor for last name"""
        return self.last_name

    def __str__(self):
        """String representation for the object"""
        return f"[ {self.first_name} {self.last_name}]"
    
    def __lt__(self, other) -> bool:
        is_less = False
        if self.first_name < other.first_name:
            is_less = True
        else:
            is_less = False
        return is_less


p1 = Person("Alex", "Petrongelli")
p1.set_birthday(9, 3)
print(p1.say_birthday())


"""
Reflection:

Our code for both SuperAles and SuperVehicles is basically the same. I didn't include many comments on this assignment
because I thought it was pretty straight foreword. I didn't include any testing code because I guess I didn't think of that,
and also writing tests for objects kind of confuses me. Including with this assignment, the testing code I wrote was hard.

I'm still working on writing the methods and all the things correctly. It seems less intuitive now with the methods and mutators and accessors.
It's hard to translate what I want the computer to do to actual words and functions.

"""