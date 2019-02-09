# 1. import Flask
from flask import Flask, jsonify

precipitation = [
{'2016-08-23': 0.7,
 '2016-08-24': 1.45,
 '2016-08-25': 0.11,
 '2016-08-26': 0.01,
 '2016-08-27': None,
 '2016-08-28': 2.07,
 '2016-08-29': 0.9,
 '2016-08-30': 0.05,
 '2016-08-31': 2.46,
 '2016-09-01': 0.01,
 '2016-09-02': 0.03,
 '2016-09-03': 1.0,
 '2016-09-04': 0.44,
 '2016-09-05': 0.18,
 '2016-09-06': 1.0,
 '2016-09-07': 1.35,
 '2016-09-08': 0.15,
 '2016-09-09': 0.35,
 '2016-09-10': 1.16,
 '2016-09-11': 0.6,
 '2016-09-12': 1.04,
 '2016-09-13': 1.2,
 '2016-09-14': 6.7,
 '2016-09-15': 3.35,
 '2016-09-16': 0.61,
 '2016-09-17': 0.23,
 '2016-09-18': 0.42,
 '2016-09-19': 0.25,
 '2016-09-20': 0.43,
 '2016-09-21': 1.02,
 '2016-09-22': 0.75,
 '2016-09-23': 0.33,
 '2016-09-24': 0.27,
 '2016-09-25': 0.04,
 '2016-09-26': 1.02,
 '2016-09-27': 1.0,
 '2016-09-28': 0.05,
 '2016-09-29': 1.49,
 '2016-09-30': 0.38,
 '2016-10-01': 1.02,
 '2016-10-02': 0.61,
 '2016-10-03': 0.46,
 '2016-10-04': 3.46,
 '2016-10-05': 0.81,
 '2016-10-06': 0.04,
 '2016-10-07': 0.01,
 '2016-10-08': 0.04,
 '2016-10-09': 0.0,
 '2016-10-10': 0.0,
 '2016-10-11': 0.35,
 '2016-10-12': 0.02,
 '2016-10-13': 0.06,
 '2016-10-14': 0.0,
 '2016-10-15': 0.33,
 '2016-10-16': 0.0,
 '2016-10-17': 0.38,
 '2016-10-18': 0.48,
 '2016-10-19': 0.0,
 '2016-10-20': 1.0,
 '2016-10-21': 0.09,
 '2016-10-22': 1.37,
 '2016-10-23': 0.24,
 '2016-10-24': 0.7,
 '2016-10-25': 0.4,
 '2016-10-26': 0.0,
 '2016-10-27': 1.25,
 '2016-10-28': 0.37,
 '2016-10-29': 0.25,
 '2016-10-30': 0.95,
 '2016-10-31': 1.35,
 '2016-11-01': 0.09,
 '2016-11-02': 0.04,
 '2016-11-03': 0.02,
 '2016-11-04': 0.06,
 '2016-11-05': 0.38,
 '2016-11-06': 0.05,
 '2016-11-07': 0.05,
 '2016-11-08': 0.53,
 '2016-11-09': 0.04,
 '2016-11-10': 0.01,
 '2016-11-11': 0.0,
 '2016-11-12': 0.0,
 '2016-11-13': 0.0,
 '2016-11-14': 0.02,
 '2016-11-15': 0.05,
 '2016-11-16': 0.91,
 '2016-11-17': 0.02,
 '2016-11-18': 0.0,
 '2016-11-19': 0.11,
 '2016-11-20': None,
 '2016-11-21': 2.87,
 '2016-11-22': 2.11,
 '2016-11-23': 0.22,
 '2016-11-24': 0.72,
 '2016-11-25': 1.03,
 '2016-11-26': 0.3,
 '2016-11-27': 0.29,
 '2016-11-28': 0.69,
 '2016-11-29': 0.2,
 '2016-11-30': 0.79,
 '2016-12-01': 0.72,
 '2016-12-02': 1.27,
 '2016-12-03': 1.62,
 '2016-12-04': 0.31,
 '2016-12-05': 1.6,
 '2016-12-06': 0.0,
 '2016-12-07': 0.02,
 '2016-12-08': 0.03,
 '2016-12-09': 0.42,
 '2016-12-10': 0.04,
 '2016-12-11': 0.13,
 '2016-12-12': 0.01,
 '2016-12-13': 0.09,
 '2016-12-14': 0.33,
 '2016-12-15': 0.03,
 '2016-12-16': 0.0,
 '2016-12-17': 0.07,
 '2016-12-18': None,
 '2016-12-19': 0.15,
 '2016-12-20': 0.0,
 '2016-12-21': 0.55,
 '2016-12-22': 1.24,
 '2016-12-23': 0.83,
 '2016-12-24': 1.08,
 '2016-12-25': 0.38,
 '2016-12-26': 1.48,
 '2016-12-27': 0.14,
 '2016-12-28': 0.14,
 '2016-12-29': 1.03,
 '2016-12-30': 2.37,
 '2016-12-31': 0.9,
 '2017-01-01': 0.03,
 '2017-01-02': 0.0,
 '2017-01-03': 0.0,
 '2017-01-04': 0.0,
 '2017-01-05': 0.47,
 '2017-01-06': 0.1,
 '2017-01-07': 0.0,
 '2017-01-08': 0.03,
 '2017-01-09': 0.0,
 '2017-01-10': 0.0,
 '2017-01-11': 0.0,
 '2017-01-12': 0.0,
 '2017-01-13': 0.0,
 '2017-01-14': 0.0,
 '2017-01-15': 0.01,
 '2017-01-16': 0.0,
 '2017-01-17': 0.0,
 '2017-01-18': 0.07,
 '2017-01-19': 0.0,
 '2017-01-20': 0.0,
 '2017-01-21': 0.08,
 '2017-01-22': 0.72,
 '2017-01-23': 0.85,
 '2017-01-24': 1.85,
 '2017-01-25': 2.64,
 '2017-01-26': 0.1,
 '2017-01-27': 0.03,
 '2017-01-28': 0.0,
 '2017-01-29': 0.55,
 '2017-01-30': 0.0,
 '2017-01-31': 0.0,
 '2017-02-01': 0.0,
 '2017-02-02': 0.0,
 '2017-02-03': 0.0,
 '2017-02-04': None,
 '2017-02-05': 0.0,
 '2017-02-06': 0.0,
 '2017-02-07': 1.79,
 '2017-02-08': 0.0,
 '2017-02-09': 0.0,
 '2017-02-10': 0.0,
 '2017-02-11': 0.73,
 '2017-02-12': 1.83,
 '2017-02-13': 0.0,
 '2017-02-14': 0.01,
 '2017-02-15': 0.07,
 '2017-02-16': 0.13,
 '2017-02-17': 0.13,
 '2017-02-18': None,
 '2017-02-19': 0.1,
 '2017-02-20': 0.0,
 '2017-02-21': 0.07,
 '2017-02-22': 0.32,
 '2017-02-23': 0.0,
 '2017-02-24': 0.0,
 '2017-02-25': 0.12,
 '2017-02-26': 0.0,
 '2017-02-27': 0.0,
 '2017-02-28': 0.58,
 '2017-03-01': 2.0,
 '2017-03-02': 0.58,
 '2017-03-03': 0.56,
 '2017-03-04': 0.0,
 '2017-03-05': 0.35,
 '2017-03-06': 0.0,
 '2017-03-07': 0.0,
 '2017-03-08': 0.0,
 '2017-03-09': 0.01,
 '2017-03-10': 0.0,
 '2017-03-11': 0.0,
 '2017-03-12': 0.0,
 '2017-03-13': None,
 '2017-03-14': 0.0,
 '2017-03-15': 0.0,
 '2017-03-16': 0.0,
 '2017-03-17': 0.12,
 '2017-03-18': None,
 '2017-03-19': 0.0,
 '2017-03-20': 0.0,
 '2017-03-21': 0.0,
 '2017-03-22': 0.0,
 '2017-03-23': 0.03,
 '2017-03-24': 0.17,
 '2017-03-25': 0.48,
 '2017-03-26': 0.0,
 '2017-03-27': 0.0,
 '2017-03-28': 0.68,
 '2017-03-29': 0.07,
 '2017-03-30': 0.04,
 '2017-03-31': None,
 '2017-04-01': 0.2,
 '2017-04-02': 0.0,
 '2017-04-03': 0.23,
 '2017-04-04': 0.02,
 '2017-04-05': 0.45,
 '2017-04-06': 0.0,
 '2017-04-07': 0.0,
 '2017-04-08': None,
 '2017-04-09': 0.0,
 '2017-04-10': 0.0,
 '2017-04-11': 0.25,
 '2017-04-12': 0.65,
 '2017-04-13': 0.23,
 '2017-04-14': 2.82,
 '2017-04-15': 0.9,
 '2017-04-16': 0.11,
 '2017-04-17': 1.3,
 '2017-04-18': 0.98,
 '2017-04-19': 0.14,
 '2017-04-20': 0.0,
 '2017-04-21': 1.84,
 '2017-04-22': 1.35,
 '2017-04-23': 0.35,
 '2017-04-24': 0.05,
 '2017-04-25': 0.0,
 '2017-04-26': 0.22,
 '2017-04-27': 0.11,
 '2017-04-28': 0.79,
 '2017-04-29': 0.0,
 '2017-04-30': 0.8,
 '2017-05-01': 0.25,
 '2017-05-02': 0.0,
 '2017-05-03': 0.01,
 '2017-05-04': None,
 '2017-05-05': 0.1,
 '2017-05-06': 0.0,
 '2017-05-07': 0.03,
 '2017-05-08': 1.11,
 '2017-05-10': 0.55,
 '2017-05-11': 0.44,
 '2017-05-12': 0.1,
 '2017-05-13': 0.1,
 '2017-05-14': 1.0,
 '2017-05-15': 0.6,
 '2017-05-16': 0.3,
 '2017-05-17': 0.06,
 '2017-05-18': 0.0,
 '2017-05-19': 0.01,
 '2017-05-20': None,
 '2017-05-21': 0.0,
 '2017-05-22': 0.3,
 '2017-05-23': 0.44,
 '2017-05-24': 2.17,
 '2017-05-25': 0.88,
 '2017-05-27': 0.5,
 '2017-05-28': 0.0,
 '2017-05-29': 0.4,
 '2017-05-30': None,
 '2017-05-31': 0.25,
 '2017-06-01': 0.01,
 '2017-06-02': 0.09,
 '2017-06-03': None,
 '2017-06-04': 0.82,
 '2017-06-05': 0.01,
 '2017-06-06': 0.0,
 '2017-06-07': 0.01,
 '2017-06-08': 0.0,
 '2017-06-09': 0.02,
 '2017-06-10': None,
 '2017-06-11': 0.7,
 '2017-06-12': 0.81,
 '2017-06-13': 0.65,
 '2017-06-14': 0.81,
 '2017-06-15': 1.69,
 '2017-06-16': 0.1,
 '2017-06-17': 0.1,
 '2017-06-18': 0.7,
 '2017-06-19': 0.4,
 '2017-06-20': 0.31,
 '2017-06-21': 0.3,
 '2017-06-22': 0.28,
 '2017-06-23': 0.5,
 '2017-06-24': 0.22,
 '2017-06-25': 0.5,
 '2017-06-26': 0.02,
 '2017-06-27': 0.1,
 '2017-06-28': 0.02,
 '2017-06-29': 0.04,
 '2017-06-30': 0.2,
 '2017-07-01': 0.1,
 '2017-07-02': 0.5,
 '2017-07-03': 0.4,
 '2017-07-04': 0.0,
 '2017-07-05': 0.0,
 '2017-07-06': 0.02,
 '2017-07-07': 0.3,
 '2017-07-08': 0.02,
 '2017-07-09': 0.0,
 '2017-07-10': 0.02,
 '2017-07-11': 0.0,
 '2017-07-12': 0.05,
 '2017-07-13': 0.68,
 '2017-07-14': 0.68,
 '2017-07-15': 0.1,
 '2017-07-16': 0.5,
 '2017-07-17': 0.39,
 '2017-07-18': 2.4,
 '2017-07-20': 0.7,
 '2017-07-21': 0.1,
 '2017-07-22': 4.0,
 '2017-07-23': 0.8,
 '2017-07-24': 0.84,
 '2017-07-25': 0.3,
 '2017-07-26': 0.3,
 '2017-07-27': 0.0,
 '2017-07-28': 0.4,
 '2017-07-29': 0.3,
 '2017-07-30': 0.3,
 '2017-07-31': 0.0,
 '2017-08-01': None,
 '2017-08-02': 0.25,
 '2017-08-03': 0.06,
 '2017-08-04': 0.0,
 '2017-08-05': None,
 '2017-08-06': None,
 '2017-08-07': 0.05,
 '2017-08-08': 0.34,
 '2017-08-09': 0.15,
 '2017-08-10': 0.07,
 '2017-08-11': None,
 '2017-08-12': 0.14,
 '2017-08-13': None,
 '2017-08-14': 0.22,
 '2017-08-15': 0.42,
 '2017-08-18': None,
 '2017-08-19': 0.09,
 '2017-08-20': None,
 '2017-08-21': 0.56,
 '2017-08-22': 0.5,
 '2017-08-23': 0.45,
 '2017-05-09': 0.23,
 '2017-05-26': 0.0,
 '2017-07-19': 0.27,
 '2017-08-16': 0.42,
 '2017-08-17': 0.13
	

}]


# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "/api/v1.0/precipitation\n"
    "/api/v1.0/stations\n"
    "/api/v1.0/tobs\n"
    "/api/v1.0/tobs\n"
    "/api/v1.0/<start>\n"
    "/api/v1.0/<start>/<end>\n"




# 4. Define what to do when a user hits the /about route
@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server received request for 'precipitation' page...")
    return jsonify(precipitation)



if __name__ == "__main__":
    app.run(debug=True)