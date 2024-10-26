def main():
    book = "books/frankenstein.txt"
    with open(book) as f:
        contents = f.read()
        words = contents.split()
        characters = {}

        for w in words:
            for c in w:
                lc = c.lower()
                if lc not in characters:
                    characters[lc] = 0
                characters[lc] += 1

        print(f"--- Begin report of {book} ---")
        print(f"{len(words)} words found in the document")

        for k in characters:
            v = characters[k]
            print(f"The '{k}' character was found {v} times")

        print("--- End Report ---")

main()
