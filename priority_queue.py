def heapify(queue, n, i):
    largest = i
    #left i child
    l = 2 * i + 1
    #right i child 
    r = 2 * i + 2

    # check if root is the biggest
    if l < n and queue[i] < queue[l]:
        largest = l
    
    if r < n and queue[largest] < queue[r]:
        largest = r

    #if not swap root with the largest child
    if largest != i:
        queue[i], queue[largest] = queue[largest], queue[i]
        #heapify swapped root
        heapify(queue, n, largest)

def insert(queue, new_element):
    if len(queue) == 0:
        queue.append(new_element)
    else:
        queue.append(new_element)
        #heapify each root 
        for i in range((len(queue) - 1) // 2, -1, -1):
            heapify(queue, len(queue), i)

queue = []

insert(queue, 4)
insert(queue, 3)
insert(queue, 54)
insert(queue, 32)
insert(queue, 11)
insert(queue, 45)
insert(queue, 36)
insert(queue, 6)

print(str(queue))

