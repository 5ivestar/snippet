import xml.etree.ElementTree as ET
import sys
import csv

'''
Create title and abstract text into csv files

title1, abstract1
title2, abstract2
...

1. Download jawiki-latest-abstract.xml.gz from https://dumps.wikimedia.org/jawiki/latest/
2. Execute the command below
python wiki_abstract_extractor.py jawiki-latest-abstract.xml.gz
3. result file is wiki_abs.csv
'''

tree=ET.ElementTree(file=sys.argv[0])
feed=tree.getroot()
count=0
with open("wiki_abs.csv","w",encoding="utf-8") as f:
    writer=csv.writer(f)
    for doc in feed:
        title=None
        for content in doc:
            if content.tag == "title":
                title=content.text[11:]
            if content.tag == "abstract":
                abstract=content.text
        if title is not None:
            docs=writer.writerow([title,abstract])
        if count%10000==0:
            print(str(count)+" docs loaded")
        count+=1
