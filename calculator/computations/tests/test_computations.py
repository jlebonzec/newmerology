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

""" Test computations methods
"""

from datetime import date
from django.test import TestCase
from django_translate.services import tranz as _

from calculator.models import Person
from calculator.computations import (
    active,
    action_1,
    action_2,
    action_3,
    action_4,
    cell_1,
    cell_2,
    cell_3,
    cell_4,
    cell_5,
    cell_6,
    cell_7,
    cell_8,
    cell_9,
    cycle_1,
    cycle_2,
    cycle_3,
    expression,
    heredity,
    intimate,
    lifepath,
    personal_year,
    personal_year_next,
    psychic,
    spiritual,
)


class AbstractTestMethod(TestCase):

    computation_class = None
    expected_result = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.person_pk = "test_computations"
        cls.person = Person(
            given_names="John Maximilien",
            last_name="Doe-Smith",
            birth=date(1984, 11, 21),
            pk=cls.person_pk
        )
        cls.method = cls.computation_class(cls.person)


class TestLifePathPower(AbstractTestMethod):
    """ Same as Life Path, but the result is a power """

    computation_class = lifepath.Computation

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.person_pk = "test_computation_lifepath_power"
        cls.person = Person(
            given_names="John Maximilien",
            last_name="Doe-Smith",
            birth=date(1974, 7, 28),
            pk=cls.person_pk
        )
        cls.method = cls.computation_class(cls.person)
        cls.expected_result = 11

    def test_coherence_result(self):
        """ Asking for a result twice should yield the same data """
        self.assertEqual(self.method.result, self.method.result)

    def test_coherence_example(self):
        """ Asking for an example twice should yield the same data """
        self.assertEqual(self.method.example, self.method.example)

    def test_result_lifepath(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_lifepath(self):
        """ The example should respect a certain format """
        self.assertEqual([
            ' + '.join([_('g.year').upper(), _('g.month').upper(), _('g.day').upper()]),
            '1974 + 07 + 28 → ' + str(self.expected_result)
        ], self.method.example)


class TestLifePath(AbstractTestMethod):

    computation_class = lifepath.Computation

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.expected_result = 9

    def test_result_lifepath(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_lifepath(self):
        """ The example should respect a certain format """
        self.assertEqual([
            ' + '.join([_('g.year').upper(), _('g.month').upper(), _('g.day').upper()]),
            '1984 + 11 + 21 → ' + str(self.expected_result)
        ], self.method.example)


class TestActive(AbstractTestMethod):

    computation_class = active.Computation

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.expected_result = 3

    def test_result_active(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_active(self):
        """ The example should respect a certain format """
        self.assertEqual([
            'JOHN MAXIMILIEN',
            '1685 4169493955 → ' + str(self.expected_result)
        ], self.method.example)


class TestExpression(AbstractTestMethod):

    computation_class = expression.Computation

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.expected_result = 6
        cls.expected_example = [
            'DOE-SMITH JOHN MAXIMILIEN',
            '465 14928 1685 4169493955 → ' + str(cls.expected_result)
        ]

    def test_result_expression(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_expression(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestHeredity(AbstractTestMethod):

    computation_class = heredity.Computation

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.expected_result = 3
        cls.expected_example = [
            'DOE-SMITH',
            '465 14928 → ' + str(cls.expected_result)
        ]

    def test_result_heredity(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_heredity(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestIntimate(AbstractTestMethod):

    computation_class = intimate.Computation

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.expected_result = 1
        cls.expected_example = [
            'D__-SM_TH J_HN M_X_M_L__N',
            '4__ 14_28 1_85 4_6_4_3__5 → ' + str(cls.expected_result)
        ]

    def test_result_intimate(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_intimate(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestPsychic(AbstractTestMethod):

    computation_class = psychic.Computation

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.expected_result = 21
        cls.expected_example = [
            '1984-11-21',
            '21 → ' + str(cls.expected_result)
        ]

    def test_result_spiritual(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_spiritual(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestSpiritual(AbstractTestMethod):

    computation_class = spiritual.Computation

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.expected_result = 5
        cls.expected_example = [
            '_OE-__I__ _O__ _A_I_I_IE_',
            '_65 __9__ _6__ _1_9_9_95_ → ' + str(cls.expected_result)
        ]

    def test_result_spiritual(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_spiritual(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestPersonalYear(AbstractTestMethod):

    computation_class = personal_year.Computation

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.method.today = date(2013, 4, 25)
        cls.expected_result = 2
        cls.expected_example = [
            ' + '.join([_('g.u_year').upper(), _('g.month').upper(), _('g.day').upper()]),
            '2013 + 11 + 21 → ' + str(cls.expected_result)
        ]

    def test_result_spiritual(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_spiritual(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestPersonalYearNext(AbstractTestMethod):

    computation_class = personal_year_next.Computation

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.method.today = date(2013, 4, 25)
        cls.expected_result = 3
        cls.expected_example = [
            ' + '.join([_('g.u_year').upper(), _('g.month').upper(), _('g.day').upper()]),
            '2014 + 11 + 21 → ' + str(cls.expected_result)
        ]

    def test_result_spiritual(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_spiritual(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestCell1(AbstractTestMethod):

    computation_class = cell_1.Computation

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.expected_result = 3
        cls.expected_example = [
            'DOE-SMITH JOHN MAXIMILIEN',
            '____1_____1_____1________ → ' + str(cls.expected_result)
        ]

    def test_result_cell_1(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_cell_1(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestCell2(AbstractTestMethod):

    computation_class = cell_2.Computation

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.expected_result = 1
        cls.expected_example = [
            'DOE-SMITH JOHN MAXIMILIEN',
            '_______2_________________ → ' + str(cls.expected_result)
        ]

    def test_result_cell_2(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_cell_2(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestCell3(AbstractTestMethod):

    computation_class = cell_3.Computation

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.expected_result = 1
        cls.expected_example = [
            'DOE-SMITH JOHN MAXIMILIEN',
            '_____________________3___ → ' + str(cls.expected_result)
        ]

    def test_result_cell_3(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_cell_3(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestCell4(AbstractTestMethod):

    computation_class = cell_4.Computation

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.expected_result = 4
        cls.expected_example = [
            'DOE-SMITH JOHN MAXIMILIEN',
            '4____4_________4___4_____ → ' + str(cls.expected_result)
        ]

    def test_result_cell_4(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_cell_4(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestCell5(AbstractTestMethod):

    computation_class = cell_5.Computation

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.expected_result = 4
        cls.expected_example = [
            'DOE-SMITH JOHN MAXIMILIEN',
            '__5__________5_________55 → ' + str(cls.expected_result)
        ]

    def test_result_cell_5(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_cell_5(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestCell6(AbstractTestMethod):

    computation_class = cell_6.Computation

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.expected_result = 3
        cls.expected_example = [
            'DOE-SMITH JOHN MAXIMILIEN',
            '_6_________6_____6_______ → ' + str(cls.expected_result)
        ]

    def test_result_cell_6(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_cell_6(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestCell7(AbstractTestMethod):

    computation_class = cell_7.Computation

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.expected_result = 0
        cls.expected_example = [
            'DOE-SMITH JOHN MAXIMILIEN',
            '_________________________ → ' + str(cls.expected_result)
        ]

    def test_result_cell_7(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_cell_7(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestCell8(AbstractTestMethod):

    computation_class = cell_8.Computation

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.expected_result = 2
        cls.expected_example = [
            'DOE-SMITH JOHN MAXIMILIEN',
            '________8___8____________ → ' + str(cls.expected_result)
        ]

    def test_result_cell_8(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_cell_8(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestCell9(AbstractTestMethod):

    computation_class = cell_9.Computation

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.expected_result = 4
        cls.expected_example = [
            'DOE-SMITH JOHN MAXIMILIEN',
            '______9___________9_9_9__ → ' + str(cls.expected_result)
        ]

    def test_result_cell_9(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_cell_9(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestAction1(AbstractTestMethod):

    computation_class = action_1.Computation

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.expected_result = 5
        cls.expected_example = [
            ' + '.join([_('g.month').upper(), _('g.day').upper()]),
            '11 + 21 → ' + str(cls.expected_result)
        ]

    def test_result_action_1(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_action_1(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestAction2(AbstractTestMethod):

    computation_class = action_2.Computation

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.expected_result = 7
        cls.expected_example = [
            ' + '.join([_('g.year').upper(), _('g.day').upper()]),
            '1984 + 21 → ' + str(cls.expected_result)
        ]

    def test_result_action_2(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_action_2(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestAction3(AbstractTestMethod):

    computation_class = action_3.Computation

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.expected_result = 3
        cls.expected_example = [
            ' + '.join([_('g.action_1').upper(), _('g.action_2').upper()]),
            '5 + 7 → ' + str(cls.expected_result)
        ]

    def test_result_action_3(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_action_3(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestAction4(AbstractTestMethod):

    computation_class = action_4.Computation

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.expected_result = 6
        cls.expected_example = [
            ' + '.join([_('g.year').upper(), _('g.month').upper()]),
            '1984 + 11 → ' + str(cls.expected_result)
        ]

    def test_result_action_4(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_action_4(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestCycle1(AbstractTestMethod):

    computation_class = cycle_1.Computation

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.expected_result = 11
        cls.expected_example = [
            _('g.month').upper(),
            '11 → ' + str(cls.expected_result)
        ]

    def test_result_cycle_1(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_cycle_1(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestCycle2(AbstractTestMethod):

    computation_class = cycle_2.Computation

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.expected_result = 3
        cls.expected_example = [
            _('g.day').upper(),
            '21 → ' + str(cls.expected_result)
        ]

    def test_result_cycle_2(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_cycle_2(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestCycle3(AbstractTestMethod):

    computation_class = cycle_3.Computation

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.expected_result = 22
        cls.expected_example = [
            _('g.year').upper(),
            '1984 → ' + str(cls.expected_result)
        ]

    def test_result_cycle_3(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_cycle_3(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)
