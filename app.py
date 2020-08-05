from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators

app = Flask(__name__)

class HelloForm(Form):
    sayhello = TextAreaField('', [validators.DataRequired()])  # 有効な入力テキストかどうかチェック

@app.route('/')
def index():
    form = HelloForm(request.form)
    return render_template('first_app.html', form=form)

# POSTでフォームのデータをサーバーに送信
@app.route('/hello', methods=['POST'])
def hello():
    form = HelloForm(request.form)
    # フォームが問題なく検証された場合hello.htmlというページを表示
    if request.method == 'POST' and form.validate():
        name = request.form['sayhello']
        return render_template('hello.html', name=name)
    return render_template('first_app.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)