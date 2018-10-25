# Keyword classification

This repository contains sample Python scripts for performing concept identification and text classification using Watson APIs.  These scripts are referenced in the prenstation "Applying NLP & Machine Learning to Keyword Analysis," delivered Nov. 7, 2018 at Text Analytics Forum.

Before using these scripts, install Watson Developer Cloud: *pip install --upgrade watson-developer-cloud*

## Identifying concepts ##

The script *nlu_concept-extraction_sample.py* extracts Concepts from a list of HTML pages using Watson Natural Language Understanding (NLU).

The input file should be in CSV with a minimum of two columns.  The column headers should include URL (for the URL of the page) and Keyword (for the search keyword that is associated with a URL).

The output is in JSON.

The script requires a Watson NLU account.

For full NLU documentation, including instructions for obtaining a Watson NLU account, see: *https://console.bluemix.net/docs/services/natural-language-understanding/getting-started.html#getting-started-tutorial*.

## Training the classifier ##

The script *nlcCreateClassifier.py* trains a text classifer using Watson Natural Language Classifier (NLC).

The input file should be in CSV format, with two columns: the text, and its assigned class.  For an example, see: *https://watson-developer-cloud.github.io/doc-tutorial-downloads/natural-language-classifier/weather_data_train.csv* . 

#The script requires a Watson NLC account.

For full NLC documentation, including instructions for obtaining a Watson NLU account, see:  *https://console.bluemix.net/docs/services/natural-language-classifier/getting-started.html#natural-language-classifier*.


## Classifying text ##
