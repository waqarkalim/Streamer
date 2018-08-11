from multiprocessing import Process


def square(x):

    for x in numbers:
        print('%s squared  is  %s' % (x, x**2))


def is_even(x):

    for x in numbers:
        if x % 2 == 0:
            print('%s is an even number ' % (x))


if __name__ == '__main__':
    numbers = [43, 50, 5, 98, 34, 35]

    p1 = Process(target=square, args=('x',))
    p2 = Process(target=is_even, args=('x',))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
