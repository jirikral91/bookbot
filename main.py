
# This function counts and returns words in the text
def count_words(text):
    # Split the text on whitespace and return the number of words.
    words = text.split()
    return len(words)


# This function counts and return number of each letter in the text
def count_characters(text):
    text = text.lower()
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1 # if character is already in counts, it increases its value by 1
        else:
            counts[char] = 1 # if character is not in counts yet, it is added with value 1
    return counts

def sort_on(item):
    # Vrací hodnotu pod klíčem "num" ze slovníku, používá se při třídění
    return item["num"]


# Report function will aggregate data and print each character by number of occurrences.
def print_report(text):
    # Count words and characters
    word_count = count_words(text)
    char_count = count_characters(text)

    # Filter only letter characters
    filtered_count = {}
    for char in char_count:
        if char.isalpha():
            filtered_count[char] = char_count[char]

    # New list of dictionaries with keys name and num.
    list_of_char = []
    for char in filtered_count:
        item = {"name": char, "num": filtered_count[char]}
        list_of_char.append(item)

    # Sorting the list of dictionaries.
    list_of_char.sort(key=sort_on, reverse=True)

    # Generating the report
    print("--- Begin report of books/frankenstein.txt ---")
    print(str(word_count) + " words found in the document\n")
    for item in list_of_char:
        print("The '" + item["name"] + "' character was found " + str(item["num"]) + " times")
    
    print("--- End report ---")

        


# THIS IS THE MAIN FUNCTION
def main():
    # Open the file at "books/frankenstein.txt"
    # (the file path is relative to where you run the program)
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    # Printing the results of report function.
    print_report(file_contents)

main()
