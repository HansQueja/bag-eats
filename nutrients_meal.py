def calculate_meal_balance(nutrients):
    def score_nutrient(value, ideal_range):
        if value == -1:  # No data provided
            return None
        low, high = ideal_range
        if low <= value <= high:
            return 1
        elif value < low:
            return value / low
        else:
            return max(0, 1 - (value - high) / high)

    ideal_ranges_meal = {
        'calories': (200, 400),
        'total_fat': (5, 30),
        'saturated_fat': (0, 10),
        'trans_fat': (0, 1),
        'cholesterol': (0, 100),
        'sodium': (0, 600),
        'total_carbs': (0, 90),
        'dietary_fiber': (5, 15),
        'sugars': (0, 15),
        'protein': (15, 40),
        'vitamin_a': (1, 30),
        'vitamin_c': (1, 30),
        'calcium': (2, 30),
        'iron': (2, 30),
        'potassium': (300, 1000)
    }

    scores = {}
    total_nutrients = len(ideal_ranges_meal)
    nutrients_with_data = 0

    for nutrient, value in nutrients.items():
        if nutrient in ideal_ranges_meal:
            if value != -1:  # Check if data is provided
                score = score_nutrient(value, ideal_ranges_meal[nutrient])
                if score is not None:
                    scores[nutrient] = score
                    nutrients_with_data += 1

    if not scores:
        return 0, 0

    balance_score = sum(scores.values()) / len(scores)
    completeness = nutrients_with_data / total_nutrients

    return balance_score * 100, completeness * 100

# Example usage
meal_item = {
    'calories': 222,
    'total_fat': 10,
    'saturated_fat': 3.493,
    'trans_fat': -1,
    'cholesterol': 49,
    'sodium': 412,
    'total_carbs': 17,
    'dietary_fiber': 2.1,
    'sugars': 12.7,
    'protein': 16.56,
    'vitamin_a': 6,
    'vitamin_c': 12,
    'calcium': 55,
    'iron': 1.73,
    'potassium': 567  # No data provided for potassium
}

meal_balance, meal_completeness = calculate_meal_balance(meal_item)
print(f"Meal Nutritional Balance Score: {meal_balance:.2f}")
print(f"Meal Data Completeness: {meal_completeness:.2f}%")