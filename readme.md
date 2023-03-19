## Bigrams and the Richness of the Stimulus

This project attempts to reproduce an experiment conducted by [Reali and Christiansen (2005)](https://onlinelibrary.wiley.com/doi/abs/10.1207/s15516709cog0000_28). The original paper is included in the repo for reference.  

### Motivation

Chomsky's _Poverty of the Stimulus_ (henceforth POS) thesis famously postulates that children are not exposed to sufficient linguistic data in their environments to be able to acquire every feature of the target langauge.  Consequently, langauge acquisition requires an alternative cognitive mechanisim (i.e. the universal grammar) in order for it to succeed.  Reali and Christiansen undermine the POS assumption by demonstrating that a simple statistical language model is sufficient to induce well-formed utterances, and that it can do so in spite of a lack of adequate amounts of linguistic data.  The authors illustrate their claim by investigating auxiliary inversion in English polar interrogatives containing subject-modifying relative clauses.

### Procedure

The experiment relies on the corpus spontaneous adult-child conversations by Bernstein-Ratner (available [here](https://childes.talkbank.org/data/Eng-NA/Bernstein.zip)).  `get_raw_data` iterates over the corpus isolating the utterances o adult speech directed to 13 through 21-month-old children and outputs them into a separate sub-corpus file (`raw_data.txt`).  The sub-corpus is then cleaned, normalized with `clean_data.py`, and output into a separate file (`normalized_data.txt`).  The latter is used by `evaluate.py` to develop a bigram language model with Knesser Ney interpolation.  The model is used to calculate the entropy of the 100 grammatical (`Bigrams_Richness_Experiment_1_grammatical.txt`) and ungrammatical (`Bigrams_Richness_Experiment_1_ungrammatical.txt`) utterance pairs.  The utterance with a lower entropy score is judged to be grammatical based on the language model.

### Outcome and Evaluation

The accuracy of the langauge model reported by Reali and Christiansen was 96%.  The accuracy reached by the current model is 88%, meaning that the model correctly evaluates 88 out of 100 utterance pairs.