def b_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


my_list = [64, 34, 25, 12, 22, 11, 90]
b_sort(my_list)
##############

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def speak(self):
        return f"{self.name} гав гав!"

dog = Dog("Рекс")
print(dog.speak())  # Виведе "Рекс гав-гав!"


