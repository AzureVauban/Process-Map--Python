"""AUTO GENERATED UNIT TEST
"""
import unittest

from main import Node, reversearithmetic

morphite: Node = Node('morphite', None, 0, 1, 1)
protocite: Node = Node('protocite', morphite, 0, 1, 6)
irradium: Node = Node('irradium', morphite, 0, 1, 8)
reversearithmetic(morphite, 5)


class MORPHITE_unittest(unittest.TestCase): # pylint:disable=C0103
	"""tentative test class, add additional comments here:
	"""

	def test_morphite(self):# pylint:disable=C0103
		"""assert that morphite is equal to 5
		"""

		self.assertEqual(morphite.amountonhand,5)

	def test_protocite(self):# pylint:disable=C0103
		"""assert that protocite is equal to 30
		"""

		self.assertEqual(protocite.amountonhand,30)

	def test_irradium(self):# pylint:disable=C0103
		"""assert that irradium is equal to 40
		"""

		self.assertEqual(irradium.amountonhand,40)


