# 1. Необходимо реализовать метод разворота связного списка (двухсвязного или односвязного на выбор).
# 2. Реализовать сортировку пузырьком для двухсвязного списка

class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class List_2:
    def __init__(self):
        self.start_node = None

    def print_1(self):
        n = self.start_node
        while n is not None:
            print(n.data, end=' ')
            n = n.next
        print()

    def insert_start(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return

        new_node.next = self.start_node
        self.start_node.prev = new_node
        self.start_node = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.next:
            n = n.next
        n.next = new_node
        new_node.prev = n


# Функция реверса двусвязного списка
    def reverse(self):
        temp = None
        current = self.start_node

        while current is not None:      # Поменять местами следующее и предыдущее для всех узлов
            temp = current.prev          
            current.prev = current.next
            current.next = temp
            current = current.prev

        if temp is not None:                 # Перед заменой головы проверить
            self.start_node = temp.prev     # пустой ли список и в списоке только один узел

               

#Пузырьковая сортировка двусвязного списка
    def bubbleSort(self):
        if self.start_node is not None:
            n = self.start_node
            while n.next is not None:
                index = n.next
                while index is not None:
                    if n.data > index.data:
                        temp = n.data
                        n.data = index.data
                        index.data = temp
                    index = index.next
                n = n.next    
    
     
l2 = List_2()
l2.insert_start(2)
l2.insert_start(3)
l2.insert_start(1)
l2.insert_start(0)
l2.insert_start(2)
l2.insert_start(5)
l2.insert_end(7)
l2.insert_end(9)
print("Двусвязный список: ")
l2.print_1()
print("Разворот двусвязного списока: ")
l2.reverse()
l2.print_1()
print("Отсортированный двусвязный список: ")
l2.bubbleSort()
l2.print_1()

