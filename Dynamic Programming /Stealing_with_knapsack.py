def stealing_with_knapsack(items, capacity):
    n = len(items)
    dp = [[0000]*(capacity+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for w in range(1, capacity+1):
            if items[i-1][1]<=w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-items[i-1][1]]+items[i-1][2])
            else:
                dp[i][w] = dp[i-1][w]
    i, w = n, capacity
    selected_items=[]
    while i>0 and w>0:
        if dp[i-1][w]!=dp[i][w]:
            selected_items.append(items[i-1])
            w -= items[i-1][1]
        i-=1
    
    return dp[n][capacity],selected_items

if __name__ == "__main__":
  items = [
      ("Guiter",1, 1500),
      ("Stereo",4,3000),
      ("Laptop",3,2000)
      ]
  capacity = 4
  
  max_value, items = stealing_with_knapsack(items, capacity)
  
  print("\n".join([f"✔{item[0]} Selected! \n Weighs: {item[1]}lb\n Value: ${item[2]}" for item in items])) 
  print(f"Maximized value of Stolen Items: ${max_value}")
