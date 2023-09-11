"""Binary Search, the Big O notation for it is O(log2(n))"""
def binary_search(l,item):
    low = 0 				# The initial low point is always going to be zero.

    high = len(l)-1 			# the len() function returns the actual number of element, so deduction of 1 would give us the highest index there is.

    while low <= high: 			#while you haven't cut it down to one element

        mid = (high+low)//2 		#finding the mid point

        guess = l[mid] 			#your guess is always in the middle

        if guess == item: 		#compare your guess to the search item

            return mid 			#if found then we return the index, which is always in the middle for binary search

        elif guess > item: 		#if guess is greater than your search item then it means that your item lies on the left side of the middle 

            high = mid-1 		#that means our high point is going to be just left of the mid index

        else:
            low = mid + 1 		#otherwise it's the opposite, so we are going to set the low pointer just above the middle pointer

    return None 			#if the item doesn't exist after all the hassle, then we are returning None

print(binary_search([1,2,3,4,5,6,7,9], 9))
