from flask import Flask, render_template
import pymysql

app = Flask(__name__)

class Database:
    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        password = "#Basketball123423434#"
        db = "MarylandCrime"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db,
                cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()
    def list_locations(self):
        self.cur.execute("SELECT *  FROM marylandZipCodes  LIMIT 630")
        result = self.cur.fetchall()
        return result
    def crime_records(self):
        self.cursor.callproc("View_Fellons_And_Their_Crime_Records",args=())
        result = self.cur.fetchall()
        return result

@app.route('/')
def hello_name():
    return render_template('index.html')

@app.route('/CrimeByCity')
def crime_city():
    return render_template('cityCrime.html')

@app.route('/CrimeByCounty')
def crime_county():
    return render_template('countyCrime.html')

@app.route('/GovernmentOfficial')
def govOfficial():
    return render_template('governmentOfficial.html')

@app.route('/PoliceOfficer')
def policeOfficer():
    return render_template('policeOfficer.html')

@app.route('/Warden')
def warden():
    return render_template('warden.html')

@app.route('/GovernmentOfficial/FellonsAndCrime')
def fellon_and_crime():
    def db_query():
        db = Database()
        ans = db.crime_records()
        return ans
    res = db_query()
    return render_template('fellonsandcrime.html', result=res, content_type='application/json')

@app.route('/locations')
def locations():
    def db_query():
        db = Database()
        loc = db.list_locations()
        return loc
    res = db_query()
    return render_template('locations.html', result=res, content_type='application/json')

@app.route('/RehabCenters')
def rehabCenters():
    return render_template('rehabCenters.html')

