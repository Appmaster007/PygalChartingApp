from flask import Flask,render_template
import pygal
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
    chart = pygal.Bar()
    chart.add('Annual Mark List',[])
    chart.render_to_file('static/images/bar_chart.svg')
    return render_template('app.html')

#
# Utility to fetch JSON annual marks from API
# and convert the data to a Python list
#
def GetAnnualMarkList():
    print 'hello'


if __name__=="__main__":
    app.run()



