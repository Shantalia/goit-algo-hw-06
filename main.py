from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
		pass

class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError('Phone is incorrect')
        

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def add_phone(self, phone): #☑
        self.phones.append(Phone(phone))

    def remove_phone(self, phone): #☑
        for ph in self.phones:
            if str(ph.value) == phone:
                self.phones.remove(ph)
            else:
                return "No such phone!"

    def edit_phone(self,  old_phone, new_phone): #☑
        for ph in self.phones:
            if str(ph.value) == old_phone:
                ph.value = new_phone
            else:
                return "No such phone!"

    def find_phone(self, phone): #☑
        for ph in self.phones:
            if str(ph.value) == phone:
                return ph.value
            elif str(ph.value) != phone:
                continue
            else:
                return "No such phone!"

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, obj_rec): #☑
        self.data[obj_rec.name.value] = list(p.value for p in obj_rec.phones)

    def find(self, name): #☑
        for nm in self.data:
            if nm == name:
                return self.data.get(nm)
            elif nm != name:
                continue
            else:
                return "No such contact!"
        
    def delete(self, name): #☑
        for nm in self.data:
            if nm == name:
                del self.data[nm]
                return "Contact deleted!"
            elif nm != name:
                continue
            else:
                return "No such contact!"

    # Створення нової адресної книги
book = AddressBook()

    # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
book.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

    # Виведення всіх записів у книзі
for key, record in book.data.items():
    print(f'{key} : {record}')

    # Знаходження та редагування телефону для John
john = book.find("John")
john_record.edit_phone("1234567890", "1112223333")

print(john_record)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
found_phone = john_record.find_phone("1234567890")
print(f"{john_record.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
book.delete("Jane")

for key, record in book.data.items():
    print(f'{key} : {record}')