# -*- coding: utf-8 -*-

class OldCourse(object):
    # old course
    
    def show(self):
        # display course information
        print("show description")
        print("show teacher of course")
        print("show labs")


class Page(object):
    
    def __init__(self, course):
        self.course = course

    def render(self):
        self.course.show()


class NewCourse(object):
    
    def show_desc(self):
        # show description information
        print("show description")
    
    def show_teacher(self):
        # show teacher's information
        print("show teacher of course")

    def show_labs(self):
        # show labs
        print("show labs")


class Adapter(object):
    
    def __init__(self, course):
        self.course = course

    def show(self):
        self.course.show_desc()
        self.course.show_teacher()
        self.course.show_labs()


if __name__ == '__main__':
    old_course = OldCourse()
    page = Page(old_course)
    page.render()
    print("")
    new_course = NewCourse()
    # there is no show method in NewCourse
    adapter = Adapter(new_course)
    page = Page(adapter)
    page.render()
