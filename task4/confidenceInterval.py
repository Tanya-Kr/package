from package.task4.projectEstimates import Estimates


def confidence_interval_mix_calculation(estimate, standard):
    return estimate - 2 * standard


def confidence_interval_max_calculation(estimate, standard):
    return estimate + 2 * standard


project_1 = Estimates(1, 2, 3)
project_2 = Estimates(30, 150, 80)


def print_project_confidence_interval(project):
    min = confidence_interval_mix_calculation(project.estimate_calculation(), project.standard_deviation_calculation())
    max = confidence_interval_max_calculation(project.estimate_calculation(), project.standard_deviation_calculation())

    print(f"Project's 95% confidence interval: {round(min)} ... {round(max)} points")


print_project_confidence_interval(project_1)
print_project_confidence_interval(project_2)