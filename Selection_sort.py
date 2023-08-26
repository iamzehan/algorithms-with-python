"""Selection sort, the Big O notation for it is O(n^2)"""

# two steps to do selection sort
# Step 1: We find the smallest index in the list
# Step 2: We assign it to a new list one by one

def smallest_index(l):

    smallest_number = l[0]          # initial guess of smallest number, which it stores on an update

    smallest_index = 0              # initial guess of smallest index, which it stores on an update

    for i in range(1, len(l)):      # since we have already initialised on the first number, we start from later

        if l[i]<smallest_number:    # if the current number is smaller than the initialised smallest number

            smallest_number = l[i]  # we update the smallest number as we go through every element
            
            smallest_index = i      # we update the smallest index as we go through every element

    return smallest_index           # returning the smallest index

def selection_sort(l):

    new_list = []                   # this list would contain the sorted numbers

    for i in range(len(l)):         # we iterate through the whole list

        j = smallest_index(l)       # We find the smallest index of the current list

        new_list.append(l.pop(j))   # now we pop the item from the original list and put it into the new one, because it's the current smallest number in the list

    return new_list                 # returning the new list as answer, which has been sorted

print(selection_sort([3,7,4,2,9]))
