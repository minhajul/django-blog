from django.shortcuts import render
from bs4 import BeautifulSoup
import urllib


# Create your views here.
def news_views(request):
    news = {}
    link = "http://en.prothom-alo.com/"
    page_link = urllib.urlopen(link)
    soup = BeautifulSoup(page_link, "html.parser")
    contents = soup.findAll('div', attrs = {'class': 'each_news'})

    for content in contents:
        title = content.findAll('h2', attrs = {'class': 'title'})[0].string
        news_summary = content.findAll('a', attrs = {'class': 'content_right'})[0].string
        new_news = {'title': title, 'news_summary': news_summary}
        news.update(new_news)

    return render(request, 'news.html', {'news': news})

