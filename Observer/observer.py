# -*- coding: utf-8 -*-

import abc


class Subject(object):
    
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        # register an observer
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        # log off an observer
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
        
    def notify(self):
        # notify all observers
        for observer in self._observers:
            observer.update(self)


class Course(Subject):
    # Course object
    
    def __init__(self):
        super(Course, self).__init__()
        self._message = None

    @property
    def message(self):
        # message is a property
        return self._message

    @message.setter
    def message(self,msg):
        # message property setter
        self._message = msg
        self.notify()


class Observer(object):
    
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def update(self, subject):
        pass


class UserObserver(Observer):
    
    def update(self, subject):
        print("User observer: %s" % subject.message)


class OrgObserver(Observer):
    
    def update(self, subject):
       print("Organization observer: %s" % subject.message)


if __name__ == '__main__':
    # initialize a user observer
    user = UserObserver()
    # initialize an organization observer
    org = OrgObserver()

    # initialize a course
    course = Course()
    # register an observer
    course.attach(user)
    course.attach(org)


    # set course.message, all observers will be notified
    course.message = "two observers"

    # detach an observer
    course.detach(user)
    course.message = "Single observer"
