# def average(l):
#     if not l:
#         return None
#     return sum(l) / len(l)

# if __name__ == "__main__":  
#     l = [1, 2, 3, 4, 5,6]
#     print(average(l))


# ....................

if __name__ == "__main__":
    L = [1,2,3,4,5]
    expected_result = 3
    avg_result = sum(L) / len(L)

    if expected_result == avg_result:
        print("Test passed")
    else:
        print("Test failed!", "received:", avg_result, "expected:", expected_result) 