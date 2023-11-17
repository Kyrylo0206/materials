size = int(input("Enter the size of the array: "))

my_array = []

print("Enter the array elements:")
for _ in range(size):
    element = int(input())
    my_array.append(element)

print("Array elements:", my_array)
