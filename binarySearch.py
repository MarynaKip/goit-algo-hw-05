def binary_search(arr, x):
    if len(arr) < 1:
        return -1
    low = 0
    high = len(arr) - 1
    mid = 0
    attepms = 0
 
    while low <= high:
 
        mid = (high + low) // 2
        attepms +=1
        # якщо х більше ніж середне значення і менше ніж наступне за середнім - повертаємо більше за середне
        if arr[mid] < x and x < arr[mid+1]:
            return (arr[mid + 1], attepms)
        # якщо х  дорівнює сер значенню або менше ніж середне значення і більше ніж попередне перед середнім - повертаємо меньше за середне        
        elif x == arr[mid] or (arr[mid] > x and x > arr[mid-1]):
            return (arr[mid], attepms)
        
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        elif arr[mid] < x:
            low = mid + 1
 
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1
 
print(binary_search([1.2 , 4.5,   7.9,   10.2], 3))