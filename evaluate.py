#!/usr/bin/env python
"""A script that evaluates the wellformedness of interrogative expressions based on a bigram language model.
The language model is based on caregivers' utterances extracted from the CHILDES corpus."""


from nltk.lm import KneserNeyInterpolated
from nltk.lm.preprocessing import pad_both_ends, padded_everygram_pipeline
from nltk.util import bigrams

train_corpus = "normalized_data.txt"
grammatical = "Bigrams_Richness_Experiment_1_grammatical.txt"
ungrammatical = "Bigrams_Richness_Experiment_1_ungrammatical.txt"


def get_data(path: str) -> list:
    """reads the data into a list of strings"""
    list_of_lines = []
    with open(path, "r") as source:
        for line in source:
            if not line:
                continue
            else:
                list_of_lines.append(line.lstrip().rstrip())
    return list_of_lines


def bigrammize(path: str) -> list:
    """converts a text file into bigrams. Each utterance line is a list of bigram tuples."""
    bigrammized = []
    data = get_data(path)
    for line in data:
        normalized = line[:-1].casefold()
        bigrammed = list(bigrams(pad_both_ends(normalized.split(), n=2)))
        bigrammized.append(bigrammed)
    return bigrammized


def main() -> None:
    corpus_data = get_data(train_corpus)  # returns a list of utterance strings
    split_corpus = [
        utterance.split() for utterance in corpus_data
    ]  # returns a list of split utterance lists
    train, vocab = padded_everygram_pipeline(
        2, split_corpus
    )  # returns lazy iterators for bigram counts and vocabulary set
    lm = KneserNeyInterpolated(order=2)  # sets up the language model
    lm.fit(train, vocab)  # fits the language model
    bigrammized_grammatical = bigrammize(grammatical)
    bigrammized_ungrammatical = bigrammize(ungrammatical)
    incorrect = 0  # sets up a counter for incorrectly labeled sentences
    for i in range(len(bigrammized_grammatical) - 1):
        if lm.entropy(bigrammized_grammatical[i]) > lm.entropy(
            bigrammized_ungrammatical[i]
        ):
            incorrect += 1
    accuracy = (len(bigrammized_grammatical) - incorrect) / 100
    print(f"The accuracy score: {accuracy:.2%} ")


if __name__ == "__main__":
    main()
