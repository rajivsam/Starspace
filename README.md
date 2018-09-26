### Starspace Embeddings for Online Retail


This repository contains the code for the embeddings associated with the items in the online retail dataset (UCI ML repository: https://archive.ics.uci.edu/ml/datasets/online+retail). The pre-processing was done with the script preprocessing_cust_trans.ipynb. Embedding was done with starspace using:

./starspace train -trainFile ./data/Online_Retail_pp.txt -model pagespace -label 'item_code_' -trainMode 1

This is per guidelines provided in https://github.com/facebookresearch/StarSpace. Training was fairly quick. The generated embedings are in pagespace.tsv. A sample of the embeddings were visualized with tSNE (sklearn). This implementation is in Embedding_Visualization.ipynb

