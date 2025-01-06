def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        print("Word count:", get_word_count(file_contents))

def get_word_count(text):
    return len(text.split())

main()