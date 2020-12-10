import telebot
import requests
from bs4 import BeautifulSoup as BeautifulSoup



# token='1465331760:AAG5nIfTxfAxttgTm1IGt3ki0ntgcnUP0t8'
# bot=telebot.TeleBot(token)
# chat_id='1465331760'
#
# url = 'https://vk.com/kvantorium62'
# page = requests.get(url)
# html = BS(page.content, 'html.parser')
#
# for el in html.select('#group_wall ._post'):
#     if (el.select('.post_header .author')):
#         title = el.select('.post_header .author')[0].text
#         image = el.select('.post_image')
#
#         post = el.select('.wall_post_text')[0]
#         for tag in post.findAll('a'):
#             if (tag.text[0] == '#'):
#                 tag.extract()
#
# bot.polling(none_stop=True)

token='1465331760:AAG5nIfTxfAxttgTm1IGt3ki0ntgcnUP0t8'
bot=telebot.TeleBot(token)
chat_id='1465331760'

def parse(message):
    #url = 'https://stopgame.ru/news#more/'
    url = 'https://vk.com/kvantorium62'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    response = requests.get(url, headers = headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    #items = soup.findAll('div', class_ = 'article-description')
    items = soup.findAll('div', class_='wall_text')
    comps = []

    for item in items:
        comps.append({
            'title': item.find('div', class_ = 'wall_post_text').get_text(strip = True),
            'picture': item.find('a', class_ ="page_post_thumb_wrap image_cover  page_post_thumb_last_column page_post_thumb_last_row")
            #'title': item.find('a').get_text(strip=True)

        })
        global comp
        for comp in comps:
             print(comp['title'])
            # print('f'{comp["title"], {comp["time"]})

parse()

bot.send_message(message.from_user.id, comps, parse_mode='html')
