"""
* Supppose you are going to London for a nice vacation. You have two days there and a lot of things you want to do. You can't do everything, so you make a list.


| Attraction             | Duration (days)  | Rating |
|------------------------|------------------|--------|
| WESTMINSTER ABBEY      | 0.5              | 7      |
| GLOBE THEATER          | 0.5              | 6      |
| NATIONAL GALLERY       | 1                | 9      |
| BRITISH MUSEUM         | 2                | 8      |
| ST. PAUL'S CATHEDRAL   | 0.5              | 8      |


* Your task is to determine the most effective strategy for utilizing your available time to maximize the overall value, taking into account the ratings of the places you intend to visit.
"""

def camping_knapsack(items, capacity):
    n = len(items) # rows
    # Initialize a table to store the maximum values for different capacities
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1): #rows
        for w in range(1, capacity + 1): #columns
            # If the current item can fit in the knapsack, consider taking it
            if items[i - 1][1] <= w: 
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - items[i - 1][1]] + items[i - 1][2])
            else:
                # If it can't fit, don't take it
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find the selected items
    selected_items = []
    i, w = n, capacity
    while i > 0 and w > 0:
        print(i,w)
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(items[i - 1])
            print(selected_items)
            w -= items[i - 1][1]
        i -= 1

    return dp[n][capacity], selected_items

# Define the items
items = [("Water", 3, 10), ("Book", 1, 3), ("Food", 2, 9), ("Jacket", 2, 5), ("Camera", 1, 6)]

# Define the knapsack capacity
capacity = 6

# Find the optimal set of items and their total value
max_value, selected_items = camping_knapsack(items, capacity)

# Print the results
print(f"Optimal set of items to take:")
for item in selected_items:
    print(f"{item[0]} - Weight: {item[1]} lb, Value: ${item[2]}")
print(f"Total Value: ${max_value}")
