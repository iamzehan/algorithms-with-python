class DynamicProgramming:
    def camping_with_knapsack(self, items,total_capacity, number_of_items):
        dp = [[(0,'')]*(total_capacity+1) for _ in range(number_of_items+1)]
        for row in range(1, number_of_items+1):
            for col in range(1, total_capacity+1):
                if items[row-1]['weight']<=col:
                    candidate1 = dp[row-1][col]
                    candidate2 = (dp[row-1][col-items[row-1]['weight']][0]+items[row-1]['value'], 
                                 (dp[row-1][col-items[row-1]['weight']][1]+", "
                                  +items[row-1]['name']).strip(', ')) # (total_value, items_taken)
                    dp[row][col]=max(candidate1,candidate2)
                else:
                    dp[row][col] = dp[row-1][col]
        return dp

if __name__ == '__main__':
    items = [
    { 'name': 'Water', 'weight': 3, 'value': 10 },
    { 'name': 'Book', 'weight': 1, 'value': 3 },
    { 'name': 'Food', 'weight': 2, 'value': 9},
    { 'name': 'Jacket', 'weight': 2, 'value': 5},
    { 'name': 'Camera', 'weight': 1, 'value': 6}
    ]
    total_capacity = 6
    number_of_items = len(items)
    dp = DynamicProgramming()
    result = dp.camping_with_knapsack(items, total_capacity, number_of_items) 
    print(result)
    total_value, items = result[number_of_items][total_capacity]
    print("Optimal set of items to take: ",items)
    print(f"Total value: ${total_value}")
