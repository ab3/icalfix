from flask import Flask, request
from urllib import urlopen
from src.icalfix import IcalTimezoneFix

app = Flask(__name__)

@app.route('/')
def main():
    source = request.args.get('s', 'http://tinyurl.com/0x20Calendar')
    timezone = request.args.get('t', 'Europe/Brussels')
    try:
        f = urlopen(source)
    except Exception as err:
        return '%s' % err
    else:
        fixer = IcalTimezoneFix()
        return fixer.fix(f.read(), timezone)

if __name__ == '__main__':
    app.run()


