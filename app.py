
import flask
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def homepage():  # put application's code here
    return render_template("homepage.html")

@app.route('/AboutUsPage')
def AboutUsPage():  # put application's code here
    return flask.render_template("AboutUsPage.html")

@app.route('/ContactPage')
def ContactPage(): # put application's code here
    return flask.render_template("ContactPage.html")

@app.route('/GalleryPage')
def Gallery(): # put application's code here
    return flask.render_template("Gallery.html")

@app.route('/InquiryPage')
def InquiryPage(): # put application's code here
    return flask.render_template("InquiryPage.html")

@app.route('/ReviewPage')
def ReviewPage(): # put application's code here
    return flask.render_template("ReviewPage.html")

@app.route('/ServiesPage')
def ServicesPage(): # put application's code here
    return flask.render_template("ServicesPage.html")

@app.route('/FinancingPage')
def FinancingPage(): # put application's code here
    return flask.render_template("Financing.html")

@app.route('/WriteReview')
def WriteReview(): # put application's code here
    return flask.render_template("WriteReview.html")

@app.route('/Payment')
def Payment(): # put application's code here
    return flask.render_template("Payment.html")

@app.route('/Paid')
def Paid(): # put application's code here
    return flask.render_template("Paid.html")

if __name__ == '__main__':
    app.run()
6