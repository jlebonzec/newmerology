""" Contains the Abstract classes used for time computation (represented as timelines)
"""

from django.core.cache import cache
from django_translate.services import tranz

from calculator.computations.lifepath import Computation as LifePath
from calculator.computations.utils import (AbstractBaseComputation, examplify, simplify)


def create_period(start, content, example):
    """ Return a dictionary representing a period """
    return {
        'start': start,
        'content': content,
        'example': example
    }


class AbstractTimeComputation(AbstractBaseComputation):
    """ AbstractTimeComputation. Every time-related computation should extend this class
    
    :type person: models.Person
    """

    def __init__(self, person):
        super(AbstractTimeComputation, self).__init__(person)
        self.period_id = None

        cache_prefix = "person_time_"
        self._cache_key = cache_prefix + str(person.pk)
        self._periods = cache.get(self._cache_key, [])
        # self._periods = [{'start': 0, 'content': 5}, {'start': 18, 'content': 1}, ...]

    @property
    def periods(self):
        """ Generate periods if needed and return it """
        if not self._periods:
            self._periods = self.generate_periods()
            cache.set(self._cache_key, self._periods)
        return self._periods

    def generate_periods(self):
        """ Return the periods """
        raise NotImplementedError()

    def run(self):
        if self.period_id is None:
            raise ValueError("Set a period_id to compute the results")
        self._result = self.periods[self.period_id]['content']
        self._example = self.periods[self.period_id]['example']


class AbstractActionComputation(AbstractTimeComputation):
    """ AbstractActionComputation. Base class for all action computations. """

    def generate_periods(self):
        """ Return the periods and content of the actions """

        life_path = LifePath(self.person).result
        life_path = simplify(life_path, keep_power=False)

        action_1_start = 0
        action_1_value = simplify(self.birth.month + self.birth.day)
        action_1_example = examplify(
            "%s + %s" % (tranz("g.month"), tranz("g.day")),
            "%02d + %02d" % (self.birth.month, self.birth.day),
            action_1_value
        )

        action_2_start = 36 - life_path
        action_2_value = simplify(self.birth.year + self.birth.day)
        action_2_example = examplify(
            "%s + %s" % (tranz("g.year"), tranz("g.day")),
            "%04d + %02d" % (self.birth.year, self.birth.day),
            action_2_value
        )

        action_3_start = action_2_start + 9
        action_3_value = simplify(
            simplify(action_1_value, keep_power=False)
            + simplify(action_2_value, keep_power=False)
        )
        action_3_example = examplify(
            "%s + %s" % (tranz("g.action_1"), tranz("g.action_2")),
            "%d + %d" % (action_1_value, action_2_value),
            action_3_value
        )

        action_4_start = action_3_start + 9
        action_4_value = simplify(self.birth.year + self.birth.month)
        action_4_example = examplify(
            "%s + %s" % (tranz("g.year"), tranz("g.month")),
            "%04d + %02d" % (self.birth.year, self.birth.month),
            action_4_value
        )

        periods = [
            create_period(action_1_start, action_1_value, action_1_example),
            create_period(action_2_start, action_2_value, action_2_example),
            create_period(action_3_start, action_3_value, action_3_example),
            create_period(action_4_start, action_4_value, action_4_example),
        ]
        return periods


class AbstractCycleComputation(AbstractTimeComputation):
    """ AbstractCycleComputation. Base class for all cycle computations. """

    def generate_periods(self):
        cycle_1_start = 0
        # FIXME: Should it allow powers?
        cycle_1_value = simplify(self.birth.month)
        cycle_1_example = examplify(
            tranz("g.month"),
            "%02d" % self.birth.month,
            cycle_1_value
        )

        cycle_2_start = 28
        cycle_2_value = simplify(self.birth.day)
        cycle_2_example = examplify(
            tranz("g.day"),
            "%02d" % self.birth.day,
            cycle_2_value
        )

        cycle_3_start = 56
        cycle_3_value = simplify(self.birth.year)
        cycle_3_example = examplify(
            tranz("g.year"),
            "%04d" % self.birth.year,
            cycle_3_value
        )

        periods = [
            create_period(cycle_1_start, cycle_1_value, cycle_1_example),
            create_period(cycle_2_start, cycle_2_value, cycle_2_example),
            create_period(cycle_3_start, cycle_3_value, cycle_3_example)
        ]

        return periods
