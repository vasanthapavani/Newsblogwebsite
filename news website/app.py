from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def slide():
    return render_template("slide.html")

@app.route('/entertainment')
def entertainment():
    return render_template("entertainment.html")

@app.route('/rrr')
def rrr():
    return render_template("rrr.html")

@app.route('/kantara')
def kantara():
    return render_template("kantara.html")

@app.route('/nbk')
def nbk():
    return render_template("nbk.html")

@app.route('/pushpa2')
def pushpa2():
    return render_template("pushpa2.html")

@app.route('/pspk')
def pspk():
    return render_template("pspk.html")

@app.route('/dasara')
def dasara():
    return render_template("dasara.html")
        
@app.route('/politics')
def politics():
    return render_template("politics.html")

@app.route('/janasena')
def janasena():
    return render_template("janasena.html")

@app.route('/tdp')
def tdp():
    return render_template("tdp.html")

@app.route('/ippatam')
def ippatam():
    return render_template("ippatam.html")

@app.route('/kavitha')
def kavitha():
    return render_template("kavitha.html")

@app.route('/sports')
def sports():
    return render_template("sports1.html")

@app.route('/ipl')
def ipl():
    return render_template("ipl.html")

@app.route('/woment20')
def woment20():
    return render_template("woment20.html")

@app.route('/trophy')
def trophy():
    return render_template("trophy.html")

@app.route('/ronaldo')
def ronaldo():
    return render_template("ronaldo.html")

@app.route('/kohli')
def kohli():
    return render_template("kohli.html")

@app.route('/sania')
def sania():
    return render_template("sania.html")

@app.route('/team')
def team():
    return render_template("team.html")

if __name__=='__main__':
   app.run(debug=True)
