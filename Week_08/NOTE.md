1、冒泡排序（Bubble Sort）

    def bubbleSort(arr):
        n = len(arr)
        for i in range(n):
            # Last i elements are already in place
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

2、选择排序（Selection Sort）

    def selectionSort(arr):
      	n = len(arr)
    		for i in range(): 
            min_idx = i 
            for j in range(i+1, n): 
                if arr[min_idx] > arr[j]: 
                    min_idx = j 
    
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr



3、插入排序（Insertion Sort）

    def insertionSort(arr): 
        for i in range(1, len(arr)): 
            key = arr[i] 
            j = i-1
            while j >=0 and key < arr[j] : 
                    arr[j+1] = arr[j] 
                    j -= 1
            arr[j+1] = key 
        return arr






