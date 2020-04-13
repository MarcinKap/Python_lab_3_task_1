
def call_counter(func):
    def counter(x,y):
        counter.calls += 1
        print('ilosc zliczen', counter.calls)
        return func(x, y)

    counter.calls = 0
    return counter


