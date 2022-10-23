class Heap:
    __data = []
    __is_min = False
    __heap_size = 0

    def __is_leaf(self, i):
        if Heap.__get_left_child_index(i) > len(self.__heap_size) and \
                Heap.__get_right_child_index(i) > len(self.__heap_size):
            return True
        return False

    @staticmethod
    def __get_parent_index(i):
        return (i - 1) // 2

    @staticmethod
    def __get_left_child_index(i):
        return 2 * i + 1

    @staticmethod
    def __get_right_child_index(i):
        return 2 * i + 2

    def __heapify(self, i, up=False):
        left = Heap.__get_left_child_index(i)
        right = Heap.__get_right_child_index(i)

        smallest_or_largest = i
        if self.__is_min:
            if left < self.__heap_size and self.__data[smallest_or_largest] > self.__data[left]:
                smallest_or_largest = left
            if right < self.__heap_size and self.__data[smallest_or_largest] > self.__data[right]:
                smallest_or_largest = right
        else:
            if left < self.__heap_size and self.__data[smallest_or_largest] < self.__data[left]:
                smallest_or_largest = left
            if right < self.__heap_size and self.__data[smallest_or_largest] < self.__data[right]:
                smallest_or_largest = right

        if smallest_or_largest != i:
            self.__data[i], self.__data[smallest_or_largest] = self.__data[smallest_or_largest], self.__data[i]
            if not up:
                self.__heapify(smallest_or_largest)
            else:
                parent_index = Heap.__get_parent_index(i)
                if parent_index >= 0:
                    self.__heapify(parent_index, up=True)

    def __build_heap(self):
        for i in range(self.__heap_size // 2 - 1, -1, -1):
            self.__heapify(i)

    def __init__(self, data=None, is_min=False):
        if is_min:
            self.__is_min = True
        if data:
            self.__data = list.copy(data)
            self.__heap_size = len(data)
            self.__build_heap()

    def append(self, item):
        self.__data.append(item)
        parent_index = Heap.__get_parent_index(self.__heap_size)
        self.__heap_size += 1
        self.__heapify(parent_index, True)

    def delete_at(self, index):
        if index < 0 or index >= self.__heap_size:
            raise IndexError

        result = self.__data[index]
        parent = Heap.__get_parent_index(index)
        if parent < 0:
            parent = 0

        del self.__data[index]
        self.__heap_size -= 1

        self.__heapify(parent)

        return result

    def __str__(self):
        return str(self.__data)
