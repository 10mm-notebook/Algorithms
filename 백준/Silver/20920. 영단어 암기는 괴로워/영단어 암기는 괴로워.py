import sys
n, m = map(int, sys.stdin.readline().split())
word_counts = {}

for _ in range(n):
    word = sys.stdin.readline().rstrip()
    if len(word) >= m:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

def get_sort_key(word):
    return (-word_counts[word], -len(word), word)

word_list = list(word_counts.keys())
word_list.sort(key=get_sort_key)

for word in word_list:
    print(word)