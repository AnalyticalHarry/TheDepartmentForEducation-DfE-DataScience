#Importing random
import random

#List of five jokes
joke_1 = "A police officer caught two kids playing with a firework and a car battery. He charged one and let the other one off."
joke_2 = "What happens to a frog\"s car when it breaks down? It gets toad."
joke_3 = "Why are pirates called pirates? Because they arrr!"
joke_4 = "Why didn’t the orange win the race? It ran out of juice."
joke_4 = "My cat was just sick on the carpet, I don’t think it’s feline well."
joke_4 = "I really want to buy one of those supermarket checkout dividers, but the cashier keeps putting it back."
joke_5 = "What did one nut say as he chased another nut? I\'m a cashew!"

#storing five list of jokes in "jokes_list"
jokes_list = [joke_1, joke_2, joke_3, joke_4, joke_5]

# random choice from sequence and printing output
print(random.choice(jokes_list))