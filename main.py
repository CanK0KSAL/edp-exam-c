
class Event:
    def __init__(self, payload):
        self.payload = payload

class ApplicationSentEvent(Event):
    name = "application_sent"

class ApplicationRejectedEvent(Event):
    name = "application_rejected"

class ApplicationAcceptedEvent(Event):
    name = "application_accepted"

communication_queue = []

class Student:
    def __init__(self, name, age, country, email):
        self.name = name
        self.age = age
        self.country= country
        self.email= email

    def apply(self, university_name, course)
        event = ApplicationSentEvent({"student_name": self.name, "university": university_name, "course": course})
        communication_queue.append(event)
        print(f"\n[APPLY] {self.name} applied to {university_name} for the course: {course} (Event: {event.name})")

        
