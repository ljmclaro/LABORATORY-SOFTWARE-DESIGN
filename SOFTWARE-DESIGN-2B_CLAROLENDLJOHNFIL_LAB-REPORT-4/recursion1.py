#4.1
'''def find_max(s):
    if len(s) < 1:
        return -1
    if len(s) <= 1:
        return s[0]
    if s[0] > s[-1]:
        return find_max(s[:-1])
    else:
        return find_max(s[1:])

print(find_max([10, 2, 3, 9, 4, 7, 3]))
print(find_max([1, 5, 146, 6, 8, 145, 147, 145]))'''

