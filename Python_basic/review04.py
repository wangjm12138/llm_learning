def sum_num(a, b, f):
    """

    :param a:
    :param b:
    :param f: high level function
    :return:
    """
    return f(a) + f(b)


def sum_num2(*args):
    def _sum_nums():
        sum1 = 0
        for num in args:
            sum1 += num
        return sum1
    return _sum_nums

def high_level_function():
    print(sum_num(1, 2, abs))
    print(sum_num(1, 2, lambda n: n**2))
    print(sum_num2(1,2,3,4)())

if __name__ == '__main__':
    high_level_function()