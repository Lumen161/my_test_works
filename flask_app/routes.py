from flask import Flask, request, render_template
from flask_app.main import count_words

app = Flask(__name__)


@app.route('/')
def start():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files.get('textfile')

    if uploaded_file and uploaded_file.filename.endswith('.txt'):
        content = uploaded_file.read().decode('utf-8')
        word_list = content.split()
        tabl = count_words(word_list)

        return render_template('result.html', words=tabl)
    else:
        return 'Загрузите .txt файл'
