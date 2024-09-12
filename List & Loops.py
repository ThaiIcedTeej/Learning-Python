buying = ["apple", "banana", "strawberry", "pineapple"]
prices = {
    "apple": 3,
    "banana": 2,
    "strawberry": 5,
    "pineapple": 1,
}

def checkout(fruits): #2 receives parameter of buying which is a list
    cost = 0

    for item in fruits: #3 item starts at 0 which is receives apple
        if item in prices: #4 starts with 0 and sees apple in prices first
            cost += prices[item] #5 adds 3 because it received the key apple which was assign value 3 in the variable
        else:
            print("item does not exist")

    return cost

print(checkout(buying)) #1 sending buying list into checkout parameter
