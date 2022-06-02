#4.23
'''import os

file_name = "C:\Users\Engr.Claro\Documents\CLARO_SD_LABACT3.docx"
file_stats = os.stat(file_name)

print(file_stats)
print(f'File Size in Bytes is {file_stats.st_size}')
'''

#4.24
'''lst = []
num = int(input("Enter the size of the array: "))
print("Enter array elements: ")
for n in range(num):
  numbers = int(input())
  lst.append(numbers)
print("Sum:", sum(lst))'''

#4.26
'''def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n - 1, aux_rod, to_rod, from_rod)


n = 4
TowerOfHanoi(n, 'A', 'C', 'B')'''

#4.27
'''import os

if __name__ == "__main__":
    for (dirpath,dirnames,filenames) in os.walk('Test', topdown='true'):
        print(dirpath)
        print(dirnames)
        print(filenames)
        print('--------------------------------')'''



