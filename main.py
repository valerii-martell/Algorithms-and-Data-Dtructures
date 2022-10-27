import itertools
import math
import sys

import bitwise
import dynamic
import fibonacci
import hanoi
import heap
import palindrome
import percentile
import search
import sort
import dividers
import wave
import random
import bst_recursive as bstr
from bst_iterative import BST
from graphs import Graph
from search import binary_search

# unsorted_list = list(random.randint(0, 100) for _ in range(0, 10))
unsorted_list = list(random.sample(range(0, 100), 10))


# unsorted_list = [1,0,3,0,3,0]

def print_sort(l, method):
    result = method(l)
    print('{}:\t {}'.format(method.__name__, result))


if __name__ == '__main__':
    # l = [int(x) for x in input().split()]
    # print(l)
    # print("Sorting:")
    # print(unsorted_list)
    # result = sort.bubble_sort(unsorted_list)
    # print_sort(unsorted_list, sort.bubble_sort)
    # print_sort(unsorted_list, sort.insertion_sort)
    # print_sort(unsorted_list, sort.selection_sort)
    # print_sort(unsorted_list, sort.merge_sort)
    # print_sort(unsorted_list, sort.quick_sort)
    # print_sort(unsorted_list, sort.heap_sort)
    # print_sort(unsorted_list, sort.counting_sort)
    # print(unsorted_list)
    #
    # print("Dividers:")
    # print(dividers.get_dividers(24))
    # print("Is prime:")
    # print(dividers.is_prime(3))
    # print("Prime numbers:")
    # print(dividers.get_prime_numbers(9))
    # print("Prime factors:")
    # print(dividers.prime_factors(121))
    # print("GCD subtraction:")
    # print(dividers.get_gcd1(8, 12))
    # print("GCD modulo:")
    # print(dividers.get_gcd2(8, 12))
    # print("LCM:")
    # print(dividers.get_lcm(8, 12))
    #
    # # matrix = [[0]*5 for _ in range(0, 5)]
    # print("Lee (wave) algorithm:")
    # wave.wave([
    #     [0, 1, 0, 1],
    #     [1, 0, 1, 0],
    #     [0, 1, 0, 0],
    #     [1, 0, 0, 1]
    # ], 0, 1)
    #
    # print("Fibonacci iterative:")
    # print(fibonacci.fib(0))
    # print("Fibonacci lazy dynamic:")
    # print(fibonacci.get_fib(0))
    #
    # print("\n\n")
    #
    # print("DFS iterative & DFS recursive & BFS:")
    # adjecency_list = [
    #     [(1, 10), (2, 5)],
    #     [(0, 10), (3, 1)],
    #     [(0, 5), (3, 1)],
    #     [(1, 1), (2, 1)],
    # ]
    #
    # graph = Graph(adjecency_list)
    #
    # print(graph.dfs(0))
    # print(graph.dfs_recursive(0))
    # print(graph.bfs(0))
    #
    # adjecency_list = [
    #     [(1, 10), (2, 5)],
    #     [(0, 10), (3, 1), (4, 2)],
    #     [(0, 5)],
    #     [(1, 1)],
    #     [(1, 1)],
    # ]
    #
    # graph = Graph(adjecency_list)
    #
    # print(graph.dfs(0))
    # print(graph.dfs_recursive(0))
    # print(graph.bfs(0))

    # adjecency_list = [
    #     [(1, 10), (2, 2)],
    #     [(0, 10), (3, 5), (4, 1)],
    #     [(4, 4), (5, 12)],
    #     [(1, 5), (6, 3)],
    #     [(1, 1), (2, 4), (6, 8)],
    #     [(2, 12), (7, 6)],
    #     [(3, 3), (4, 8), (7, 4)],
    #     [(5, 6), (6, 4)],
    # ]
    #
    # graph = Graph(adjecency_list)
    #
    # print(*graph.dijkstra(0, 7))
    # print(*graph.prim())
    #
    # incidence_matrix = [
    #     [0, 5, 0, 6, 0, 50],
    #     [5, 0, 7, 0, 0, 0],
    #     [0, 7, 0, 4, 0, 10],
    #     [6, 0, 4, 0, 10, 0],
    #     [0, 0, 0, 10, 0, 8],
    #     [50, 0, 10, 0, 8, 0]
    # ]
    #
    # graph = Graph(None)
    # graph.from_matrix(incidence_matrix)
    # print(graph.floyd_warshall()[0][5])

    # print(palindrome.is_palindrome(51615))
    # print(palindrome.is_palindrome(5))
    # print(palindrome.is_palindrome(10001))
    # print(palindrome.is_palindrome(1001))
    # print(palindrome.is_palindrome(11))
    # print(palindrome.is_palindrome(12))

    # print("Binary search tree:")
    # bst = BST()
    # bst.insert(40)
    # bst.insert(100)
    # bst.insert(20)
    # bst.insert(30)
    # bst.insert(50)
    # bst.insert(60)
    # bst.insert(1)
    # print(bst.inorder())
    # print(bst.select(50).key)
    # print("root", bst.root.key)
    # bst.delete(50)
    # print(bst.inorder())
    # print(bst.get_min().key)
    # print(bst.get_max().key)
    #
    # print("Binary search tree recursive:")
    # bst = bstr.Node(10)
    # bst = bstr.insert(bst, 20)
    # bst = bstr.insert(bst, 20)
    # bst = bstr.insert(bst, 30)
    # bst = bstr.insert(bst, 40)
    # bst = bstr.insert(bst, 50)
    # bst = bstr.insert(bst, 5)
    # bst = bstr.insert(bst, 1)
    # bst = bstr.insert(bst, 100)
    # print(bstr.inorder(bst))
    # bst = bstr.delete(bst, 20)
    # bst = bstr.delete(bst, 20)
    # bst = bstr.delete(bst, 100)
    # bst = bstr.delete(bst, 30)
    # bst = bstr.delete(bst, 1)
    # bst = bstr.delete(bst, 5)
    # print(bstr.inorder(bst))
    # print(bstr.select(bst, 50).key)

    # print("Bitwise:")
    # print(bitwise.is_two_pow(5))
    # print(4 >> 3)
    # print(8 << 2)
    # print("Is odd:")
    # print(bitwise.is_odd(4))
    # print(bitwise.is_odd(3))
    # print("Is zero:")
    # print(bitwise.is_zero(0))
    # print(bitwise.is_zero(5))
    # print(bitwise.is_zero(-2))
    # print("Signum:")
    # print(bitwise.signum(0))
    # print(bitwise.signum(10))
    # print(bitwise.signum(-15))
    # print("Swap")
    # print(*bitwise.swap(1, 100))
    # print("Adder")
    # print(bitwise.adder(6, 7))
    # print(bitwise.adder(7, 6))
    # print("Subtractor")
    # print(bitwise.subtractor(7, 6))
    # print(bitwise.subtractor(6, 7))
    # # print("Multiplier")
    # print(bitwise.multiplicator(4, -6))
    # print(bitwise.multiplicator(8, 6))
    # print("Divider")
    # print(bitwise.divider(12, 2))
    # print("Pow")
    # print(bitwise.pow(4, 2))
    # print("Odd occurrences")
    # print(bitwise.get_occurrences([1, 1, 5, 6, 5, 9, 7, 7, 7, 9, 6, 6]))
    # print("\n\n")
    # print("Percentile:")
    # print(percentile.get_percentile([5, 6, 9, 87, 2, 3, 5, 7, 2, 6, 5, 2, 3, 4, 69, 4], 50))
    # print(percentile.get_percentile([1, 2, 3, 4], 25))

    # print("Dynamic. Rabbit:")
    # print(rabbit.rabbit_moves(1, 1))
    # print(rabbit.rabbit_moves(4, 3))
    #
    # print("Dynamic. Coins:")
    # print(coins.coins([1, 2, 3], 4))
    # print(coins.coins([1, 2, 3], 3))
    # print(coins.coins([2, 5, 3, 6], 10))
    # print(coins.coins([10], 10))
    # print(coins.coins([5, 10], 25))
    #
    # print("Best change:")
    # print(coins.best_change([1, 2, 3], 4))
    #
    # l = [
    #      [1, 0, 0],
    #      [1, 2, 0],
    #      [2, 3, 5]
    # ]
    #
    # print(l[2][1])
    #
    # print("Dynamic. Hanoi tower:")
    # print(hanoi.hanoi(3, 1, 3, 2))

    # s = "31173"

    # print(s[1:len(s)])

    # primes = [311, 173, 73, 31, 17, 11, 7, 3]

    # print(dynamic.unique_prime_combos("31173"))

    # primes = [311,173,73,31,17,11,7,3]
    # primes = [311,173,73,31,17,11,7,3]
    # primes.reverse()
    # primes = [3, 7, 73]
    #
    # def combos(s):
    #     result = []
    #
    #     def _combos(s):
    #         for prime in primes:
    #             if str(prime) in s[0:len(str(prime))]:
    #                 # print(f"{str(prime)} in {s[0:len(str(prime))]}")
    #                 head = s[0:len(str(prime))]
    #                 tail = s[len(str(prime)):len(s)]
    #                 # print(head)
    #                 # print(tail)
    #                 res = []
    #                 if int(tail) in primes:
    #                     res = [tail]
    #                 else:
    #                     if len(tail) > 1:
    #                         res = _combos(tail)
    #                 for r in res:
    #                     r.append([head])
    #                 return res
    #
    #     result.append(_combos(s))
    #     return result
    #
    #
    # for combo in combos("733"):
    #     print(combo)

    #

    # print([1]+[2,3])
    # print(combos("31173"))

    # def readlines():
    #     for line in sys.stdin:
    #         yield line.strip('\n')
    #
    # lines = readlines()
    # while True:
    #     try:
    #         print(eval(next(lines)))
    #         # arr = eval(next(lines))
    #         # X = eval(next(lines))
    #         # print(solve(arr, X))
    #     except StopIteration:
    #         break

    # print(dynamic.all_combos_from_list([1,3,3]))

    # heap = heap.Heap([10, 3, 11, 4, 5, 2], is_min=True)
    # print(heap)
    # heap.append(1)
    # print(heap)
    # heap.delete_at(1)
    # print(heap)
    # heap.delete_at(0)
    # print(heap)
    # heap.delete_at(0)
    # print(heap)
    # heap.delete_at(0)
    # print(heap)
    # heap.delete_at(0)
    # print(heap)

    # for j in range(1, 4):
    #    for i in itertools.combinations([1, 2, 3], j):
    #        print(i)

    print("All combos:")
    print(dynamic.number_of_all_combos(4))
    print(dynamic.all_combos(4))

    print("All unique combos:")
    print(dynamic.number_of_unique_combos(4))
    print(dynamic.all_unique_combos(4))

    # print(sort.sort_logs(["def1 1 2 4 5", "let1 art zero", "def3 2 0 9 8", "let2 art can"]))

    print("All combos from list:")
    print(dynamic.all_combos_from_list([1, 2, 3]))

    print("Permutations from list:")
    print(dynamic.permutations([1, 2, 3]))

    # print(list(itertools.chain.from_iterable(
    #    itertools.combinations([1, 2, 3], i+1) for i in range(len([1, 2, 3]) + 1))))

    arr = [1, 2, 3, 4]
    print(search.binary_search(arr, 4, 0, len(arr) - 1))
    print(search.binary_search(arr, 3, 0, len(arr) - 1))

    pass
