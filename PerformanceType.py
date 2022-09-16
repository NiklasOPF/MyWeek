# Performs a certain type of performance.
# e.g.

class PerformanceType:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def Equals(self, performanceType2):
        if self.name == performanceType2.name:
            if self.category == performanceType2.category:
                return True
        return False
