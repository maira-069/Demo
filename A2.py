def second_largest(numbers):
    largest = None
    second = None

    for num in numbers:
        
        if largest is None or num > largest:
            if num != largest:
                second = largest
                largest = num

        elif num != largest and (second is None or num > second):
            second = num

    return second


print(second_largest([10, 5, 8, 20, 15]))