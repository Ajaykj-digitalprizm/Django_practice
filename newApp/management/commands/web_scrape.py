from django.core.management.base import BaseCommand
import requests
from ...models import Article
import time
import requests
from bs4 import BeautifulSoup

class Command(BaseCommand):

    help = 'Repeat task every 10 minute'

    def handle(self, *args, **kwargs):
        while True:

            print("im running")

            url = "https://news.ycombinator.com/newest"
            response = requests.get(url)

            if response.status_code != 200:
                print("Error fetching page")
                
            else:
                soup = BeautifulSoup(response.content, "html.parser")
                articles = soup.find_all('tr', class_='athing')
                for article in articles:
                    title_td = article.find_all('td', class_='title')
                    vote_id = article.get('id')
                    if title_td:
                        for title_span in title_td:
                            span = title_span.find_all('span', class_='titleline')
                            if span:
                                for title in span:
                                    title_text = title.find('a').text
                                    if vote_id:
                                        score_text = "score_"+ vote_id
                                        score = soup.find(class_="score", id=score_text).text
                                        point = int(score.split(" ")[0])
                                        Article.objects.create(title=title_text, vote_count = point)
            time.sleep(600)