from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        # ToDo add check is value not empty
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        # ToDo add pnone number validation
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, number):
        self.phones.append(Phone(number))

    def del_phone(self, number):
        self.phones = [phone for phone in self.phones if phone.value != number]

    def find_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                 return phone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу
		pass

if __name__ == "__main__":
    record01 = Record("Name01")
    print(record01.name, len(record01.phones))
    assert str(record01.name) == "Name01"

    record01.add_phone("1234567890")
    record01.add_phone("1234567891")
    print(record01, len(record01.phones))
    assert len(record01.phones) == 2

    record01.del_phone("1234567891")
    assert len(record01.phones) == 1

    record01.add_phone("1234567891")
    record01.add_phone("1234567891")
    assert len(record01.phones) == 3

    record01.del_phone("1234567891")
    assert len(record01.phones) == 1

    # number not found
    assert record01.find_phone("1234567891") == None
    # number found
    assert record01.find_phone("1234567890") != None
    assert record01.find_phone("1234567890").value == "1234567890"

    print(record01, len(record01.phones))