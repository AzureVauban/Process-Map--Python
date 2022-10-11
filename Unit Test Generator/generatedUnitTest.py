"""AUTO GENERATED UNIT TEST
"""
import unittest

from main import Node, reversearithmetic

morphite: Node = Node('morphite', None, 0, 1, 1)
protocite: Node = Node('protocite', morphite, 0, 1, 1)
irradium: Node = Node('irradium', morphite, 0, 1, 1)
phase_matter: Node = Node('phase matter', morphite, 0, 1, 1)
sulphuric_acid: Node = Node('sulphuric acid', morphite, 0, 1, 5)
reversearithmetic(morphite);

class MORPHITE_unittest(unittest.TestCase): # pylint:disable=C0103
	"""tentative test class, add additional comments here:
	"""

	def test_morphite(self):# pylint:disable=C0103
		"""assert that morphite is equal to 999
		"""

		self.assertEqual(morphite.amountonhand,999)

	def test_protocite(self):# pylint:disable=C0103
		"""assert that protocite is equal to 999
		"""

		self.assertEqual(protocite.amountonhand,999)

	def test_irradium(self):# pylint:disable=C0103
		"""assert that irradium is equal to 999
		"""

		self.assertEqual(irradium.amountonhand,999)

	def test_phase_matter(self):# pylint:disable=C0103
		"""assert that phase matter is equal to 999
		"""

		self.assertEqual(phase_matter.amountonhand,999)

	def test_sulphuric_acid(self):# pylint:disable=C0103
		"""assert that sulphuric acid is equal to 4995
		"""

		self.assertEqual(sulphuric_acid.amountonhand,4995)


