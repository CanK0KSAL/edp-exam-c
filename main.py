import random
import time


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
        self.country = country
        self.email = email

    def apply(self, university_name, course):
        event = ApplicationSentEvent({"student_name": self.name, "university": university_name, "course": course})
        communication_queue.append(event)
        print(f"\n[APPLY] {self.name} applied to {university_name} for the course: {course} (Event: {event.name})")


class University:
    def __init__(self, name):
        self.name = name

    def process_event(self, event):
        if isinstance(event, ApplicationSentEvent):
            self.handle_application(event)

    def handle_application(self, event):
        print(f"[RECIVED] University {self.name} received an application from {event.payload['student_name']} for the course {event.payload['course']}.")
        time.sleep(1)
        if random.choice([True, False]):
            self.accept_application(event)
        else:
            self.reject_application(event)

    def accept_application(self, event):
        acceptance_event = ApplicationAcceptedEvent(event.payload)
        print(f"[ACCEPTED] {event.payload['student_name']}'s application for {event.payload['course']} has been accepted by {self.name}.")

    def reject_application(self, event):
        rejection_event = ApplicationRejectedEvent(event.payload)
        print(f"[REJECTED] {event.payload['student_name']}'s application for {event.payload['course']} has been rejected by {self.name}.")


if __name__ == "__main__":
    
    student1 = Student("Alice Johnson", 19, "US", "alice.johnson@example.com")
    student2 = Student("Bob Smith", 21, "UK", "bob.smith@example.com")
    student3 = Student("Clara Lee", 22, "CA", "clara.lee@example.com")
    student4 = Student("Piotr Brundy", 22, "CA", "piotrlee@example.com")


    university = University("Wseiz")


    student1.apply(university.name, "Computer Science")
    student2.apply(university.name, "Business Administration")
    student3.apply(university.name, "Psychology")
    student4.apply(university.name, "Managmenent")


    # Process events
    print("\n[PROCESSING EVENTS]\n" + "-" * 30)
    time.sleep(2)
    for event in communication_queue:
        university.process_event(event)
