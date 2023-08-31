class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0
        basket = {}  # A dictionary to store the types of fruits in the baskets
        start = 0  # Start index of the current sequence
        
        for end, fruit in enumerate(fruits):
            basket[fruit] = end  # Update the index of the last occurrence of the fruit
            
            if len(basket) > 2:  # If there are more than 2 types of fruits in the baskets
                # Find the index of the oldest fruit and remove it from the baskets
                oldest_fruit = min(basket.values())
                del basket[fruits[oldest_fruit]]
                start = oldest_fruit + 1  # Update the start index
                
            max_fruits = max(max_fruits, end - start + 1)  # Update the maximum number of fruits
        
        return max_fruits