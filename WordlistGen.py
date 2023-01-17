from tqdm import tqdm
import itertools
import random
import string
import time
from termcolor import colored

words = ["Siddhu"]
symbols = list(string.punctuation)
numbers = list(string.digits)

min_length = int(input("Enter minimum length for the word including symbols: "))
max_length = int(input("Enter maximum length for the word including symbols: "))

# calculate total possible words
total_words = 0
for i in range(min_length, max_length+1):
    total_words += len(words) * (len(symbols) * len(numbers) ** min(6,i-len(words)))

with open("wordlist.txt", "w") as f:
    pbar = tqdm(total=total_words, desc="Generating words", bar_format="{l_bar}{bar}|{n_fmt}/{total_fmt}[{elapsed}<{remaining}]")
    for i in range(min_length, max_length+1):
        for symbol in symbols:
            number_combinations = [''.join(n) for n in itertools.product(numbers, repeat=min(6,i-len(words)))]
            word_symbol_combinations = [list(x) + [symbol + n] for x in itertools.product(words, repeat=1) for n in number_combinations]
            for combination in word_symbol_combinations:
                f.write("".join(combination)+'\n')
                pbar.update(1)
    pbar.close()
    print(colored("words saved in wordlist.txt file.", 'green'))

