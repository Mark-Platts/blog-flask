import os

#Logic Stuff
def getArcList():
    mypath = "./templates"
    hold_dir = os.listdir(mypath)
    dontUse = ['archive.html', 'base.html', 'home.html']
    arcList = []
    for i in hold_dir:
        if i not in dontUse:
            arcList.append(i)
    return(arcList)




#Server Stuff
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return(render_template('home.html'))

@app.route("/archive")
def archive():
    arcList = getArcList()
    return(render_template('archive.html', arcList = arcList))

@app.route('/<path:page>')
def goTo(page):
    return render_template('%s.html' % page)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
