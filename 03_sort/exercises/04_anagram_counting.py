from collections import defaultdict


def count_anagrams(word, dictionary):
    sorted_word = ''.join(sorted(word))
    return dictionary[sorted_word]


N, *words = input().split()
word_counts = defaultdict(int)
for word in words:
    sorted_word = ''.join(sorted(word))
    word_counts[sorted_word] += 1
sorted_words = sorted(word_counts.keys())
output = []
for sorted_word in sorted_words:
    word = next((w for w in words if ''.join(sorted(w)) == sorted_word), None)
    count = word_counts[sorted_word]
    output.append(f"{word} {count}")
output.sort()
print('  '.join(output))
