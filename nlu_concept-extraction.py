#This script extracts Concepts from a list of HTML pages using Watson Natural Language Understanding (NLU).
#
#The input file should be in CSV with a minimum of three columns.  The column headers should include the names URL (for the URL of the page), Keyword (for the search keyword that is associated with a URL), and Query volume (for the number of queries).  Note that header names are case-sensitive.
#
#The output is in JSON.
#
#The script requires a Watson NLU account.
#
#For full NLU documentation, including instructions for obtaining a Watson NLU account, see https://console.bluemix.net/docs/services/natural-language-understanding/getting-started.html#getting-started-tutorial.

#!/usr/bin/env python
#!/usr/bin/env python3

import json
import csv
import io
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, ConceptsOptions

#Enter credentials and NLU version info.  Check the NLU documentation to confirm the current version number.
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-03-16',
    username='{user name}',
    password='{password}'
)

#File names

#The path and name of the input file.  The input file must be in CSV format.
input_file = '{file path and file name}'

#The path and name of the output file.  The output file must have the extension .json
output_file = '{file path and file name}'

#Open the read-from file.
reader = csv.DictReader(open(input_file))

#Open the write-to file.
with io.open(output_file,'w',encoding='utf8') as extraction_results: 

    for row in reader:
    
            #Make multiple attempts to process input.  If system returns an error, then esacpe and go to the next row.
            for i in range(0,5):
            
                try:
                    url = row ['URL']
                    keyword = row ['Keyword']
                    query_volume = row ['Query volume']
                    response = natural_language_understanding.analyze(
                        url=url,
                      features=Features(
                        concepts=ConceptsOptions(limit=10)),
                        return_analyzed_text=False)

                    output = {'keyword':keyword,'query volume':query_volume,'response':response }
                        
                    #Print output to screen
                    print(json.dumps(output, indent=2))
                    
                    #Write output to .json file
                    extraction_results.write(json.dumps(output, indent=2))
                    break
                    
                except:
                    pass
                
                

