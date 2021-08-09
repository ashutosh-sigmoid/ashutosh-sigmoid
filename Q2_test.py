from unittest import TestCase
from Q2 import compensation


class ProblemTest(TestCase):
    def setUp(self) -> None:
        self.Compensation = compensation("cur")

    def tearDown(self) -> None:
        self.Compensation = None

    def test_get_result(self):
        self.assertEqual(self.Compensation.total_compensation(), False)