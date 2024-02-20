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
    
    def add_phone(self):
        phone = Phone()
        phone.validation()
        #self.phones.append(phone)
        pass
    def remove_phone(self):
        pass
    def edit_phone(self,  old_phone, new_phone):
        pass
    def find_phone(self):
        pass
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, name):
        #self.data[name] = Phone()
        pass

    def find(self):
        pass
    def delete(self):
	    pass

# Створення нової адресної книги
book = AddressBook()
john_record = Record("John")
john_record.add_phone("1234567890")
print(john_record)
jane_record = Record("Jane")
book.add_record(jane_record)
for name, record in book.data.items():
        print(record)
