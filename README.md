# Wordlist-Generation-for-Efficient-Password-Cracking

This is a simple yet powerful python script that generates a wordlist of all possible combinations of words, symbols, and numbers, within a specified minimum and maximum length. The generated wordlist can be used for various purposes such as password cracking, penetration testing, and other security-related tasks. This script is designed to be efficient, customizable and user-friendly.

# Features
Generates all possible combinations of words, symbols, and numbers within a specified length range
Customizable list of words, symbols, and numbers
Uses the "tqdm" library to display a progress bar, providing an estimate of the time remaining for completion
Uses "termcolor" library to display a message in green when the words have been saved to a file called "wordlist.txt"
User-friendly, easy to use and understand

# Requirements
Python 3
tqdm
termcolor
Installation

  Before you can use this script, you will need to have Python 3 and the following libraries installed: tqdm and termcolor. You can install these libraries by running the following command in your terminal:

    pip install tqdm termcolor

# Usage
  To use the script, navigate to the directory where the script is located and run the following command:

    python wordlist_generator.py
    
  You will be prompted to enter the minimum and maximum length for the words in the wordlist. The script will then generate all possible combinations of words, symbols, and numbers within that length range and save them to a file called "wordlist.txt" in the same directory.

# Customization

  The script comes with a default list of words, symbols, and numbers. However, you can easily customize these lists by editing the words, symbols, and numbers variables in the script.

For example, to add a new word to the list, simply add it to the words variable like this:

    words = ["Siddhu","newword"]

Similarly, you can add or remove symbols and numbers from the symbols and numbers variables.

# Note

  This script is for educational and research purposes only. Please use this script ethically and in compliance with all applicable laws. The author is not responsible for any misuse of this script. It is the user's responsibility to ensure compliance with all laws and regulations before using this script.

# Contribution
  
  This script is open-source and welcomes contributions from the community. If you have any suggestions or improvements, please feel free to create a pull request.

# Conclusion
  The Wordlist Generator script is a useful tool for security professionals and researchers, providing an easy way to generate a comprehensive list of possible combinations of words, symbols, and numbers. With its customization options and user-friendly interface, it can be used to test the strength of passwords, identify vulnerabilities in systems, and perform other security-related tasks.
