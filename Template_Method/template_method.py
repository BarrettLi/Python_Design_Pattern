# -*- coding: utf-8 -*-

import abc


class Fishing(object):
    
    __metaclass__ = abc.ABCMeta
    
    def finishing(self):
        self.prepare_bait()
        self.go_to_riverbank()
        self.find_location()
        print("start fishing")

    @abc.abstractmethod
    def prepare_bait(self):
        pass

    @abc.abstractmethod
    def go_to_riverbank(self):
        pass

    @abc.abstractmethod
    def find_location(self):
        pass


class JohnFishing(Fishing):
    
    def prepare_bait(self):
        # John buys bait from Walmart
        print("John: by bait from Walmart")

    def go_to_riverbank(self):
        # go fishing by car
        print("John: to river by driving")

    def find_location(self):
        # select location on the island
        print("John: select location on the island")


class SimonFishing(Fishing):
    
    def prepare_bait(self):
        # buy bait from Amazon
        print("Simon: buy bait from Amazon")

    def go_to_riverbank(self):
        # go fishing by bike
        print("Simon: to river by biking")

    def find_location(self):
        # select location on the riverbank
        print("Simon: select location on the riverbank")


if __name__ == '__main__':
    # John goes fishing
    f = JohnFishing()
    f.finishing()

    # Simon goes fishing
    f = SimonFishing()
    f.finishing()
