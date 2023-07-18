import requests
from bs4 import BeautifulSoup

# Запрашиваем у пользователя ссылку на исполнителя
# Ссылка на исполнителя "https://mp3party.net/artist/344/pop"
artist_url = input("Введите ссылку на исполнителя: ")

try:
    # Отправляем GET-запрос на указанную ссылку
    response = requests.get(artist_url)

    # Проверяем статус код ответа
    if response.status_code == 200:
        # Получаем HTML-код страницы
        html = response.text

        # Создаем объект BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(html, 'html.parser')

        # Находим все элементы с тегом <div> и классом "song"
        songs = soup.find_all('div', class_='track song-item')

        # Проверяем, что найдено хотя бы 10 песен
        if len(songs) < 10:
            print("Недостаточно песен. "
                  "Попробуйте другого исполнителя или сервис.")
        else:
            # Выводим информацию о топ 10 песен
            for i in range(10):
                song_title = songs[i].find('a',
                                           class_='track__title js-track-title').text.strip()
                print(f"{i + 1}. {song_title}")
    else:
        print("Ошибка при отправке запроса. "
              "Проверьте ссылку или подключение к интернету.")
except requests.exceptions.RequestException as e:
    print("Ошибка при отправке запроса:", e)
