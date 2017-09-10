""" Test abstract grid class
"""

from datetime import date
from django.test import TestCase

from calculator.computations.grid_computation import AbstractGridComputation
from calculator.models import Person


class TestAbstractGridComputation(TestCase):
    """ Test the AbstractGridComputation class """

    @classmethod
    def setUpClass(cls):
        """ Set up attributes used several times """
        super(TestAbstractGridComputation, cls).setUpClass()
        cls.today = date.today()
        cls.person_pk = "test_abstract_grid"
        cls.person = Person(
            given_names="John",
            last_name="Doe",
            birth=cls.today,
            pk=cls.person_pk
        )
        cls.clazz = AbstractGridComputation(cls.person)

    def test_abstract_grid_computation_generates_correct_grid(self):
        """ The grid generated should be correct """
        expected_counts = [1, 0, 0, 1, 2, 2, 0, 1, 0]
        for i, cell in self.clazz.grid.items():
            self.assertEqual(expected_counts[i-1], cell['count'])

    def test_abstract_grid_computation_uses_cache(self):
        """ Using the same pk for Person but different values
        should return same (but wrong) result
        """
        person = Person(
            given_names="Cirilla Fiona Ellen",
            last_name="Riannon",
            birth=self.today,
            pk=self.person_pk
        )  # Results will obviously differ from John Doe
        expected = AbstractGridComputation(person)
        self.assertDictEqual(expected.grid, self.clazz.grid)

    def test_abstract_grid_computation_run_is_not_directly_possible(self):
        """ It should not be possible to directly run this abstract class """
        with self.assertRaises(ValueError):
            self.clazz.run()