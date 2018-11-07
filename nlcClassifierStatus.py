#This script returns the status of a text classifer in Watson Natural Language Classifier (NLC).
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

#Define password
user_password = '{password}'

#Define user name
user_name = '{user name}'

classifier_id = '{classifier ID}'

natural_language_classifier = NaturalLanguageClassifier(
  username = user_name ,
  password = user_password)

status = natural_language_classifier.get_classifier(classifier_id)
print (json.dumps(status, indent=2))