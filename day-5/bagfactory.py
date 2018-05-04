class BagFactory():
    """This is a factory that produces bags, preferably turquoise.

    Founded in Australia, with subsidiary operations in the UK.

    @param color: A C{str} giving the color.
    @raises ValueError: if C{height} is not an integer.
    """

    def __init__(self, color='turquoise', material='leather',
                 length=1, width=1, height=1):
        self.color = color
        self.material = material
        self.length = int(length)
        self.width = int(width)
        self.height = int(height)

    def dumbVolume(self):
        """Return the volume of a bag, with an unusual
        multiplication method.

        This is just the length * width * height.
        """
        count = 0
        inc = 0.5
        for i in range(self.length):
            for j in range(self.width):
                for k in range(self.height):
                    count += inc
        return 2 * count

    def volume(self):
        """Return the volume of a bag.

        This is just the length * width * height.
        """
        return self.length * self.width * self.height

    def __len__(self):
        return self.length

    def __str__(self):
        return 'I am a %s bag of length %d' % (self.color, self.length)

    def __gt__(self, otherBag):
        return self.volume() > otherBag.volume()


class BritishBagFactory(BagFactory):

    def __init__(self, material='leather', length=1, width=1, height=1):
        BagFactory.__init__(self, material=material, color='green',
                            length=length, width=width, height=height)

    def __len__(self):
        return int(self.length / 2.54)

    def bulletproof(self):
        return False
