# -*- coding: utf-8 -*-

class Question(object):
    # Question object, before applying strategy pattern
    def __init__(self, admin=True):
        self._admin = admin
        
    def show(self):
        # display different information depending on if admin or not
        if self._admin is True:
            return "show page with admin"
        else:
            return "show page with user"


if __name__ == "__main__":
    q = Question(admin=False)
    print(q.show())
