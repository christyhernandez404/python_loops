# Create a game where a player has a list of items. They have to guess which item in the list was selected. Use random.choice() to select the item and take the user's guess via input. Provide feedback on whether they guessed correctly or not keep them playing until they guess correctly
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
