import random

items = ['candlestick', 'knife', 'cat toy', 'newspaper', 'rope', 'air fryer']

correct_item = random.choice(items)

while True:
    user_input = input("What item did Shirley hit Bob with in the art room?")
    if user_input == correct_item:
        print('you are right! you will continue to the next level')
        break
    else:
        print("try again :(")
