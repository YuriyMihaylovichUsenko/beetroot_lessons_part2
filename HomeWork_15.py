# For Task 1
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def greeter(self):
        print(f"Hallo, my name is {self.first_name} {self.last_name}."
              f"I'm {self.age} years old.")


per_1 = Person('Yuriy', "Labutenko", 18)


# For Task 2
class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self):
        return self.age * self.age_factor


dog1 = Dog(5)

# For Task 3
CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    def __init__(self, list_chan, cur_chan=0):
        self.cur_chan = cur_chan
        self.list_chan = list_chan

    def first_channel(self):
        self.cur_chan = self.list_chan[0]
        return self.cur_chan

    def last_channel(self):
        self.cur_chan = self.list_chan[-1]
        return self.cur_chan

    def turn_channel(self, chan):
        self.cur_chan = self.list_chan[chan - 1]
        return self.cur_chan

    def next_channel(self):
        if self.cur_chan == self.list_chan[-1]:
            self.cur_chan = self.list_chan[0]
        else:
            self.cur_chan = \
                self.list_chan[self.list_chan.index(self.cur_chan) + 1]
        return self.cur_chan

    def previous_channel(self):
        if self.cur_chan == self.list_chan[0]:
            self.cur_chan = self.list_chan[-1]
        else:
            self.cur_chan = \
                self.list_chan[self.list_chan.index(self.cur_chan) - 1]
        return self.cur_chan

    def current_channel(self):
        return self.cur_chan

    def is_exist(self, chan):
        if isinstance(chan, int):
            if chan <= len(self.list_chan):
                return 'Yes'
            else:
                return 'No'
        elif isinstance(chan, str):
            if chan in self.list_chan:
                return 'Yes'
            else:
                return 'No'


controller = TVController(CHANNELS)


def main():
    per_1.greeter()
    print(dog1.human_age())

    print(controller.first_channel() == "BBC")

    print(controller.last_channel() == "TV1000")

    print(controller.turn_channel(1) == "BBC")

    print(controller.next_channel() == "Discovery",
          controller.previous_channel() == "BBC",

          controller.current_channel() == "BBC",

          controller.is_exist(4) == "No",

          controller.is_exist("BBC") == "Yes")


if __name__ == '__main__':
    main()
