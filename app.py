from flask import Flask, request, render_template
from main import get_prediction
from flask import Flask, request, render_template

from main import get_prediction

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/getprediction', methods=['POST'])
def getprediction():
    input = [x for x in request.form.values()]
    print(input)
    ar_score = get_prediction(input[0], input[1], input[2], input[3], input[4], input[5])
    return render_template('index.html', output='ar score was:{}'.format(ar_score))


if __name__ == "__main__":
    app.run(debug=True)
