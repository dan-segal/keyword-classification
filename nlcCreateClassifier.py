#This script trains a text classifer using Watson Natural Language Classifier (NLC).
#
#The input file should be in CSV format, with two columns: the text, and its assigned class.  For an example, see: https://watson-developer-cloud.github.io/doc-tutorial-downloads/natural-language-classifier/weather_data_train.csv
#
#The script requires a Watson NLC account.
#
#For full NLC documentation, including instructions for obtaining a Watson NLU account, see:  https://console.bluemix.net/docs/services/natural-language-classifier/getting-started.html#natural-language-classifier.


#!/usr/bin/env python
#!/usr/bin/env python3

import json
from watson_developer_cloud import NaturalLanguageClassifierV1

#Define user name
user_name = '{user name}'

#Define password
user_password = '{password}'

#Define input file
input_file = '{file path and name)}'

#Define the name of the classifier
classifier_name = '{classifier name}'

natural_language_classifier = NaturalLanguageClassifierV1(
  username=user_name,
  password=user_password)

with open(input_file, 'rb') as training_data:
  classifier = natural_language_classifier.create_classifier(
    training_data=training_data,
    # before Python SDK v1.0.0, name and language were top-level parameters
    metadata='{'name':clasifier_name,'language': 'en'}'
  )
print(json.dumps(classifier, indent=2))