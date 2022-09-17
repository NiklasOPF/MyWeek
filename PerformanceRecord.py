# This class defines a given measurement along a certain dimension of performance.
# e.g. The nubmer of hours spent talking to my family last week

class PerformanceRecord:
    def __init__(self, time_range, performance_metric, performance_type):
        self.time_range = time_range
        self.performance_metric = performance_metric
        self.performance_type = performance_type

    def GetPerformanceMetric(self):
        return self.performance_metric

    def GetPerformanceType(self):
        return self.performance_type