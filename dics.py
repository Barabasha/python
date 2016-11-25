dic = {'c': 2, 'a': 3, 'b': 1}
epmty_dict = {}
empty_dict2 = dict()
d1 = dict(id=1948, name="Washer", size=3)
d2 = {"id": 1948, "name": "Washer", "size": 3}
list = ['a','a','a','b','b','b']

print 'add pair key-value'
dic['d'] = 5
print dic

# comprehension
symbols = {chr(code): 0 for code in range(ord("a"), ord("z"))}

# printing
print 'print key - value pairs'
for key in dic:
    print key, dic[key]

print 'sorted by keys'
for key in sorted(dic):
    print key, dic[key]

print 'sorted by values'
for key in sorted(dic, key=dic.get):# reverse=True):
    print key, dic[key]

# grouping
print 'grouping (accumulating) values by keys'
dic_accum = {}
for element in list:
    if element in dic_accum:
        dic_accum[element] += 1
    else:
        dic_accum[element] = 1
print dic_accum


# advanced
######################################################
def print_top_n_words(filename, top_n):
    f = open(filename)
    words_list = f.read().split()
    print (len(words_list))
    words_freq = {}
    for word in words_list:
        if word[:1].isupper():
            words_freq[word] = words_freq.get(word, 0) + 1

    print (len(words_freq))
    for key in sorted(words_freq, reverse=True, key=words_freq.get)[:top_n]:
        print ("%-20s -> %d" % (key, words_freq[key]))
    f.close()


######################################################
def print_top_ngrams(filename):
    import string

    f = open(filename)
    words_list = f.read().split()
    print (len(words_list))
    words_freq = {}
    symb_dict = {}
    _ngram_freq = {}
    words = []
    limit = 4

    # skip_words = ["the", "to", "in", "on", "of", "by", "in", "from", "with", "no"
    # "he", "she", "and", "it", "was", "a", "said", "be", "would", "have", "had", "been", 
    # "were", "i", "as", "that", "this", "are", "at", "do", "not", "is", "her", "if", "i"]

    skip_words = [ 'в', 'время', 'же', 'бы', 'было', 'ни', 'то', 'более', 'всё', 'и',
     'в', 'же', 'но', 'то', 'до', 'не', 'пор', 'сих', 'ж', 'ну', 'так', 'что',
     'всё', 'это', 'к', 'а', 'вместе', 'с', 'тем', 'и', 'не', 'он', 'сам', 'до',
     'же', 'что', 'он', '']

    for word in words_list:
        word = word.lower().strip(",. !?:'\"-")
        if word not in skip_words:
            if len(words) == limit:
                words.pop(0)
            words.append(word)
            _ngram = tuple(sorted(words))
            _ngram_freq[_ngram] = _ngram_freq.get(_ngram, 0) + 1

    for key in sorted(_ngram_freq, reverse=True, key=_ngram_freq.get)[:20]:
        print("%s: %d" % (key, _ngram_freq[key]))

