import sys


print(sys.version)


def median(lst):
    lst = sorted(lst)
    index = (len(lst) - 1) // 2
    print(lst)
    if len(lst) % 2 != 0:
        return lst[index]
    elif len(lst) % 2 == 0:
        return (lst[index] + lst[index + 1]) / 2.0


a = 0
print(median([1]))  # 1
print(median([1, 2, 3]))  # 2
print(median([4, 5, 5, 4]))  # 2.5
f"Test {a} test"
