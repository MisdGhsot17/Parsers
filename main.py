import re
import requests
from bs4 import BeautifulSoup



# with open('asasas.html', encoding='utf-8') as f:
# src = f.read()
# print(src)

#title = soup.title
games = []
page = 0

while page != 83:
        response = requests.get("https://stopgame.ru/games?p=" + str(page))
        soup = BeautifulSoup(response.content, 'html.parser')
        games_list = soup.find_all('div', class_='caption caption-bold')
        with open('parser.games', 'a', encoding='utf-8') as f:
                for e in games_list:
                        a = e.text.strip()
                        f.writelines(f'{a}\n')
        page+=1

# print(title) #выводит с тегом <></>
# print(title.text) #выводит просто текст title без тега
# print(title.string)

# .find() .find_all()

# page_h1 = soup.find_all('h1')
# print(page_h1)

# for e in page_h1:
# print(e.text)

# user_div_name = soup.find_all('div', class_="user__name")
# print(user_div_name)

# for e in user_div_name:
# print(e.text)

# user_name = soup.find(class_="user__name").find('span').text
# print(user_name)

# user_name = soup.find('div', {'class': 'user__name', 'id': 'aaa'}).find("span").text
# print(user_name)

# user_info = soup.find(class_="user__info").find_all('span')
# print(user_info)

#for item in user_info:
# print(item.text)

# print(user_info[0].text)


# social_networks = soup.find(class_='social__networks').find('ul').find_all('a')
# print(social_networks)

# for item in social_networks:
# print(item.text)

# all_a = soup.find_all('a')
# print(all_a)

# for item in all_a:
# item_text = item.text
# item_url = item.get('href')
# print(f'{item_text}:{item_url}')

# .find_parent() .find_parents()

# post_div = soup.find(class_='post__text').find_parent('div', 'user__post')
# print(post_div)

# post_div = soup.find(class_='post__text').find_parents('div', 'container')
# print(post_div)

# .next_element .previous_element

# next_el = soup.find(class_='post__title').next_element.next_element.text
# print(next_el)

# next_el = soup.find(class_='post__title').find_next().text
# print(next_el)

# .find_next_sibling().find_previous_sibling()
# next_sib = soup.find(class_='post__title').find_next_sibling()
# print(next_sib)

# prev_sib = soup.find(class_='post__title').find_previous_sibling()
# print(prev_sib)

# post_title = soup.find(class_='post__date').find_previous_sibling().find_next().text
# print(post_title)

# links = soup.find(class_='some__links').find_all('a')
# print(links)

# for link in links:

# link_href = link.get('href')
# link_href_attr1 = link['href']

# link_data_attr = link.get('data-attr')
# link_data_attr1 = link['data-attr']

# print(link_data_attr)
# print(link_href)

# print(link_data_attr1)
# print(link_href_attr1)

# find_by_text = soup.find('a', text='Одежда').text
# print(find_by_text)

# find_by_text = soup.find('a', text=re.compile('Одежд')).text
# print(find_by_text)

# find_by_text = soup.find('a', text=re.compile('Одежда')).text
# print(find_by_text)

# find_by_text = soup.find(text=re.compile("([Оо]дежда)"))
# print(find_by_text)
