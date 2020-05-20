class Estimates:
    def __init__(self, best_case_estimate, most_likely_estimate, worst_case_estimate):
        self.best_case_estimate = best_case_estimate
        self.most_likely_estimate = most_likely_estimate
        self.worst_case_estimate = worst_case_estimate

    def estimate_calculation(self):
        return (self.best_case_estimate + 4 * self.most_likely_estimate + self.worst_case_estimate) / 6

    def standard_deviation_calculation(self):
        return (self.worst_case_estimate - self.best_case_estimate) / 6