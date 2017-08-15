# -*- coding: utf-8 -*-

import abc


class AbsShow(object):
    
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def show(self):
        pass


class AdminShow(AbsShow):
    # admin show
    def show(self):
        return "show with admin"


class UserShow(AbsShow):
    # user show
    def show(self):
        return "show with user"


class Question(object):
    # question object, after applying strategy pattern

    def __init__(self, show_obj):
        self.show_obj = show_obj

    def show(self):
        return self.show_obj.show()



if __name__ == '__main__':
    q = Question(show_obj=AdminShow())
    print(q.show())
    # replace the previous object
    q.show_obj = UserShow()
    print(q.show())
