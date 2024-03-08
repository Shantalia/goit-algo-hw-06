from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
		pass

class Phone(Field):
    def validation(self):
        phone = self.value
        if len(phone) != 10:
            return "Wrong phone number!"
        else:
	        return phone

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def add_phone(self, phone):
        phone = Phone(phone)
        phone.validation()
        self.phones.append(phone)

    def remove_phone(self, phone):
        for ph in self.phones:
            if ph == phone:
                self.phones.remove(ph)
                return "Phone deleted."
            else:
                return "No such phone!"

    def edit_phone(self,  old_phone, new_phone):
        pass

    def find_phone(self):
        pass
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, name, phone):
        self.data[name] = Phone(phone)
        pass

    def find(self, name):
        if self.data[name]:
            return self.data[name]
        else:
            return "No such contact!"
    def delete(self, name):
        if self.data[name]:
            
            return "Contact deleted!"
        else:
            return "No such contact!"

# Створення нової адресної книги
book = AddressBook()
john_record = Record("John")
john_record.add_phone("1234567890")
print(john_record)
jane_record = Record("Jane")
book.add_record(jane_record)
for name, record in book.data.items():
        print(record)
