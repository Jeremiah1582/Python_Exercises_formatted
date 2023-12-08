import json
import pandas
import re 
import os

dataPath = './data.txt'
allExercises=[]

def formatData(path):
    try:
        os.path.exists(path)
        with open(path, 'r+') as f: 
            print(f) # class _io.TextIOWrapper
            # convert file to string 
            # use regex to locate content & save to variables
            content = f.read()
            block = re.split('\n\n', content)
            
            for text in block:
                
                link= re.findall(r'(https:\/\/classroom\.github\.com\/a\/[^\n]+\n*)+', text)
                
                name= re.search(r'[A-Z][a-z]+(?:\s[A-Z][a-z]+)*(?=\n)',text).group()
                
                assignment_name= re.findall(r'(?:Assignment|Topic):\s*(.*?)(?=https|:white_check_mark:)', text)       
                
                time= re.search(r'\d{1,2}:\d{2}\s(?:AM|PM)',text).group()
                
                day= re.search(r'\b([1-9]|[12][0-9]|3[01])(st|nd|rd|th)\b', text).group()
            
                month = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)',text).group()
                
                dataCard= {
                    'date_uploaded': f'{day} {month} 2023',
                    'time_of_upload': time,
                    'uploaded_by': name, 
                    'assignment_name': assignment_name,
                    'links_to_exercise': {f'link{i+1}':val for i,val in enumerate(link)}
                }
                
                allExercises.append(dataCard)
                
    except AttributeError: 
        print('unable to find relevant data in text') 
        
    finally: 
        print('action complete')

        # print(len(links))
formatData(dataPath)
    
with open('allExercises.json', 'w') as f: 
    json.dump(allExercises, f, indent=4)

