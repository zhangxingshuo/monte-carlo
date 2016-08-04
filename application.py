from flask import Flask, render_template, send_file, request
import functions
application = Flask(__name__)

@application.route("/home")
@application.route("/")
def home():
    return render_template("index.html")

@application.route("/intro")
def intro():
    return render_template("intro.html")

@application.route("/week1")
def week1():
    return render_template("week1.html")

@application.route("/week2")
def week2():
    return render_template("week2.html")

@application.route("/week3")
def week3():
    return render_template("week3.html")


@application.route("/week4")
def week4():
    return render_template("week4.html")

@application.route("/week5")
def week5():
    return render_template("week5.html")

@application.route("/week6")
def week6():
    return render_template("week6.html")

@application.route("/week7")
def week7():
    return render_template("week7.html")


@application.route("/weather", methods=["GET", "POST"])
def weather():
    if request.method == "POST":
        import requests
        from json import loads
        print("hey")
        url = "http://api.openweathermap.org/data/2.5/forecast/daily?apikey="
        key = "68bc028863585c845c58bf9a99b99ddd"

        url += key

        city = request.form["city"]
        url += "&q=" + city

        form = "json"
        url +=",us&mode=" + form # xml

        units = request.form.getlist('units') # standard, metric

        if len(units) == 1:
            url += "&units="+units[0]

        days = request.form['days']
        url += "&cnt="+str(days)

        response = requests.get(url)
        data = loads(response.text)

        weather = data['list']
        return render_template("display.html", weather=weather)
    else:
        return render_template("ask.html")


@application.route("/prime/<int:num>")
@application.route("/prime/")
def prime(num=None):
    return render_template("prime.html", num=num, isPrime=functions.isPrime)

@application.route('/example1')
def example1():
      return render_template('example1.html')



if __name__ == "__main__":
    application.debug = True
    application.run()
