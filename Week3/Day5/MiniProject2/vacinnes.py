class Human:
    def __init__(self, id_number, name, age, priority, blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
        self.next = None
        self.prev = None
        self.family = Queue()
    
    def add_family_member(self, person):
        self.family.add_person(person)
        while self.family.head != None:
            person.family.add_person(self.family.get_next)

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_person(self, person):
        if self.head == None:
            self.head = person
            self.tail = person
        else:
            self.tail.next = person
            self.tail = person

    def find_in_queue(self, person):
        find_person = self.head
        while find_person != person:
            find_person = find_person.next
        return find_person

    def swap(self, person1, person2):
        person1.next, person2.next = person2.next, person1.next
        person1.prev, person2.prev = person2.prev, person1.prev

    def get_next(self):
        if self.head.next == None:
            person = self.head
            self.head = None
            self.tail = None
        else:
            person = self.head
            self.head = person.next
            person.next = None
        return person

    def get_next_blood_type(self, blood_type):
        if self.head.next == None:
            person = self.head
            self.head = None
            self.tail = None
        else:
            person = self.head
            self.head = person.next
            person.next = None
        return person.blood_type if person != None else None

    def sort_by_age(self):
        pass

