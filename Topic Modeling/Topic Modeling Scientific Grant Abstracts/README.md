# Topic Modeling Scientific Grant Abstracts
_______________________________________

## About

This set of notebooks were developed by Margaret Gratian and can be used to perform topic modeling on NIH scientific grant abstracts. The workflow is as follows: 

1. In Notebook 1, use code available in the reporter directory to request abstracts from the NIH RePORTER API.
2. In Notebook 2, use the sentence-transformers library and the PubMedBERT model to produce embeddings of the abstracts.
3. In Notebook 3, use the BERTopic library to reduce the dimensionality of the text embeddings, cluster the newly reduced dimension vectors, and assign representative labels describing the clusters.

## Installation Instructions

Please see the README file at the top level of the Topic Modeling folder for instructions. The requirements.txt file is also located at the top level of the Topic Modeling folder.