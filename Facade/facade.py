# -*- coding: utf-8 -*-


class User(object):
    # user class
    def is_login(self):
        return True

    def has_privilege(self, privilege):
        return True


class Course(object):
    # course class
    def can_be_learned(self):
        return True


class Lab(object):
    # lab class
    def can_be_started(self):
        return True


class Client(object):
    # client class used to start a lab
    def __init__(self, user, course, lab):
        self.user = user
        self.course = course
        self.lab = lab

    def start_lab(self):
        
        if self.user.is_login() and self.lab.can_be_started():
            print("start lab")
        else:
            print("can not start lab")


class FacadeLab(object):
    # new lab class, applied object-oriented pattern
    def __init__(self, user, course, lab):
        self.user = user
        self.course = course
        self.lab = lab
    
    def can_be_started(self):
        if self.user.is_login() and self.course.can_be_learned() and self.lab.can_be_started():
            return True
        else:
            return False


class NewClient(object):
    
    def __init__(self, facade_lab):
        self.lab = facade_lab

    def start_lab(self):
        if self.lab.can_be_started:
            print("start lab")
        else:
            print("can not start lab")


if __name__ == '__main__':
    user = User()
    course = Course()
    lab = Lab()
    client = Client(user, course, lab)
    client.start_lab()

    print("Use Facade Pattern:")
    facade_lab = FacadeLab(user, course, lab)
    facade_client = NewClient(facade_lab)
    facade_client.start_lab()
