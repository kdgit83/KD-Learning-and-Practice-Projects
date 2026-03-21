def sort_words(words: str) -> str:
    return ' '.join(sorted(words.split(), key=str.casefold))

    # words = [word.lower() + word for word in words.split()]
    # words.sort()
    # words = [word[len(word) // 2:] for word in words]
    # return ' '.join(words)


# commands used in solution video for reference
if __name__ == '__main__':
    print(sort_words('banana ORANGE apple'))  # apple banana ORANGE
