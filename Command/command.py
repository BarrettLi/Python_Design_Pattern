# -*- coding: utf-8 -*-

import abc


class VmReceiver(object):
    # command receiver where commands are executed

    def start(self):
        print("Virtual machine start")

    def stop(self):
        print("Virtual machine stop")


class Command(object):
    # command abstract class
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self):
        pass


class StartVmCommand(Command):
    
    def __init__(self, recevier):
        self.recevier = recevier

    def execute(self):
        self.recevier.start()


class StopVmCommand(Command):
    
    def __init__(self, recevier):
        self.recevier = recevier

    def execute(self):
        self.recevier.stop()


class ClientInvoker(object):
    # command invoker
    def __init__(self, command):
        self.command = command

    def do(self):
        self.command.execute()


if __name__ == '__main__':
    recevier = VmReceiver()
    start_command = StartVmCommand(recevier)

    client = ClientInvoker(start_command)
    client.do()

    stop_command = StopVmCommand(recevier)
    client.command = stop_command
    client.do()
