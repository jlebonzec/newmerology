""" Contains the AbstractMethod that any other computation should inherit and implement run()
"""
from calculator.config import CONVERSION, POWERS

import datetime


class AbstractMethod(object):
    """ AbstractMethod. Every other method should inherit from this one, implementing run()

    :type first_name: str
    :type middle_names: list
    :type last_name: str
    :type birth: datetime.date
    :type gender: str
    """

    def __init__(self, first_name, middle_names, last_name, birth, gender):
        self.first_name = first_name
        self.middle_names = middle_names
        self.last_name = last_name
        self.birth = birth
        self.gender = gender
        self.today = datetime.date.today()

        # Not computed yet variables
        self._has_run = False
        self._result = None
        self._example = []

    @property
    def result(self):
        """ Obtain the result of the computation. Computes it if not yet calculated.
        """
        if not self._has_run:
            self.run()
        return self._result

    @property
    def example(self):
        """ Obtain an example string based on the given content. Computes it if not yet calculated.

        This has for objective to explain how the calculation is done
        """
        if not self._has_run:
            self.run()
        return self._example

    def run(self):
        """ Run the method to compute the result.

        It doesn't have to return anything, but shall always fill the `self._result` variable.
        It is preferable, though not mandatory, to also fill the `self._example` variable.

        This is the core method that needs to be implemented by sub-methods.
        """
        raise NotImplementedError()

    # -- Utility methods
    @staticmethod
    def string_to_digits(s):
        """ Convert a character string into a digit strings.

        Uses the conversion dictionary from the config.

        :param s: the string to convert
        :type s: str

        :return: a digit string
        :rtype: str
        """
        digits = ""
        for char in s:
            digits += str(CONVERSION[char])
        return digits

    @staticmethod
    def simplify(number, keep_power=True):
        """ Simplify a number string to a numerological entity

        :param number: The number to simplify
        :param keep_power: If we want to keep the powers (over 9)
        :return: a simplified number
        """
        # TODO: return an object with power?
        def add_digits(num):
            """ Add all the digits of a number together """
            res = 0
            for digit in str(num):
                res += int(digit)
            return res

        while len(str(number)) > 1:
            if keep_power and number in POWERS:
                break
            number = add_digits(number)

        return int(number)
