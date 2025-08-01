class NegativeNumberError(Exception):
    def __init__(self, message="negative numbers not allowed"):
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return self.message