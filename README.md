# Keyword classification

This repository contains sample Python scripts for performing concept identification and text classification using Watson APIs.  These scripts are referenced in the prenstation "Applying NLP & Machine Learning to Keyword Analysis," delivered Nov. 7, 2018 at Text Analytics Forum.

Before using these scripts, install Watson Developer Cloud:
- pip install --upgrade watson-developer-cloud 

This script extracts Concepts from a list of HTML pages using Watson Natural Language Understanding (NLU).

The script requires a Watson NLU account.

The input file should be in CSV with a minimum of two columns.  The column headers should include URL (for the URL of the page) and Keyword (for the search keyword that is associated with a URL).

_For full NLU documentation, see https://console.bluemix.net/docs/services/natural-language-understanding/getting-started.html#getting-started-tutorial.
