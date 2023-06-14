from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.
def index(request):
    url = "https://www.businesstoday.in/technology/news"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')

    finalNews=""
    for data in soup.find_all("div",class_="widget-listing",limit=6):
        news=data.div.div.a["title"]
        finalNews += '\u2022 '+news+'\n'
    
    context = {"News":finalNews}
    return render(request,'index.html',context)
