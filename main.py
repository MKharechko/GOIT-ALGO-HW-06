from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        self.data_name = set()

    def name_data(self, name):
        self.data_name.add(name)


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.data_phone = set() 

    def phone_data(self, phone):
        if len(str(phone)) != 10:
            print("Phone must be 10 symbols")
        else:
            self.data_phone.add(phone)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def add_phone(self, phone):
        if len(str(phone)) == 10:
            self.phones.append(Phone(phone))
        else:
            print("Phone must be 10 symbols")

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        if len(str(new_phone)) != 10:
            print("New phone must be 10 symbols")
            return 
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                return
        print("Old phone not found")
            
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find_record(self, name):
        return self.data.get(name, None)
    
    def delete_record(self, name):
        if name in self.data:
            del self.data[name]
        else:
            print("Record not found")

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())

    
book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

john = book.find_record("John")
john.edit_phone("1234567890", "1112223333")

found_phone = john.find_phone("5555555555")
print(f"{john.name.value}: {found_phone}")

book.delete_record("Jane")

print(john)
print(book)


