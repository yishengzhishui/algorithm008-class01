import heapq


def heapSort(arr):
    n = len(arr)
    queue = []

    heapq.heapify(arr)
    for i in range(n):
        queue.append(heapq.heappop(arr))
    print(queue)



arr = [2,3,5,6,7,1]
heapSort(arr)