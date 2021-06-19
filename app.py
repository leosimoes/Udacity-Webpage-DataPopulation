from flask import Flask, request, render_template
from dataUtils.dataProcessor import *

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello_world():
    figures = generateGraphs()
    ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]
    figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index.html',
                           ids=ids,
                           figuresJSON=figuresJSON)

if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=3001, debug=True)
    app.run()