#recursion a:
'''def findMinRec(A, n):
    if (n == 1):
        return A[0]
    return min(A[n - 1], findMinRec(A, n - 1))
def findMaxRec(A, n):
    if (n == 1):
        return A[0]
    return max(A[n - 1], findMaxRec(A, n - 1))

if __name__ == '__main__':
    A = [1, 4, 45, 6, -50, 10, 2]
    n = len(A)
    print(findMinRec(A, n))
    print(findMaxRec(A, n))'''

#recursion b:
'''def sum(x, y):
    if (y == 0):
        return x;
    else:
        return (1 + sum(x, y - 1));

x = int(input("Enter number first number: "))
y = int(input("Enter number second number: "))
print("Sum of two numbers are: ", sum(x, y))

def sub(x, y):
    if y == 0:
        return x
    return sub(x - 1, y - 1)

x = int(input("Enter some first number = "))
y = int(input("Enter some second number = "))
print("Sub of two numbers are: ", sub(x, y))'''

#recursion c:
'''a = "pots&pans"
b = a.split("&")

def reverse(word):

    if not word:
        return ""

    return reverse(word[1:]) + word[0]

result = reverse(b[1]) + "&" + reverse(b[0])

print(result)'''
