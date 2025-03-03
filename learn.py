# Program to perform operations name:Glory

def count_vowels(name):
    """Function to count vowels in the given name."""
    vowels = "AEIOUaeiou"
    return sum(1 for char in name if char in vowels)

# Accepting user input for name and n value
name = input("Enter your name: ")
n = int(input
        ("Enter the number of characters to display from the left: "))

# Displaying first 'n' characters
first_n_chars = name[:n]

# Counting vowels
vowel_count = count_vowels(name)

# Reversing the name
reversed_name = name[::-1]

# Displaying the results
print(f"First {n} characters: {first_n_chars}")
print(f"Number of vowels: {vowel_count}")
print(f"Reversed name: {reversed_name}")