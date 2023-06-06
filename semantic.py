# *** NOTE ON COMMENTS & own example ***
# The similarities between "cat," "monkey," and "banana" are interesting because they showcase how word embeddings capture semantic relationships. In this case, the model seems to capture a notion of animal categories and a connection between the monkey and the banana as a potential food source or association in some contexts.
# For example, when we examine the word vectors for these words using a language model like 'en_core_web_md,' we may observe that the vectors for "cat" and "monkey" are relatively closer to each other compared to the vector for "banana." This similarity implies a closer semantic relationship between "cat" and "monkey" than between either of them and "banana." This aligns with our understanding that cats and monkeys are both animals, while a banana is a fruit.
# Now, considering an example of my own, let's look at the words "car," "road," and "fuel." We might expect these words to exhibit certain similarities and relationships. A car requires fuel to operate, and it typically moves on a road. The word embeddings should reflect these connections by placing "car" and "road" closer together, while "fuel" might be slightly further away. By examining the vector representations of these words, we can gain insights into how the model captures their semantic relationships.
# Running the example file with the simpler language model 'en_core_web_sm,' we might notice some differences compared to the 'en_core_web_md' model. The 'en_core_web_sm' model is a smaller and lighter version of the language model, which means it may have a reduced vocabulary and less contextual information. Consequently, the 'en_core_web_sm' model might not capture as fine-grained nuances or exhibit the same level of accuracy in tasks like named entity recognition or entity linking compared to the 'en_core_web_md' model. However, it can still provide useful linguistic information and perform adequately in various natural language processing tasks, albeit with some limitations.


import spacy

nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
