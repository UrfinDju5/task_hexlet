from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

#menu = [" гост 2719 ", "гост 31877", "гост 9064"]

questions = [
    {
        'question': 'ГОСТ 3217 какого банана это все',
        'options': ['London', 'Paris', 'Berlin', 'Madrid'],
        'answer': 'Paris'
    },
    {
        'question': 'What is the largest country in the world?',
        'options': ['China', 'Russia', 'India', 'USA'],
        'answer': 'Russia'
    },
    {
        'question': 'What is the currency of Japan?',
        'options': ['Yen', 'Dollar', 'Euro', 'Pound'],
        'answer': 'Yen'
    }
]

@app.route('/', methods=['GET', 'POST'])
def test_form():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        return redirect(url_for('test', name=name, surname=surname))
    return render_template('test_form.html')

@app.route('/test/<name>/<surname>', methods=['GET', 'POST'])
def test(name, surname):
    if request.method == 'POST':
        score = 0
        for i, q in enumerate(questions):
            answer = request.form.get(f'q{i}')
            if answer == q['answer']:
                score += 1
        result = {
            'name': name,
            'surname': surname,
            'score': score,
            'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        return redirect(url_for('test_result', **result))
    return render_template('test.html', questions=questions)

@app.route('/result')
def test_result():
    name = request.args.get('name')
    surname = request.args.get('surname')
    score = request.args.get('score')
    date = request.args.get('date')
    return render_template('result.html', name=name, surname=surname, score=score, date=date)

@app.context_processor
def inject_enumerate():
    return dict(enumerate=enumerate)

if __name__ == '__main__':
    app.run(debug=True)
