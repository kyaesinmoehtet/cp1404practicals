def main():
    text = input("Text: ")
    word_counts = {}
    words = text.split()
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    max_length = max(len(word) for word in word_counts)
    for word in sorted(word_counts):
        print(f"{word:{max_length}} : {word_counts[word]}")

if __name__ == "__main__":
    main()