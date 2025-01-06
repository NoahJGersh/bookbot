def main():
    generate_report("books/frankenstein.txt")

def get_word_count(text):
    return len(text.split())

def get_character_counts(text):
    lowercase = text.lower()
    character_counts = {}

    for c in lowercase:
        if not c in character_counts:
            character_counts[c] = 1
        else:
            character_counts[c] += 1

    return character_counts

# Function for sorting character counts
def sort_on(dict):
    return dict["count"]

def generate_report(filepath):
    print(f"--- Begin report of {filepath} ---")
    
    with open(filepath) as f:
        file_contents = f.read()
        # print(file_contents)
        # print("Word count:", get_word_count(file_contents))
        # print("Unique characters:", get_character_counts(file_contents))

        print(f"{get_word_count(file_contents)} words found in the document\n")

        character_counts = get_character_counts(file_contents)
        sorted_character_counts = []
        for character in character_counts:
            if character.isalpha():
                sorted_character_counts.append({
                    "name": character, 
                    "count": character_counts[character]
                })

        sorted_character_counts.sort(reverse=True, key=sort_on)
        for character in sorted_character_counts:
            print(f"The '{character["name"]}' character was found {character["count"]} times")

    print("--- End report ---")

main()