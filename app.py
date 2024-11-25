from flask import Flask, render_template, url_for, send_from_directory

app = Flask(__name__, static_url_path='/static')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route("/")
def index():
    carousel_images = [
        {"src": "/static/Бакуля4.jpg", "alt": "Image 1"},
        {"src": "/static/Бакуля5.jpg", "alt": "Image 2"},
        {"src": "/static/Бакуля6.jpg", "alt": "Image 3"},
    ]
    cards = [
        {
            "image": "/static/Бакуля1.jpg",
            "title": "Профессионал",
            "description": "Опытный дипломированный специалист со стажем работы 3,5 года.",
        },
        {
            "image": "/static/Бакуля2.jpg",
            "title": "Красавчик",
            "description": "Он обладает невероятной харизмой, мастерством сладостных изречений и бросает завлекающие взгляды.",
        },
        {
            "image": "/static/Бакуля3.jpg",
            "title": "И просто любимый мамин сын",
            "description": "Всегда за любой кипиш, но только если мама отпустит (на деле, весь кипиш создают с мамой сами)",
        },
    ]
    accordion_items = [
        {"title": "Наши курсы", "content": "Базовый курс - обучение стандартным приёмам покорения людей своей харизмой<br>Стандартный курс - помимо стандартных приёмов добавляется владение навыками попрашайничества<br>Продвинутый курс - после этого курса ваша харизма будет прокачана на максимум, вся вкусная еда достанется вам, и ни одна бабуля во дворе не сможет отвести от вас взгляд!"},
        {"title": "Отзывы", "content": "Все отзывы хорошие. Плохие писать нельзя. Запрещено регламентом, потому что мы так сказали."},
        {"title": "Оплата", "content": "Варианты оплаты: <br>Карта<br>Наличные<br>Перевод<br>Вкусняшки, желательно побольше"},
    ]

    return render_template(
        "index.html",
        carousel_images=carousel_images,
        cards=cards,
        accordion_items=accordion_items,
    )


if __name__ == "__main__":
    app.run(debug=True)