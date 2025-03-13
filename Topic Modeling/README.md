# Topic Modeling Scientific Text
_______________________________________

## About

This folder contains two workflows for topic modeling scientific text: one for extracting and topic modeling scientific articles from PubMed and one for extracting and topic modeling NIH scientific grant abstracts from the NIH RePORTER API.

These workflows and code were developed by Margaret Gratian. 

## Installation Instructions 

To use either of these two workflows, you will need to install packages listed in the requirements.txt file in addition to the PubMed e-utilities command line tool. If you are not planning to extract data from PubMed, you can ignore the last command in the instructions below.

We recommend creating a virtual environment and using Python 3.10. The following instructions will help you set up a virtual conda environment and install the required packages. 

    `conda create -n topic_modeling_env python=3.10`

    `conda activate topic_modeling_env`

    `pip install -r requirements.txt`

    `sh -c "$(curl -fsSL https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/install-edirect.sh)"`