#!/usr/bin/env python3

from bagfactory import BagFactory, BritishBagFactory


bag1 = BagFactory()

print('Bag 1 is', bag1.color)

bag2 = BagFactory('green', material='lyric', height=2, length=10)

print('Bag 2 is', bag2.color)
print('Bag 2 is make of', bag2.material)
print('Bag 2 has a volume of', bag2.volume())
print('Bag 2 has a length of', len(bag2))

bbag = BritishBagFactory(material='lyric', height=2, length=10)
print('The British bag has a length of', len(bbag))

print('The British bag is bulletproof:', bbag.bulletproof())

bbag.length = 254
print('The British bag has a length of', len(bbag))

if bag1 > bag2:
    print('Bag 1 is biggest')
else:
    print('Bag 2 is biggest')

print(bag1)
