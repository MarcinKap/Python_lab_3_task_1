from Project.Decorator import call_counter
from Project.runnable import Runnable


# @call_counter
class Fibonacci(Runnable):

    @call_counter
    def run(self, n):
        print(self.fibonacci(n))
        return None


    # def __init__(self, n):
    #     self.n = n
    #     self.fibonacci()

    def fibonacci(self, n):

        if n<0:
            print("Incorrect input")
        # First Fibonacci number is 0
        elif n==0:
            return 1
        elif n==1:
            return 1
        # Second Fibonacci number is 1
        elif n==2:
            return 1
        else:
            return self.fibonacci(n-1)+self.fibonacci(n-2)
