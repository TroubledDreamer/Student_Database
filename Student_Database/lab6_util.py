def my_map(f, lst):
    if lst == []:
        return []
    else:
        return [f(lst[0])] + my_map(f, lst[1:])


def my_filter(f, lst):
    if lst == []:
        return []
    elif f(lst[0]):
        return [lst[0]] + my_filter(f, lst[1:])
    else:
        return my_filter(f, lst[1:])


def foldr(combiner, base, lst):
    if lst == []:
        return base
    else:
        return combiner(lst[0], foldr(combiner, base, lst[1:]))


def myzip(lst1, lst2):
    if lst1 == [] or lst2 == []:
        return []
    else:
        return [(lst1[0], lst2[0])] + myzip(lst1[1:], lst2[1:])