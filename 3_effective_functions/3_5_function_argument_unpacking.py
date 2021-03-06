#!/usr/bin/env python3
if __name__ == '__main__':
    def print_vector(x, y, z):
        print('<%s, %s, %s>' % (x, y, z))
    
    tuple_vec = (1, 0, 1)
    # unpacking tuple
    print_vector(*tuple_vec)

    genexpr = (x * x for x in range(3))
    # works with generators as well
    print_vector(*genexpr)

    dict_vec = {'y': 0, 'z': 1, 'x': 1}
    # dict unpacking
    print_vector(**dict_vec)
