# Performs a certain type of performance.
# e.g.

class PerformanceType:
    def __init__(self, name, category):
        if name == "":
            raise ValueError("The name of a performance type cannot be empty")
        if category == "":
            raise ValueError("The category of a performance type cannot be empty")
        self.name = name
        self.category = category

    def Equals(self, performanceType2):
        if self.name == performanceType2.name:
            if self.category == performanceType2.category:
                return True
        return False


    def GetName(self):
        return self.name

    def GetCategory(self):
        return self.category