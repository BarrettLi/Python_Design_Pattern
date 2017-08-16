# -*- coding: utf-8 -*-

from time import sleep

class Redis(object):
    # simulate redis service
    def __init__(self):
        # use dict to store data
        self.cache = dict()
        
    def get(self, key):
        # get data
        return self.cache.get(key)

    def set(self, key, value):
        # set data
        self.cache[key] = value

class Image(object):
    
    def __init__(self, name):
        self.name = name

    @property
    def url(self):
        sleep(2)
        return "https://dn-syl-static.qbox.me/img/logo-transparent.png"

class Page(object):
    # display image
    def __init__(self, image):
        # initialize image
        self.image = image
    
    def render(self):
        # display image
        print(self.image.url)

redis = Redis()

class ImageProxy(object):
    
    def __init__(self, image):
        self.image = image

    @property
    def url(self):
        addr = redis.get(self.image.name)
        if not addr:
            addr = self.image.url
            print("Set url in redis cache!")
            redis.set(self.image.name, addr)
        else:
            print("Get url from redis cache!")
        return addr


if __name__ == '__main__':
    img = Image(name="logo")
    proxy = ImageProxy(img)
    page = Page(proxy)

    page.render()
    print("")

    page.render()
