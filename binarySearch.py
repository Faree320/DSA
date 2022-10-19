import time
import math
from jovian.pythondsa import evaluate_test_case


# ------------------ Linear Search ----------------------- #
# numbers = [10, 8, 6, 5, 4, 2, 1]
# output = 2
#
# start_time = time.time()
# for i, j in enumerate(numbers):
#     if j == output:
#         print("I found it after {} numbers of turn".format(i + 1))
#         time.sleep(1)
#
# print("--- %s seconds ---" % (time.time() - start_time))


# ------------------ Binary Search ----------------------- #

# test = {
#     "input": {
#         "cards": [13, 11, 10, 7, 4, 3, 2, 1],
#         "query": 2
#     },
#     "output": 6
# }
#
#
def locate(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]
        print("lo: ", lo, " ,hi: ", hi, " ,mid: ", mid, " ,mid_number: ", mid_number)

        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid - 1
        elif mid_number > query:
            lo = mid + 1
    return -1


# evaluate_test_case(locate, test)


def locate_card_linear(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1


large_test = {
    "input": {
        "cards": list(range(10000000, 0, -1)),
        "query": 2
    },
    "output": 9999998
}

result, passed, runtime = evaluate_test_case(locate, large_test, display=False)

print(f"Result: {result} Passed: {passed} Runtime: {runtime}ms")


# def binary_search(lo, hi, condition):
#     # TODO: - add docs
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         result = condition(mid)
#         if result == 'found':
#             return mid
#         elif result == 'left':
#             hi = mid - 1
#         else:
#             lo = mid + 1
#     return -1
#
#
# def first_position(nums, target):
#     def condition(mid):
#         if nums[mid] == target:
#             if mid > 0 and nums[mid-1] == target:
#                 return 'left'
#             return 'found'
#         elif nums[mid] < target:
#             return 'right'
#         else:
#             return 'left'
#     return binary_search(0, len(nums)-1, condition)
#
#
# def last_position(nums, target):
#     def condition(mid):
#         if nums[mid] == target:
#             if mid < len(nums)-1 and nums[mid+1] == target:
#                 return 'right'
#             return 'found'
#         elif nums[mid] < target:
#             return 'right'
#         else:
#             return 'left'
#     return binary_search(0, len(nums)-1, condition)
#
#
# def first_and_last_position(nums, target):
#     return first_position(nums, target), last_position(nums, target)
