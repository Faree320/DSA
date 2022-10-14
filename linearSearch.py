from jovian.pythondsa import evaluate_test_case

# Brute For solution
test = {
    "input": {
        "cards": [13, 11, 10, 7, 4, 3, 2, 1],
        "query": 1
    },
    "output": 7
}


def locate_card(cards, query):
    position = 0

    while True:
        if cards[position] == query:
            return position

        position += 1

        if cards[position] == len(cards):
            return -1


# result = locate_card(test['input']['cards'], test['input']['query'])
# print(result)
#
# print(result == test['output'])
evaluate_test_case(locate_card, test)


