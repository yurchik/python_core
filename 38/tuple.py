item4 = ['December 23', 'September 12', 'February 23', 23]


def first_drop_last(grades):
    first, *all, last = grades
    print(first, last)


first_drop_last(item4)