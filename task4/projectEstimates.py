import math


class Task:
    """Task class has three property: best_case_estimate, most_likely_estimate, worst_case_estimate
    and methods to calculate estimate (E) and standard deviation (SD) for each task."""
    def __init__(self, task: dict):
        self.__best_case_estimate = task["best_case_estimate"]
        self.__most_likely_estimate = task["most_likely_estimate"]
        self.__worst_case_estimate = task["worst_case_estimate"]

    def get_task_estimate(self) -> float:
        """Calculates an estimate (E) using the following formula: E(task) = (a + 4m + b) / 6.
        :return task_estimate(float)."""
        return (self.__best_case_estimate + 4 * self.__most_likely_estimate + self.__worst_case_estimate) / 6

    def get_task_standard_deviation(self) -> float:
        """Calculates a standard deviation (SD) using the following formula: SD(task) = (b − a) / 6.
        :return task_standard_deviation(float)."""
        return (self.__worst_case_estimate - self.__best_case_estimate) / 6


class Project:
    """Project class has two property: tasks_estimate_list, tasks_standard_deviation_list and methods.
    to calculate project estimate, project standard error, confidence interval."""
    def __init__(self, tasks_estimate_list: list, tasks_standard_deviation_list: list):
        self.__tasks_estimate_list = tasks_estimate_list
        self.__tasks_standard_deviation_list = tasks_standard_deviation_list

    def get_project_estimate(self) -> float:
        """Calculates the expected value for the total project work time.
        :return project_estimate(float)."""
        return sum(self.__tasks_estimate_list)

    def get_project_standard_error(self) -> float:
        """Calculates the value SE(project) for the standard error of the estimated total project work time.
        :return project_standard_error(float)."""
        return round(math.sqrt(sum([i ** 2 for i in self.__tasks_standard_deviation_list])))

    def get_confidence_interval_95(self) -> dict:
        """Calculates the 95% confidence interval (CI) for the project based on formula: E(project) ± 2 × SE(project)
        :return dict consists from min_confidence_interval(int), max_confidence_interval(int)"""
        min_confidence_interval = int(round((self.get_project_estimate() - 2 * self.get_project_standard_error()), 0))
        max_confidence_interval = int(round((self.get_project_estimate() + 2 * self.get_project_standard_error()), 0))
        return {"min_CI": min_confidence_interval, "max_CI": max_confidence_interval}


if __name__ == '__main__':
    project_tasks_list = []
    continue_ = True
    while continue_:
        try:
            task_estimation = {"best_case_estimate": int(input("Enter the best-case estimate: ")),
                               "most_likely_estimate": int(input("Enter the most-likely estimate estimate: ")),
                               "worst_case_estimate": int(input("Enter the worst-case estimate-case estimate: "))}
            project_tasks_list.append(task_estimation)
        except ValueError:
            print("Please enter integer numbers!")

        continue_ = input("Do you want add another task estimation (y / n): ").lower() == "y"

    if len(project_tasks_list) > 0:
        tasks_estimate_list = []
        tasks_standard_deviation_list = []

        for task_data in project_tasks_list:
            tasks_estimate_list.append(Task(task_data).get_task_estimate())
            tasks_standard_deviation_list.append(Task(task_data).get_task_standard_deviation())

        project = Project(tasks_estimate_list, tasks_standard_deviation_list)

        print(f"Project's 95% confidence interval: {project.get_confidence_interval_95()['min_CI']} ... "
              f"{project.get_confidence_interval_95()['max_CI']} points")


