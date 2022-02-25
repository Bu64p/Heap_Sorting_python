import math

def build_heap(input_array,size):

    # applay the Max heap attribute to array:
    for i in range(math.ceil(size/2),-1,-1):
        heapify(i,size)
    # now the we have a Max heap but we want a sorted array not a heap with sorted roots:
    heap2line(size)

def heap2line(size):
# take max element out of heap and re-build the heap:
    for i in range(size-1,0,-1):
        exchange(0, i)
        size = size-1
        heapify(0,size)

def heapify(index,size):
# apply the max heap attribute for parent and two (or one) roots:
    left = left_index(index)
    right = right_index(index)
    largest = index

    if size > left and input_array[left] > input_array[largest]:
        largest = left
    if size > right and input_array[right] > input_array[largest]:
        largest = right
    if largest != index:
      # if we have change in heap's structure, we should check the Max heap attribute for changed element;
      # the interesting part of code is here, use Recursion: 
        exchange(largest,index)
        heapify(largest,size)

def left_index(index):
    # get the right index of parent(heap) in array:
    return index*2+1

def right_index(index):
    # get the left index of parent(heap) in array: 
    return (index+1)*2

def exchange(in1,in2):
    # just a very simple method to exchange 2 element in array:
    temp = input_array[in1]
    input_array[in1] = input_array[in2]
    input_array[in2] = temp

size = int(input("Inter the size of your list: "))
input_array = []
for i in range(0,size):
    input_array.append(float(input(str(i+1) + ". ")))
print(input_array,end="")
# call the first method to start the Process:
build_heap(input_array,size)
print(" ====> ",end="")
print(input_array)