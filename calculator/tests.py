""" FIXME
"""

from django.test import TestCase

from calculator.models import Number


class TestNumber(TestCase):

    def test_make_room(self):
        Number(code="1", name="1", position=1).save()
        Number(code="3", name="3", position=3).save()
        Number(code="8", name="8", position=8).save()
        Number(code="3bis", name="3bis", position=3).save()
        Number(code="4", name="4", position=4).save()
        Number(code="9", name="9", position=9).save()

        expected_codes = ["1", "3bis", "4", "3", "8", "9"]
        expected_positions = [1, 3, 4, 5, 8, 9]
        expected = dict(zip(expected_codes, expected_positions))

        numbers = Number.objects.all()

        obtained_codes = [n.code for n in numbers]
        obtained_positions = [n.position for n in numbers]
        obtained = dict(zip(obtained_codes, obtained_positions))

        self.assertDictEqual(expected, obtained)

