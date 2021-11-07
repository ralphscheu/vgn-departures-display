# VGN Departures Display

This tiny Flask app pulls upcoming departures for a given station in the *Verkehrsverbund Großraum Nürnberg (VGN)* public transport service area from the official API.

VGN offers something very similar to this already, however I found it to waste too much space on small screens or iframes.
Also, I wanted to learn Flask :)

My personal use case is embedding this into my Home Assistant dashboard as an iframe using the Website Lovelace Card.

## Setup
This describes a minimal setup on Linux.

- Clone the repository
- Ensure that your system has python3 and python3-virtualenv installed
- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `pip install -r requirements.txt`
- `export FLASK_APP=next_departures_display`
- `export FLASK_ENV=production` (set to development for debug mode)
- `flask run --host 0.0.0.0 --port 5000`

## Future plans
- Enable filtering types of transportation
- Enable customizing the timespan in minutes that shall be included (e.g. 60min from now)
- Turn this into a Home Assistant Integration
- Provide a docker container
