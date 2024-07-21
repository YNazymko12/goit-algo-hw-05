def binary_search_with_upper_bound(arr, target):
    low = 0 
    high = len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        iterations += 1

        if guess == target:
            return iterations, guess
        elif guess > target:
            upper_bound = guess
            high = mid - 1
        else:
            low = mid + 1
    
    return iterations, upper_bound

# Тести:
arr = [1.1, 1.3, 2.5, 3.8, 4.6]
print(binary_search_with_upper_bound(arr, 3.5))  # Виведе: (2, 3.8)
print(binary_search_with_upper_bound(arr, 4))  # Виведе: (3, 4.6)
print(binary_search_with_upper_bound(arr, 6.0))  # Виведе: (3, None)
print(binary_search_with_upper_bound(arr, 2.5))  # Виведе: (1, 2.5)
print(binary_search_with_upper_bound(arr, 0))  # Виведе: (2, 1.1)
