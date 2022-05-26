#16.10 Exercises

# used in exercise 4
from collections import Counter
import collections

# 1 Create a dict, info, that holds your first and last name, as well as age.
info = {'first': 'Justice', 'last': 'Bole', 'age': 27}


# 2 Create an empty dict, phone, that will hold deets about your phone. Add screen size, mem, OS, bran, etc. to the dict
phone = {}
phone['screen_size'] = '6.1 inches (diagonal)'
phone['memory'] = '64GB'
phone['os'] = 'iOS 15'
phone['brand'] = 'Apple'
phone['model'] = 'iPhone XR'
print(phone)


# 3 Write a para in ''' strings. use .split to make a list of words. make a dict to hold the count for every word in the para
paragraph = '''
Paragraphs are the building blocks of papers. Many students define paragraphs in terms of length: a paragraph is a 
group of at least five sentences, a paragraph is half a page long, etc. In reality, though, the unity and coherence 
of ideas among sentences is what constitutes a paragraph. A paragraph is defined as “a group of sentences or a single 
sentence that forms a unit” (Lunsford and Connors 116). Length and appearance do not determine whether a section in a 
paper is a paragraph. For instance, in some styles of writing, particularly journalistic styles, a paragraph can be 
just one sentence long. Ultimately, a paragraph is a sentence or group of sentences that support one main idea. In 
this handout, we will refer to this as the “controlling idea,” because it controls what happens in the rest of the 
paragraph. '''

word_list = paragraph.split()
word_count = 0
for words in word_list:
    word_count += 1
print(word_count)


# 4 count how many times each word is used in a para from ralph waldo
waldo_paragraph = "I would not be hurried by any love of system, by any exaggeration of instincts, to underrate the Book. " \
            "We all know that as the human body can be nourished on any food, though it were boiled grass and the " \
            "broth of shoes, so the human mind can be fed by any knowledge. And great and heroic men have existed who " \
            "had almost no other information than by the printed page. I only would say that it needs a strong head " \
            "to bear that diet. One must be an inventor to read well. As the proverb says, \"He that would bring home " \
            "the wealth of the Indies must carry out the wealth of the Indies.\" There is then creative reading as " \
            "well as creative writing. When the mind is braced by labor and invention, the page of whatever book we " \
            "read becomes luminous with manifold allusion. Every sentence is doubly significant, and the sense of our " \
            "author is as broad as the world. We then see, what is always true, that as the seer's hour of vision is " \
            "short and rare among heavy days and months, so is its record, perchance, the least part of his volume. " \
            "The discerning will read, in his Plato[36] or Shakespeare, only that least part,—only the authentic " \
            "utterances of the oracle;—all the rest he rejects, were it never so many times Plato's and Shakespeare's. "

waldo_word_list = waldo_paragraph.split()
waldo_count = collections.Counter(waldo_word_list)
print(waldo_count)


# 5 print out the anagrams from a para of text **!#INCOMPLETE#!**
anagram_para = '''
Why would he race if he doesn't care ? To me it sounds like we're a part of his trap .'''

anagram_word_list = anagram_para.split()
print("step one", anagram_word_list)

for word in anagram_word_list:
    word_counted = collections.Counter(word)
    print(word_counted)

# 6 ?????




