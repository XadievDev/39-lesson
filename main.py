#XadievDev
#39-lesson.PIP. Tashqi kutubxona.

#----------------------------------------------------------------------------------------------#

# from googletrans import Translator

# tarjimon = Translator() # Translator bu maxsus klass (tarjimon esa obyekt)
# matn_uz = "Salom,mening ismim Amirbek.Men dasturlashga qiziqaman va doimiy kod yozib turaman."
# tarjima = tarjimon.translate(matn_uz)
# tarjima_ru = tarjimon.translate(matn_uz,dest='ru')
# print(tarjima_ru.text)
# print(tarjima.origin)
# print(tarjima.text)
# print(tarjima.src)

#----------------------------------------------------------------------------------------------#

# tarjimon = Translator()
# matn_en = 'Tashkent is the capital of Uzbekistan.'
# tarjima_uz = tarjimon.translate(matn_en,dest='uz')
# print(tarjima_uz.text) 

#----------------------------------------------------------------------------------------------#

# from googletrans import Translator

# tarjimon = Translator()
# msg = "Tarjima uchun math kiriting('q'-chiqish):"

# while True:
#     text = input(msg)
#     if text == 'q':
#         print('Dastur tugadi.')
#         break
#     else:
#         tarjima = tarjimon.translate(text, src='uz', dest='en')
#         print(tarjima.text)

#----------------------------------------------------------------------------------------------#

# import requests
# from pprint import pprint

# manzil= "https://kundalik.com/userfeed"
# r = requests.get(manzil)
# pprint(r.text)

# country = 'Uzbekistan'
# url = f"https://restcountries.eu/rest/v2/name/{country}"
# r = requests.get(url)
# r_json = r.json()[0]
# print(r_json['capital'])

#----------------------------------------------------------------------------------------------#

# import requests
# import googletrans

# url = "https://api.adviceslib.com/advice"
# r = requests.get(url) 
# advice = r.json()['slip']['advices']
# print(advice)

# translator = googletrans.Translator()
# tarjima = translator.translate(advice,dest='uz')
# print(tarjima.text)

#----------------------------------------------------------------------------------------------#

# from bs4 import BeautifulSoup

# sahifa = "https://kun.uz/news/main"
# r = requests.get(sahifa)

# soup = BeautifulSoup(r.text, 'html.parser')
# news = soup.find_all(class_="news-title") # yangiliklarning mavzusini ajratib olamiz
# print(news[26].text)

#----------------------------------------------------------------------------------------------#