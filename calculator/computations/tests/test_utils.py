""" Test utils methods for computations
"""

from datetime import date
from django.test import TestCase

from calculator.computations import utils
from calculator.models import Person


class TestSimplify(TestCase):
    """ Test the simplification of a digit string """

    def test_simplify_zero_single_digit(self):
        """ Zero should simplify as zero """
        zeros = "0"
        self.assertEqual(0, utils.simplify(zeros))

    def test_simplify_zero_multiple_digits(self):
        """ Zero string should simplify as zero """
        zeros = "000000"
        self.assertEqual(0, utils.simplify(zeros))

    def test_simplify_single_digit(self):
        """ Simplification of one digit should return the same digit """
        digit = "3"
        self.assertEqual(3, utils.simplify(digit))

    def test_simplify_multiple_digits(self):
        """ Simplification of a multiple digits string should return the sum of all digits """
        digits = "0123456789"  # Simple sum is 45 [(n²+n)/2]
        self.assertEqual(9, utils.simplify(digits))

    def test_simplify_two_digits_power_kept(self):
        """ Simplification of a power should keep the power by default """
        digits = "11"
        self.assertEqual(11, utils.simplify(digits))

    def test_simplify_multiple_digits_power_kept(self):
        """ Simplification resulting in a power should keep the power by default """
        digits = "886"
        self.assertEqual(22, utils.simplify(digits))

    def test_simplify_two_digits_power_dropped(self):
        """ Simplification of a power can be forced """
        digits = "11"
        self.assertEqual(2, utils.simplify(digits, keep_power=False))

    def test_simplify_multiple_digits_power_dropped(self):
        """ Simplification of a power can be forced """
        digits = "434"
        self.assertEqual(2, utils.simplify(digits, keep_power=False))

    def test_simplify_with_non_digits(self):
        """ Simplification should work even if characters look wrong """
        digits = "12_4 6_ _"
        self.assertEqual(4, utils.simplify(digits))

    def test_simplify_with_non_digits_only_single(self):
        """ Simplification of one non-digit character should return 0 """
        digit = "_"
        self.assertEqual(0, utils.simplify(digit))

    def test_simplify_with_non_digit_only_multiple(self):
        """ Simplification of only non-digit characters should return 0 """
        digit = "__"
        self.assertEqual(0, utils.simplify(digit))


class TestDigitization(TestCase):
    """ Test the transformation of a character string into a digit string """

    def test_digitization_empty_string(self):
        """ Digitization of empty string should return an empty string """
        string = ""
        self.assertEqual("", utils.digitize(string))

    def test_digitization_alpha_string_lower(self):
        """ Digitization of lower alpha string should be transformable into int easily """
        string = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual("12345678912345678912345678", utils.digitize(string))

    def test_digitization_alpha_string_upper(self):
        """ Digitization of upper alpha string should be transformable into int easily """
        string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.assertEqual("12345678912345678912345678", utils.digitize(string))

    def test_digitization_alpha_and_space(self):
        """ Digitization of alpha string with space should result not create interferences """
        string = "a C e G i"
        self.assertEqual("1 3 5 7 9", utils.digitize(string))

    def test_digitization_non_alpha(self):
        """ Digitization of non parsable characters should result in underscores """
        string = "A+&\"'(_"
        self.assertEqual("1______", utils.digitize(string))

    def test_digitization_number(self):
        """ Number should be digitized without any trouble """
        string = "123456789"
        self.assertEqual(string, utils.digitize(string))

    def test_digitization_alphanumeric(self):
        """ Alphanumeric string should be no trouble """
        string = "A2C4E6"
        self.assertEqual("123456", utils.digitize(string))


class TestExamplify(TestCase):
    """ Test the generation of example string from a computation """

    def test_examplify(self):
        """ Examplifying should give the expected format """
        string = "John Doe"
        numbers = "1685 465"
        res = 8
        expected = ["JOHN DOE", "1685 465 → 8"]
        self.assertEqual(expected, utils.examplify(string, numbers, res))

    def test_examplify_with_symbol(self):
        """ Examplifying should be possible with a different symbol """
        string = "John Doe"
        numbers = "1685 465"
        res = 8
        expected = ["JOHN DOE", "1685 465 gives 8"]
        self.assertEqual(expected, utils.examplify(string, numbers, res, "gives"))


class TestCountOccurrences(TestCase):
    """ Test the counting of occurrences of a certain digit in a string """

    def test_count_occurrences_without_explanation(self):
        """ The method should return a single int """
        digits = "1223334444555566666777777788888888999999999"
        self.assertEqual(4, utils.count_occurrences(digits, 4, explain=False))

    def test_count_occurrences_with_explanation(self):
        """ Explanation should be given if asked for """
        digits = "1223334444555566666777777788888888999999999"
        res = utils.count_occurrences(digits, 7, explain=True)
        self.assertTrue(isinstance(res, (tuple, list, set)))
        self.assertEqual(7, res[0])
        self.assertEqual("___________________7777777_________________", res[1])


class TestAbstractBaseComputation(TestCase):
    """ Test the AbstractBaseComputation class """

    @classmethod
    def setUpClass(cls):
        """ Set up attributes used several times """
        super(TestAbstractBaseComputation, cls).setUpClass()
        cls.today = date.today()
        cls.person_pk = "test_examplify"
        cls.person = Person(given_names="John", last_name="Doe", birth=cls.today, pk=cls.person_pk)
        cls.clazz = utils.AbstractBaseComputation(cls.person)

    def test_abstract_base_computation_attributes_are_set(self):
        """ The abstract class should get the person parameters """
        self.assertEqual(self.person.given_names, self.clazz.given_names)
        self.assertEqual(self.person.last_name, self.clazz.last_name)
        self.assertEqual(self.person.birth, self.clazz.birth)
        self.assertEqual(self.person.gender, self.clazz.gender)

    def test_abstract_base_computation_run_is_not_implemented(self):
        """ This abstract class should not implement the run method """
        with self.assertRaises(NotImplementedError):
            self.clazz.run()
