def bubble_sort(arr):
    size = len(arr)
    print("| "+" | ".join(map(str,arr))+" |")
    swaps = 0
    passes = 0 
    comparisons = 0
    for i in range(size-1):
        swapped = False
        passes+=1
        print(f"pass: {passes} range: {size-1-i}\n----------------")
        
        for j in range(size-1-i):
            print(f"j: {j}, j+1: {j+1}")
            tmp = arr[j]
            print(f"comparing: {tmp} and {arr[j+1]}")
            comparisons+=1
            if tmp > arr[j+1]:
                print(f"swapping: {arr[j]} 🔄 {arr[j+1]}")
                arr[j] = arr[j+1]
                arr[j+1] = tmp
                print("| "+" | ".join(map(str,arr))+" |")
                swapped = True
                swaps+=1
        if not swapped:
            break
    return arr,swaps,passes,comparisons

if __name__ == "__main__":
    result, swaps, passes,comparisons = bubble_sort([5, 2, 8, 1, 7, 4, 6, 3])
    result = "| "+" | ".join(map(str,result))+" |"
    print(f"\n===========results============\nSorted Array: {result}\nTotal Swaps: {swaps}\nTotal Passes: {passes}\nTotal Comparisons: {comparisons}")
            
