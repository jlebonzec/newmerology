""" Contains the AbstractMethod that any other computation should inherit and implement run()

Also contains various utility methods used for computations.
"""
import re
import datetime

from django.core.cache import cache

from calculator.config import CONVERSION, POWERS


# TODO: use Person? Remove middle_name
class AbstractBaseComputation(object):
    """ AbstractBaseComputation. Every other method should inherit from this one, implementing run()

    :type person: models.Person
    """

    def __init__(self, person):
        self.person = person
        self.given_names = person.given_names
        self.first_name = person.first_name
        self.middle_names = person.middle_names
        self.last_name = person.last_name
        self.full_name = person.full_name
        self.birth = person.birth
        self.gender = person.gender
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


class AbstractGridComputation(AbstractBaseComputation):
    """ AbstractGridComputation represents the computation of a cell in the grid.
    
    Because of how the display of the grid work, we have to compute the grid for every cell.
    Despite this operation being pretty fast (9 cells maximum), caching it avoids unnecessary work.
    
    :type person: models.Person
    """

    def __init__(self, person):
        super(AbstractGridComputation, self).__init__(person)
        self.cell_id = None
        cache_prefix = "person_grid_"
        self._cache_key = cache_prefix + str(person.pk)
        self._grid = cache.get(self._cache_key, {})

    @property
    def grid(self):
        """ Generate the grid if needed and return it """
        if not self._grid:
            self._grid = {}
            digits = digitize(self.full_name)

            for i in range(1, 10):
                count, explanation = count_occurrences(digits, i, explain=True)
                example = examplify(self.full_name, explanation, count)

                self._grid[i] = {
                    'count': count,
                    'example': example,
                }

            cache.set(self._cache_key, self._grid)
        return self._grid

    def run(self):
        if self.cell_id is None:
            raise ValueError("Set a cell_id to compute the results")

        self._result = self.grid[self.cell_id]['count']
        self._example = self.grid[self.cell_id]['example']


class AbstractTimeComputation(AbstractBaseComputation):

    def run(self):
        raise NotImplementedError()


# -- Other utility methods
def examplify(string, numbers, result, symbol="→"):
    """ Generate an example from a string-to-number conversion

    :param string: the string converted into numbers
    :type string: str

    :param numbers: the numbers obtained from the string
    :type numbers: str

    :param result: the result obtained after simplification
    :type result: int

    :param symbol: the symbol to use as link between numbers and result
    :type symbol: str

    :return: a list of examples
    :rtype: list of str
    """

    return [
        string.upper(),
        "%s %s %s" % (numbers, symbol, result)
    ]


def digitize(s):
    """ Convert a character string into a digit strings.

    Uses the conversion dictionary from the config.

    :param s: the string to convert
    :type s: str

    :return: a digit string
    :rtype: str
    """
    digits = ""
    for char in s:
        d = "_"

        try:
            d = str(int(char))  # Already a number
        except ValueError:
            pass

        try:
            d = str(CONVERSION[char.lower()])  # In the table?
        except KeyError:
            pass

        digits += d

    return digits


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
            try:
                res += int(digit)
            except ValueError:  # Can not be parsed
                continue
        return res

    # Is it already a number?
    try:
        number = int(number)
    except ValueError:
        # If length is already good, return; else ignore.
        if len(str(number)) <= 1:
            return 0

    while len(str(number)) > 1:
        if keep_power and number in POWERS:
            break
        number = add_digits(number)

    return number


def count_occurrences(digitized, c, explain=False):
    """ Applies a mask so only characters matching will be kept 
    
    :param digitized: the digitized string
    :type digitized: str
    
    :param c: the single character to keep occurrences of
    :type c: int or str
    
    :param explain: if the explanation should be returned as well.
        In such a case, the return value is a tuple (value, explanation)
    :type explain: bool
    
    :return: the count, or the count and the explanation if the latter is wanted too
    :rtype: str or tuple of str
    """
    c = str(c)
    count = digitized.count(c)

    if explain:
        pattern = '[^' + c + ']'
        re_digit = re.compile(pattern, re.IGNORECASE)
        matching = re.sub(re_digit, '_', digitized)
        return count, matching

    return count
