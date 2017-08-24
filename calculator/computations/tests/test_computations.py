""" Test computations methods
"""

from datetime import date
from django.test import TestCase
from calculator.models import Person
from calculator.computations import (
    active,
    cell_1,
    cell_2,
    cell_3,
    cell_4,
    cell_5,
    cell_6,
    cell_7,
    cell_8,
    cell_9,
    expression,
    heredity,
    intimate,
    lifepath,
    psychic,
    spiritual,
)


class AbstractTestMethod(TestCase):

    computation_class = None

    def __init__(self, *args, **kwargs):
        super(AbstractTestMethod, self).__init__(*args, **kwargs)
        self.person_pk = "test_computations"
        self.person = Person(
            given_names="John Maximilien",
            last_name="Doe-Smith",
            birth=date(1984, 11, 21),
            pk=self.person_pk
        )
        self.method = self.computation_class(self.person)


class TestLifePath(AbstractTestMethod):

    computation_class = lifepath.Computation

    def setUp(self):
        self.expected_result = 9

    def test_result_lifepath(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_lifepath(self):
        """ The example should respect a certain format """
        self.assertEqual([
            '1984-11-21',
            '1984+11+21 → ' + str(self.expected_result)
        ], self.method.example)


class TestActive(AbstractTestMethod):

    computation_class = active.Computation

    def setUp(self):
        self.expected_result = 3

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

    def setUp(self):
        self.expected_result = 6
        self.expected_example = [
            'DOE-SMITH JOHN MAXIMILIEN',
            '465 14928 1685 4169493955 → ' + str(self.expected_result)
        ]

    def test_result_expression(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_expression(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestHeredity(AbstractTestMethod):

    computation_class = heredity.Computation

    def setUp(self):
        self.expected_result = 3
        self.expected_example = [
            'DOE-SMITH',
            '465 14928 → ' + str(self.expected_result)
        ]

    def test_result_heredity(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_heredity(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestIntimate(AbstractTestMethod):

    computation_class = intimate.Computation

    def setUp(self):
        self.expected_result = 1
        self.expected_example = [
            'D__-SM_TH J_HN M_X_M_L__N',
            '4__ 14_28 1_85 4_6_4_3__5 → ' + str(self.expected_result)
        ]

    def test_result_intimate(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_intimate(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)
        self.assertEqual(self.expected_example, self.method.example)


class TestPsychic(AbstractTestMethod):

    computation_class = psychic.Computation

    def setUp(self):
        self.expected_result = 3
        self.expected_example = [
            '1984-11-21',
            '21 → ' + str(self.expected_result)
        ]

    def test_result_spiritual(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_spiritual(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestSpiritual(AbstractTestMethod):

    computation_class = spiritual.Computation

    def setUp(self):
        self.expected_result = 5
        self.expected_example = [
            '_OE-__I__ _O__ _A_I_I_IE_',
            '_65 __9__ _6__ _1_9_9_95_ → ' + str(self.expected_result)
        ]

    def test_result_spiritual(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_spiritual(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestCell1(AbstractTestMethod):

    computation_class = cell_1.Computation

    def setUp(self):
        self.expected_result = 3
        self.expected_example = [
            'DOE-SMITH JOHN MAXIMILIEN',
            '____1_____1_____1________ → ' + str(self.expected_result)
        ]

    def test_result_cell_1(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_cell_1(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestCell2(AbstractTestMethod):

    computation_class = cell_2.Computation

    def setUp(self):
        self.expected_result = 1
        self.expected_example = [
            'DOE-SMITH JOHN MAXIMILIEN',
            '_______2_________________ → ' + str(self.expected_result)
        ]

    def test_result_cell_2(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_cell_2(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestCell3(AbstractTestMethod):

    computation_class = cell_3.Computation

    def setUp(self):
        self.expected_result = 1
        self.expected_example = [
            'DOE-SMITH JOHN MAXIMILIEN',
            '_____________________3___ → ' + str(self.expected_result)
        ]

    def test_result_cell_3(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_cell_3(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestCell4(AbstractTestMethod):

    computation_class = cell_4.Computation

    def setUp(self):
        self.expected_result = 4
        self.expected_example = [
            'DOE-SMITH JOHN MAXIMILIEN',
            '4____4_________4___4_____ → ' + str(self.expected_result)
        ]

    def test_result_cell_4(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_cell_4(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestCell5(AbstractTestMethod):

    computation_class = cell_5.Computation

    def setUp(self):
        self.expected_result = 4
        self.expected_example = [
            'DOE-SMITH JOHN MAXIMILIEN',
            '__5__________5_________55 → ' + str(self.expected_result)
        ]

    def test_result_cell_5(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_cell_5(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestCell6(AbstractTestMethod):

    computation_class = cell_6.Computation

    def setUp(self):
        self.expected_result = 3
        self.expected_example = [
            'DOE-SMITH JOHN MAXIMILIEN',
            '_6_________6_____6_______ → ' + str(self.expected_result)
        ]

    def test_result_cell_6(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_cell_6(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestCell7(AbstractTestMethod):

    computation_class = cell_7.Computation

    def setUp(self):
        self.expected_result = 0
        self.expected_example = [
            'DOE-SMITH JOHN MAXIMILIEN',
            '_________________________ → ' + str(self.expected_result)
        ]

    def test_result_cell_7(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_cell_7(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestCell8(AbstractTestMethod):

    computation_class = cell_8.Computation

    def setUp(self):
        self.expected_result = 2
        self.expected_example = [
            'DOE-SMITH JOHN MAXIMILIEN',
            '________8___8____________ → ' + str(self.expected_result)
        ]

    def test_result_cell_8(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_cell_8(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)


class TestCell9(AbstractTestMethod):

    computation_class = cell_9.Computation

    def setUp(self):
        self.expected_result = 4
        self.expected_example = [
            'DOE-SMITH JOHN MAXIMILIEN',
            '______9___________9_9_9__ → ' + str(self.expected_result)
        ]

    def test_result_cell_9(self):
        """ The result should be the one expected """
        self.assertEqual(self.expected_result, self.method.result)

    def test_example_cell_9(self):
        """ The example should respect a certain format """
        self.assertEqual(self.expected_example, self.method.example)
