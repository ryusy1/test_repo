def word_count(text):
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


if __name__ == "__main__":
    print(word_count("hello python hello"))
