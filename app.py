from flask import Flask,render_template
import pygal
import json
import time
app = Flask(__name__)

# -----------------------------------------
# Default route for the charting application
# -----------------------------------------

@app.route("/")
def home():
    return "Welcome tp Pygal Charting Libraru !!"

# -------------------------------------------
# Charting route which displays the bar chart
# -------------------------------------------

@app.route("/bar")
def bar():
    with open('bar.json','r') as bar_file:
        data = json.load(bar_file)
    mark_list = [x['mark'] for x in data]
    chart = pygal.Bar()
    chart.add('Annual Mark List',mark_list)
    chart.x_labels = [x['year'] for x in data]
    chart.render_to_file('static/images/bar_chart.svg')
    img_url = 'static/images/bar_chart.svg?cache=' + str(time.time())
    return render_template('app.html',image_url = img_url)

if __name__=="__main__":
    app.run()
