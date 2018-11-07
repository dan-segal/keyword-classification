#This script reads a flat list of keywords from the CSV file, passes the keywords to Watson Natural Language Classifier (NLC), and writes the NLC output to JSON.
#
#The column in the CSV file that contains the keywords must have "Keyword" as the header.  The header name is case-sensitive.
#
#Before running the script, update:
#
#1) the version of the Watson NLC classifier
#2) the name or the CSV input file - MUST BE ENCODED IN UTF-8 FORMAT
#3) the name of the JSON output file

#This script requires a Watson NLC account.

#It also requires the classsifer ID.   The classifier ID is assigned during the training step.

#For full NLC documentation, including instructions for obtaining a Watson NLU account, see:  https://console.bluemix.net/docs/services/natural-language-classifier/getting-started.html#natural-language-classifier.

#!/usr/bin/env python
#!/usr/bin/env python3

import json
import csv
import io
from watson_developer_cloud import NaturalLanguageClassifierV1

#Define user name
user_name = '{user name}'

#Define password
user_password = '{password}'

#Define the classifier ID
classifier_id = '{classifier ID}'

#The path and name of the input file.  The input file must be in CSV format.
input_file = '{file path and name}'

#The path and name of the output file.  The output file must have the extension .json
output_file = '{file path and name}'

natural_language_classifier = NaturalLanguageClassifierV1(
  username = user_name,
  password = user_password )


#Open the read-from file.
reader = csv.DictReader(open(input_file))

#Open the write-to file.
with io.open(output_file,'w',encoding='utf8') as classification_results:  
    
    for row in reader:            
         
        #Make multiple attempts to process input.  If system returns an error, then esacpe and go to the next row.    
        for i in range(0,10):
            
            try:
                keyword = row['Keyword']
                classes = natural_language_classifier.classify(classifier_id, keyword)
                
                #Print output to screen
                print(json.dumps(classes, indent=2))
                
                #Write output to .json file
                classification_results.write(json.dumps(classes, indent=2))
                
                break
                
            except TypeError:
                pass
        
        
    
                

            
        