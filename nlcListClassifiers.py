#This script returns a list of text classifers that are associated with an account in Watson Natural Language Classifier (NLC).
#
#The script requires a Watson NLC account.
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

natural_language_classifier = NaturalLanguageClassifierV1(
  username=user_name,
  password=user_password)

classifiers = natural_language_classifier.list_classifiers().get_result()

#Print output to screen
print(json.dumps(classifiers, indent=2))