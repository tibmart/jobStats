import requests
import datetime
import time
import pandas
from bs4 import BeautifulSoup
import progressbar




def searchSeekCount(skill,location):
    page = requests.get(f"https://www.seek.com.au/{skill}-jobs/{location}")
    soup = BeautifulSoup(page.content, 'html.parser')
    jc= soup.find('strong', attrs={'data-automation': 'totalJobsCount'})
    #print(skill,' ',location,' -> ', jc.text)
    return jc.text

Locations=["in-All-Perth-WA","in-All-Brisbane-QLD","in-All-Canberra-ACT","in-All-Sydney-NSW","in-All-Melbourne-VIC","in-All-Adelaide-SA","in-All-Australia" ]
Skills=["AWS","Azure", "Docker","Kubernetes","Python","Powershell", "PHP","DevOps","SAP","Mulesoft","SQL"]

bar = progressbar.ProgressBar(maxval=len(Locations)*len(Skills), \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])


print(datetime.datetime.now())
allResults={}

bar.start()

barIndex=0
for loc in Locations:
    auxd={}
    for s in Skills:
        barIndex+=1
        bar.update(barIndex)
        auxd[s]=searchSeekCount(s,loc)
        time.sleep(2)
    allResults[loc]=auxd

bar.finish()

df=pandas.DataFrame(allResults)
print(df)



