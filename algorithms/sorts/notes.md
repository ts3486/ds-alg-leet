Sort algorithms have different use cases and certian scenarios where it outperforms the other. 

Bubble sort - Is commonly for an introduction to sorting algorithms and its use cases are very limted due to its low performance compared to the others. 

    Best case: O(n) (when the array is already sorted)
    Average case: O(n^2)
    Worst case: O(n^2)

Insertion sort - It is effective when the dataset is very small or it is already close to being completely sorted. 

    Best case: O(n) (when the array is already sorted)
    Average case: O(n^2)
    Worst case: O(n^2)

Selection sort - Given its time complexity, it is not ideal when speed matters. However its simple logic can be more readable and can be more advantageous when the dataset is small and speed differences are negligible. 

    Best case: O(n^2)
    Average case: O(n^2)
    Worst case: O(n^2)

Merge sort - Fast and very stable sort algorithm. If stability is very important merge sort can be chosen over quick sort. 

    Best case: O(n log n)
    Average case: O(n log n)
    Worst case: O(n log n) 

Quick sort - Usually the quickest sort option. It outperforms merge in terms of lower memory consunption (plus less code with recursion). However in certain cases where the pivot is inadequately selected, it can become very slow. 

    Best case: O(n log n)
    Average case: O(n log n)
    Worst case: O(n^2) (when the pivot selection is poor, e.g., always picking the smallest or largest element as the pivot)

