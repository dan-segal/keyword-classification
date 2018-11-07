#This script deletes a text classifer that is associated with an account in Watson Natural Language Classifier (NLC).
#
#The script requires a Watson NLC account.
#
#It also requires the classsifer ID.   The classifier ID is assigned during the training step.
#
#For full NLC documentation, including instructions for obtaining a Watson NLU account, see:  https://console.bluemix.net/docs/services/natural-language-classifier/getting-started.html#natural-language-classifier.


#!/usr/bin/env python
#!/usr/bin/env python3

import json
from watson_developer_cloud import NaturalLanguageClassifierV1 as NaturalLanguageClassifier

#Define user name
user_name = '{user name}'

#Define password
user_password = '{password}'

#Define the classifier ID
classifier_id = '{classifier ID}'

natural_language_classifier = NaturalLanguageClassifierV1(
  username=user_name,
  password=user_password)

status = natural_language_classifier.delete_classifier(classifier_id).get_result()

#Print output to screen
print(json.dumps(classifiers, indent=2))