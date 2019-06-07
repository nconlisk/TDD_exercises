from django.test import TestCase

class DuckTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1+1, 3)
