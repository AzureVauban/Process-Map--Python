"""AUTO GENERATED UNIT TEST
"""
import unittest

from main import Node, reversearithmetic

ooga_booga: Node = Node('ooga booga', None, 0, 1, 1)
uio: Node = Node('uio', ooga_booga, 0, 8, 7)
hj: Node = Node('hj', ooga_booga, 0, 8, 8)
ll: Node = Node('ll', ooga_booga, 0, 8, 9)
reversearithmetic(ooga_booga, 768)


class OOGABOOGAA_unittest(unittest.TestCase):  # pylint:disable=C0103
    """tentative test class, add additional comments here:
    """

    def test_ooga_booga(self):  # pylint:disable=C0103
        """assert that ooga booga is equal to 768
        """

        self.assertEqual(ooga_booga.amountonhand, 768)

    def test_uio(self):  # pylint:disable=C0103
        """assert that uio is equal to 672
        """

        self.assertEqual(uio.amountonhand, 672)

    def test_hj(self):  # pylint:disable=C0103
        """assert that hj is equal to 768
        """

        self.assertEqual(hj.amountonhand, 768)

    def test_ll(self):  # pylint:disable=C0103
        """assert that ll is equal to 864
        """

        self.assertEqual(ll.amountonhand, 864)
