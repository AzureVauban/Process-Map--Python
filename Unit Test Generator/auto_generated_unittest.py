"""AUTO GENERATED UNIT TEST
"""
import unittest

from main import Node, reversearithmetic

pooop: Node = Node('pooop', None, 0, 1, 1)
pixels: Node = Node('pixels', pooop, 0, 45, 4)
sad: Node = Node('sad', pixels, 0, 4, 4)
pixels2: Node = Node('pixels2', sad, 0, 3, 4)
pixels3: Node = Node('pixels3', sad, 0, 3, 3)
adadas: Node = Node('adadas', pixels, 0, 4, 4)
fdasfds: Node = Node('fdasfds', pixels, 0, 4, 4)
dad: Node = Node('dad', pooop, 0, 45, 43)
asda: Node = Node('asda', pooop, 0, 45, 43)
asdasd: Node = Node('asdasd', pooop, 0, 45, 43)
reversearithmetic(pooop, 5)


class POOOP_unittest(unittest.TestCase):  # pylint:disable=C0103
    """tentative test class, add additional comments here:
    """

    def test_pooop(self):  # pylint:disable=C0103
        """assert that pooop is equal to 5
        """

        self.assertEqual(pooop.amountonhand, 5)

    def test_pixels(self):  # pylint:disable=C0103
        """assert that pixels is equal to 0
        """

        self.assertEqual(pixels.amountonhand, 0)

    def test_sad(self):  # pylint:disable=C0103
        """assert that sad is equal to 0
        """

        self.assertEqual(sad.amountonhand, 0)

    def test_pixels2(self):  # pylint:disable=C0103
        """assert that pixels2 is equal to 0
        """

        self.assertEqual(pixels2.amountonhand, 0)

    def test_pixels3(self):  # pylint:disable=C0103
        """assert that pixels3 is equal to 0
        """

        self.assertEqual(pixels3.amountonhand, 0)

    def test_adadas(self):  # pylint:disable=C0103
        """assert that adadas is equal to 0
        """

        self.assertEqual(adadas.amountonhand, 0)

    def test_fdasfds(self):  # pylint:disable=C0103
        """assert that fdasfds is equal to 0
        """

        self.assertEqual(fdasfds.amountonhand, 0)

    def test_dad(self):  # pylint:disable=C0103
        """assert that dad is equal to 4
        """

        self.assertEqual(dad.amountonhand, 4)

    def test_asda(self):  # pylint:disable=C0103
        """assert that asda is equal to 4
        """

        self.assertEqual(asda.amountonhand, 4)

    def test_asdasd(self):  # pylint:disable=C0103
        """assert that asdasd is equal to 4
        """

        self.assertEqual(asdasd.amountonhand, 4)
