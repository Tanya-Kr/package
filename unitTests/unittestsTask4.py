from package.task4.projectEstimates import Task
from package.task4.projectEstimates import Project
import unittest
from unittest import TestCase, main, TestSuite


class TaskTest(TestCase):
    def setUp(self) -> None:
        data = {"best_case_estimate": 24, "most_likely_estimate": 33, "worst_case_estimate": 42}
        self.task = Task(data)

    def test_get_task_estimate(self):
        expected = 33

        actual = self.task.get_task_estimate()

        self.assertEqual(expected, actual)

    def test_get_task_standard_deviation(self):
        expected = 3

        actual = self.task.get_task_standard_deviation()

        self.assertEqual(expected, actual)


class ProjectTest(TestCase):
    def setUp(self) -> None:
        self.project = Project([25, 40], [45, 43])

    def test_get_project_estimate(self):
        expected = 65

        actual = self.project.get_project_estimate()

        self.assertEqual(expected, actual)

    def test_get_project_standard_error(self):
        expected = 62

        actual = self.project.get_project_standard_error()

        self.assertEqual(expected, actual)

    def test_get_confidence_interval_95(self):
        expected = {'min_CI': -59, 'max_CI': 189}
        actual = self.project.get_confidence_interval_95()

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()