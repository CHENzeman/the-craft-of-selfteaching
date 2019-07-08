#!/bin/usr/env python3

class Fruit:
    name = 'Fruitas'

    @classmethod
    def printName(cls):
        print('The name is:', cls.name)

apple = Fruit()
berry = Fruit()

Fruit.printName()
apple.printName()
berry.printName()

apple.name="Apple"  #改object的name，不会改变method
Fruit.printName()
apple.printName()
berry.printName()

Fruit.name="Apple" #改class的name，会改变method
Fruit.printName()
apple.printName()
berry.printName()