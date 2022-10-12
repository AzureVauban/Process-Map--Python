"""AUTO GENERATED UNIT TEST
"""
import unittest

from main import Node, reversearithmetic

morphite: Node = Node('morphite', None, 0, 1, 1)
yt: Node = Node('yt', morphite, 0, 43, 6)
fgd: Node = Node('fgd', morphite, 0, 43, 7)
reversearithmetic(morphite, 7)


class MORPHITE_unittest(unittest.TestCase):  # pylint:disable=C0103
    """tentative test class, add additional comments here:
    """

    def test_morphite(self):  # pylint:disable=C0103
        """assert that morphite is equal to 7
        """

        self.assertEqual(morphite.amountonhand, 7)

    def test_yt(self):  # pylint:disable=C0103
        """assert that yt is equal to 0
        """

        self.assertEqual(yt.amountonhand, 0)

    def test_fgd(self):  # pylint:disable=C0103
        """assert that fgd is equal to 1
        """

        self.assertEqual(fgd.amountonhand, 1)
