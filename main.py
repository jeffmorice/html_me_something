from flask import Flask, request, render_template
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('1_early_anim.html')

@app.route("/hand-anim")
def hand_anim():
    return render_template('2_hand_anim.html')

@app.route("/stopmotion")
def stopmotion_anim():
    return render_template('3_stopmotion_anim.html')

@app.route("/3d")
def three_d_anim():
    return render_template('4_3d_anim.html')

@app.route("/future")
def future_anim():
    return render_template('5_Future.html')

app.run()
