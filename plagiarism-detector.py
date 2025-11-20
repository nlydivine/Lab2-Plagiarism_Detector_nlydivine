#!/usr/bin/env python3

import string
import os

def clean(file_path):
    stop_words = {'a', 'an', 'the', 'is', 'in', 'of', 'on', 'and', 'to', 'for', 'at', 'by'}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read().lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = [w for w in text.split() if w not in stop_words]
        return words
    except FileNotFoundError:
        print("File not found:", file_path)
        return []

def find_word(word, list1, list2):
    count1 = list1.count(word)
    count2 = list2.count(word)
    print("\n'{}' appears {} times in essay1 and {} times in essay2.\n".format(word, count1, count2))

def common(list1, list2):
    c = set(list1) & set(list2)
    print("Common words ({}):".format(len(c)))
    if c:
        print(", ".join(sorted(c)))
    else:
        print("None found.")
    return c

def similarity(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    if not (set1 or set2):
        return 0
    inter = set1 & set2
    uni = set1 | set2
    return (len(inter) / len(uni)) * 100

def save(sim, common_words):
    os.makedirs("reports", exist_ok=True)
    path = "reports/similarity_report.txt"
    with open(path, 'w', encoding='utf-8') as f:
        f.write("Similarity: {:.2f}%\n".format(sim))
        f.write("Common words:\n")
        f.write(", ".join(sorted(common_words)))
    print("Report saved to", path)

def main():
    file1 = "essays/essay1.txt"
    file2 = "essays/essay2.txt"

    words1 = clean(file1)
    words2 = clean(file2)

    if not words1 or not words2:
        print("Missing or empty essay files. Exiting.")
        return

    print("\nEssays loaded successfully.\n")

    w = input("Enter a word to search for: ").lower()
    find_word(w, words1, words2)

    c_words = common(words1, words2)

    sim = similarity(words1, words2)
    print("\nPlagiarism similarity: {:.2f}%".format(sim))
    if sim >= 50:
        print("High similarity detected (possible plagiarism).")
    else:
        print("Acceptable similarity level.")

    save_choice = input("\nSave similarity report? (y/n): ").lower()
    if save_choice == 'y':
        save(sim, c_words)

if __name__ == "__main__":
    main()


