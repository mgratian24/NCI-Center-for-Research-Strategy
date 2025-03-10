# Topic Modeling Scientific Text
_______________________________________

## About

This set of notebooks were developed by Margaret Gratian and can be used to perform topic modeling on scientific text. The workflow is as follows: 

1. In Notebook 1, use the PubMed entrez command line tools to search for and download scientific publication titles and abstracts in PubMed.
2. In Notebook 2, use the biopython library to format the raw PubMed text into a table.
3. In Notebook 3, use the sentence-transformers library and the SPECTER Transformer-based embedding model from the Allen Institute for AI to produce embeddings of the titles and abstracts.
4. In Notebook 4, use the BERTopic library to reduce the dimensionality of the text embeddings, cluster the newly reduced dimension vectors, and assign representative labels describing the clusters.


## Installation Instructions 

We recommend creating a virtual environment and using Python 3.10. The following instructions will help you set up a virtual conda environment and install the required packages. 

    `conda create -n topic_modeling_env python=3.10`

    `conda activate topic_modeling_env`

    `pip install -r requirements.txt`

    `sh -c "$(curl -fsSL https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/install-edirect.sh)"`