from unittest import TestCase

from bagfactory import BagFactory, BritishBagFactory


class TestBagFactory(TestCase):

    def testDefaultAttributes(self):
        bag = BagFactory()
        self.assertEqual('turquoise', bag.color)
        self.assertEqual('leather', bag.material)
        self.assertEqual(1, bag.length)
        self.assertEqual(1, bag.width)
        self.assertEqual(1, bag.height)
        self.assertIsInstance(bag.height, int)

    def testNonDefaultColor(self):
        """If we pass a color then the bag should have that color.
        """
        bag = BagFactory(color='gold')
        self.assertEqual('gold', bag.color)

    def testPassedHeightMustBeAnInt(self):
        bag = BagFactory(height='44')
        self.assertEqual(44, bag.height)

    def testVolume(self):
        """If we pass a length, width, and height then the bag's
           volume function should return the right value.
        """
        bag = BagFactory(height=3, width=4, length=6)
        self.assertEqual(72, bag.volume())

    def testVolumeWithStringDimensions(self):
        """If we pass a length, width, and height that are all strings
           then the bag's volume function should return the right value.
        """
        bag = BagFactory(height='3', width='4', length='6')
        self.assertEqual(72, bag.volume())

    def testVolumeWithNonNumericStringHeight(self):
        """If we pass a height that is a non-numeric string then
           we should get a ValueError.
        """
        self.assertRaises(ValueError, BagFactory, height='abc')

    def testVolumeWithNumericStringHeight(self):
        """If we pass a height that is a non-numeric string then
           we should get a ValueError.
        """
        self.assertEqual(33, BagFactory(height='33').height)


class TestBritishBagFactory(TestCase):

    def testNothing(self):
        pass
