# Topic Modeling Scientific Articles
_______________________________________

## About

This set of notebooks were developed by Margaret Gratian and can be used to perform topic modeling on scientific articles. The workflow is as follows: 

1. In Notebook 1, use the PubMed entrez command line tools to search for and download scientific publication titles and abstracts in PubMed.
2. In Notebook 2, use the biopython library to format the raw PubMed text into a table.
3. In Notebook 3, use the sentence-transformers library and the SPECTER Transformer-based embedding model from the Allen Institute for AI to produce embeddings of the titles and abstracts.
4. In Notebook 4, use the BERTopic library to reduce the dimensionality of the text embeddings, cluster the newly reduced dimension vectors, and assign representative labels describing the clusters.

## Installation Instructions

Please see the README file at the top level of the Topic Modeling folder for instructions. The requirements.txt file is also located at the top level of the Topic Modeling folder.