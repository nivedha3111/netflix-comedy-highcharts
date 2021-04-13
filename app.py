from flask import Flask, render_template, jsonify
import random
import json

app = Flask(__name__)
PORT = 3500

#FILEPATH = "data.json"



@app.route("/", methods=["GET", "POST"])
def startpy():

    result = {

        "Greetings": "Tactlabs welcomes you"
    }

    return render_template("index.html")




@app.route("/data", methods=["GET"])
def read_json():

    #data = None
    #with open(FILEPATH) as json_file:
     #   data = json.load(json_file)

    
    series_list = ['FRIENDS', 'The Big Bang Theory', 'Brooklyn nine-nine', 'The good place', 'The Ranch', 'Workin moms',
                  'After Life', 'The Crew', 'Alexa & Katie']

    rate_list = [8.9, 8.1, 8.4, 8.2, 7.5, 7.6, 8.4, 6.6, 7.5]

    result_dict = {
        'series_data': series_list,
        #'local_data': data,
        'series_names': 'series names',
        'title': 'netflix comedy series and their IMDb rating ',
        'subtitle': 'Source: https://www.netflix.com/in/browse/genre/10375',
        'rate_data': rate_list
    }

    

    return jsonify(result_dict)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
