words_list = ['bat', 'rats', 'god', 'dog', 'cat',
              'arts', 'star', 'acres', 'cares',
              'races', 'scare', 'alert', 'alter',
              'later', 'lab', 'lag', 'nod', 'aligned',
              'dealing', 'leading', 'banana']

anagrams = set()
anagrams_dict = {}

for word in words_list:
    sorted_word = "".join(sorted(word))
    print("\n Word: {0}, Sorted word: {1}".format(word, sorted_word))

    if sorted_word in anagrams_dict:
        anagrams_dict[sorted_word].add(word)
        print("Added word: {0}, to dictionary: {1}".format(word, sorted_word))
    else:
        anagrams_dict[sorted_word] = set([word])
        print("Created dictionary: {0} and added word: {1}".format(sorted_word, word))

for words_in_dict in anagrams_dict.values():
    if len(words_in_dict) < 2:
        print("Discarding: {0}".format(words_in_dict))
        continue

    print("Adding words to the anagrams set: {0}".format(words_in_dict))
    anagrams = anagrams.union(words_in_dict)

print("\nThere are: {0} anagrams:\n{1}".format(len(anagrams), anagrams))
