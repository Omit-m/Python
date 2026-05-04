def add_numbers(numbers):
    global result
    result = 0
    for number in numbers:
        result +=number
    return result
    
add_numbers([2,3,4,5,6,7,7])
print(result)

