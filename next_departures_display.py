from flask import Flask, render_template
import pandas as pd
import requests
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/departures/<int:station_id>')
def hello(station_id):
    
    raw = pd.DataFrame(requests.get(f'https://start.vag.de/dm/api/v1/abfahrten/VGN/{station_id}?timespan=30').json()['Abfahrten'])
    df = raw.copy()
    
    df.Richtungstext = df.Richtungstext.str.replace('_', ' ')
    
    df['AbfahrtszeitSoll_UTC'] = pd.to_datetime(raw.AbfahrtszeitSoll, utc=True)
    df['AbfahrtszeitIst_UTC'] = pd.to_datetime(raw.AbfahrtszeitIst, utc=True)
    
    df['AbfahrtszeitSoll'] = pd.to_datetime(raw.AbfahrtszeitSoll)
    df['AbfahrtszeitIst'] = pd.to_datetime(raw.AbfahrtszeitIst)
    
    df['Verspaetung'] = (df.AbfahrtszeitIst_UTC - df.AbfahrtszeitSoll_UTC).apply(pd.to_timedelta).astype('timedelta64[m]')
    df.Verspaetung = df.Verspaetung.astype('int')
    
    df['AbfahrtszeitIstIn'] = (df.AbfahrtszeitIst_UTC - pd.Timestamp(datetime.now(pytz.UTC)) ).apply(pd.to_timedelta).astype('timedelta64[m]')
    df.AbfahrtszeitIstIn = df.AbfahrtszeitIstIn.astype('int')
    
    df = df[['Linienname', 'Richtungstext', 'AbfahrtszeitIst', 'Verspaetung', 'AbfahrtszeitIstIn', 'Produkt']]

    return render_template('index.html', abfahrten=df.to_dict(orient='records'))
