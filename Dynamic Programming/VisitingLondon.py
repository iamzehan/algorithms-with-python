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
#this solution is a bit expensive

def maximize_rating(attractions, available_time):
    n = len(attractions)  # Number of attractions
    
    # Create a 2D table to store the maximum rating for different time constraints
    dp = [[0] * (int(available_time * 2) + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for t in range(1, int(available_time * 2) + 1):
            name, duration, rating = attractions[i - 1]
            if duration <= t / 2:
                dp[i][t] = max(dp[i - 1][t], dp[i - 1][int(t - 2 * duration)] + rating)
            else:
                dp[i][t] = dp[i - 1][t]

    # Backtrack to find the selected attractions
    selected_attractions = []
    i, t = n, int(available_time * 2)
    while i > 0 and t > 0:
        if dp[i][t] != dp[i - 1][t]:
            name, duration, rating = attractions[i - 1]
            selected_attractions.append(attractions[i - 1])
            t -= int(2 * duration)
        i -= 1

    return dp[n][int(available_time * 2)], selected_attractions

if __name__ == "__main__":
    # Define the attractions and available time
    attractions = [
        ("WESTMINSTER ABBEY", 0.5, 7),
        ("GLOBE THEATER", 0.5, 6),
        ("NATIONAL GALLERY", 1, 9),
        ("BRITISH MUSEUM", 2, 8),
        ("ST. PAUL'S CATHEDRAL", 0.5, 8),
    ]
    
    available_time = 2.0  # 2 days
    
    # Find the optimal set of attractions and their total rating
    max_rating, selected_attractions = maximize_rating(attractions, available_time)
    
    # Print the results
    print(f"Optimal set of attractions to visit:")
    for attraction in selected_attractions:
        print(f"{attraction[0]} - Duration: {attraction[1]} days, Rating: {attraction[2]}")
    print(f"Total Rating: {max_rating}")

