# Keyword classification

This repository contains sample Python scripts for performing concept identification and text classification using Watson APIs.  These scripts are referenced in the prenstation "Applying NLP & Machine Learning to Keyword Analysis," delivered Nov. 7, 2018 at Text Analytics Forum.

Before using these scripts, install Watson Developer Cloud: *pip install --upgrade watson-developer-cloud*

## Identifying concepts ##

The script *nlu_concept-extraction_sample.py* extracts Concepts from a list of HTML pages using Watson Natural Language Understanding (NLU).

The input file should be in CSV with a minimum of two columns.  The column headers should include URL (for the URL of the page) and Keyword (for the search keyword that is associated with a URL).

The output is in JSON.

This script requires a Watson NLU account.

For full NLU documentation, including instructions for obtaining a Watson NLU account, see: *https://console.bluemix.net/docs/services/natural-language-understanding/getting-started.html#getting-started-tutorial*.

## Training the classifier ##

The script *nlcCreateClassifier.py* trains a text classifer using Watson Natural Language Classifier (NLC).

The input file should be in CSV format, with two columns: the text, and its assigned class.  For an example, see: *https://watson-developer-cloud.github.io/doc-tutorial-downloads/natural-language-classifier/weather_data_train.csv* . 

This script requires a Watson NLC account.

For full NLC documentation, including instructions for obtaining a Watson NLU account, see:  *https://console.bluemix.net/docs/services/natural-language-classifier/getting-started.html#natural-language-classifier*.

## Checking the status of a classifier ##

This script *nlcClassifierStatus.py* returns the status of a text classifer in Watson Natural Language Classifier (NLC).

This script requires a Watson NLC account.

It also requires the classsifer ID.   The classifier ID is assigned during the training step. If the classifier ID is not known, it can be found using the script *nlcListClassifiers.py* below.

For full NLC documentation, including instructions for obtaining a Watson NLU account, see:  https://console.bluemix.net/docs/services/natural-language-classifier/getting-started.html#natural-language-classifier.

## Classifying text ##

The script *nlcClassify.py* reads a flat list of keywords from the CSV file, passes the keywords to Watson Natural Language Classifier (NLC), and writes the NLC output to JSON.

#The column in the CSV file that contains the keywords must have "Keyword" as the header.

#Before running the script, update:

- The version of the Watson NLC classifier
- The name or the CSV input file - MUST BE ENCODED IN UTF-8 FORMAT
- The name of the JSON output file

This script requires a Watson NLC account.

It also requires the classsifer ID.   The classifier ID is assigned during the training step.  If the classifier ID is not known, it can be found using the script *nlcListClassifiers.py* below.

For full NLC documentation, including instructions for obtaining a Watson NLU account, see:  https://console.bluemix.net/docs/services/natural-language-classifier/getting-started.html#natural-language-classifier.

## List classifiers ##

The script *nlcListClassifiers.py* returns a list of text classifers that are associated with an account in Watson Natural Language Classifier (NLC).

The script requires a Watson NLC account.

For full NLC documentation, including instructions for obtaining a Watson NLU account, see:  https://console.bluemix.net/docs/services/natural-language-classifier/getting-started.html#natural-language-classifier.

## Deleting a classifier ##

