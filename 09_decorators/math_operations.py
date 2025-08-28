class Average:
    
    def __init__(self):
        self.series = []
    
    def __call__(self, number: int | float):
        self.series.append(number)
        return sum(self.series) / len(self.series)

avg = Average()
print(avg(10))
print(avg(20))
print(avg(30))