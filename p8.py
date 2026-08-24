numbers= [10, 5, 8, 20, 15]
def sec_largest(numbers):
    largest = None
    second = None
    for num in numbers:
        if largest is None or num > largest:
            second = largest
            largest = num
        elif num != largest and (second is None or num > second):
            second = num       
    return second
result = sec_largest(numbers)
print("Second largest number is:", result)