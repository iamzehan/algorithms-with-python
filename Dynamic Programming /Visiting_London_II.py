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

def maximize_rating(attractions, available_time):
    n = len(attractions)  # Number of attractions
    
    # Create a 2D table to store the maximum rating for different time constraints
    dp = [[(0.0,'')] * (int(available_time * 2) + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for t in range(1, int(available_time * 2) + 1):
            name, duration, rating = attractions[i - 1]
            if duration <= t / 2:
                candidates1 = dp[i - 1][t]
                candidates2 = (dp[i - 1][int(t - 2 * duration)][0]+rating,(dp[i - 1][int(t - 2 * duration)][1] +", "+ name).strip(", "))
                dp[i][t] = max(candidates1,candidates2)
            else:
                dp[i][t] = dp[i - 1][t]

    return dp[n][-1]

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
    max_rating, places_selected = maximize_rating(attractions, available_time)
    print(f"Max Rating: {max_rating} \nOptimal set of Places to visit: {places_selected}")
