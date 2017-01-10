from flask import Flask,render_template
import pygal
import json
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
def chart():
    with open('bar.json','r') as bar_file:
        data = json.load(bar_file)
    mark_list = [x['mark'] for x in data]
    chart = pygal.Bar()
    chart.add('Annual Mark List',mark_list)
    chart.render_to_file('static/images/ba_chart.svg')
    return render_template('app.html')

#
# Utility to fetch JSON annual marks from API
# and convert the data to a Python list
#
def GetAnnualMarkList():
    print 'hello'


if __name__=="__main__":
    app.run()



