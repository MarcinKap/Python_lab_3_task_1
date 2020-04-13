from Project import Iterator
from Project.Iterator import Fibonacci


def main():



    print('zaczynamy')
    fibbonaci = Fibonacci()
    fibbonaci.run(4)
    fibbonaci.run(10)
    fibbonaci.run(11)
    fibbonaci.run(20)


if '__main__' == __name__:
    main()