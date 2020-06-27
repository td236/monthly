class core:
    def __init__(self, name, id, colour):
        self.name = name
        self.id = id
        self.colour = colour

    def change_name(self, name):
        self.name = name

    def change_colour(self, colour):
        self.colour = colour


class category(core):
    pass
    #list of events

class month(core):
    pass#first day last day


class event(core):
    def __init__(self, name, id, colour, amount, date, categories):
        super().__init__(name, id, colour)
        self.date = date
        self.amount = amount
        self.categories = categories

    def change_amount(self, amount):
        self.amount = amount

    def change_name(self, date):
        self.date = date

    def add_category(self, category):
        self.categories.append(category)

    def remove_category(self, category):
        self.categories.remove(category)


class user(core):
    def __init__(self, name, id, colour):
        super().__init__(name, id, colour)

    events=[]
    categories=[]
    months=[]

    def create_category(self, name, id, colour):
        self.categories.append(category(name, id, colour))

    def create_event(self, name, id, colour, amount, date, categories):
        self.events.append(event(name, id, colour, amount, date, categories))
