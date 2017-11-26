#   This file is part of Newmerology.
#
#   Newmerology is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published
#   by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Newmerology is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with Newmerology.  If not, see <https://www.gnu.org/licenses/agpl.html>.

""" Test abstract time computations
"""

from datetime import date
from django.test import TestCase

from calculator.computations.time_computation import (AbstractActionComputation,
                                                      AbstractCycleComputation,
                                                      AbstractTimeComputation,
                                                      create_period)
from calculator.models import Person


class TestAbstractTimeComputation(TestCase):
    """ Test the AbstractTimeComputation class """

    @classmethod
    def setUpClass(cls):
        """ Set up attributes used several times """
        super(TestAbstractTimeComputation, cls).setUpClass()
        cls.today = date.today()
        cls.person_pk = "test_abstract_time"
        cls.person = Person(
            given_names="John",
            last_name="Doe",
            birth=cls.today,
            pk=cls.person_pk
        )
        cls.clazz = AbstractTimeComputation(cls.person)

    def test_abstract_time_computation_run_raises_value_error(self):
        """ The run should raise a ValueError since it's an abstract class """
        with self.assertRaises(ValueError):
            self.clazz.run()

    def test_abstract_time_computation_generate_periods_is_not_implemented(self):
        """ This abstract class should not implement the period generation """
        with self.assertRaises(NotImplementedError):
            self.clazz.generate_periods()

    def test_create_period(self):
        """ The period creation helper method should return an appropriate dict """
        self.assertDictEqual({'start': 0, 'content': 'some_content', 'example': 'some_example'},
                             create_period(0, 'some_content', 'some_example'))


class TestAbstractActionComputation(TestCase):

    @classmethod
    def setUpClass(cls):
        """ Set up attributes used several times """
        super(TestAbstractActionComputation, cls).setUpClass()
        cls.birth = date(2010, 3, 21)
        cls.person_pk = "test_abstract_action"
        cls.person = Person(
            given_names="John",
            last_name="Doe",
            birth=cls.birth,
            pk=cls.person_pk
        )
        cls.clazz = AbstractActionComputation(cls.person)

    def test_abstract_action_period_generation(self):
        """ The actions and periods should correspond to the expectations """
        expected_start = [0, 27, 36, 45]
        expected_content = [6, 6, 3, 6]

        actual_start = [x['start'] for x in self.clazz.periods]
        actual_content = [x['content'] for x in self.clazz.periods]
        self.assertListEqual(expected_start, actual_start)
        self.assertListEqual(expected_content, actual_content)

    def test_abstract_action_uses_cache(self):
        """ The periods should use cache """
        periods_pre_change = self.clazz.periods
        self.clazz.birth = date.today()
        self.assertEqual(periods_pre_change, self.clazz.periods)


class TestAbstractCycleComputation(TestCase):

    @classmethod
    def setUpClass(cls):
        """ Set up attributes used several times """
        super(TestAbstractCycleComputation, cls).setUpClass()
        cls.birth = date(2010, 3, 21)
        cls.person_pk = "test_abstract_cycle"
        cls.person = Person(
            given_names="John",
            last_name="Doe",
            birth=cls.birth,
            pk=cls.person_pk
        )
        cls.clazz = AbstractCycleComputation(cls.person)

    def test_abstract_cycle_period_generation(self):
        """ The cycles and periods should correspond to the expectations """
        expected_start = [0, 28, 56]
        expected_content = [3, 3, 3]

        actual_start = [x['start'] for x in self.clazz.periods]
        actual_content = [x['content'] for x in self.clazz.periods]
        self.assertListEqual(expected_start, actual_start)
        self.assertListEqual(expected_content, actual_content)

    def test_abstract_cycle_uses_cache(self):
        """ The periods should use cache """
        periods_pre_change = self.clazz.periods
        self.clazz.birth = date.today()
        self.assertEqual(periods_pre_change, self.clazz.periods)
