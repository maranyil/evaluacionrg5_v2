import pandas as pd
from flask import Flask

app = Flask(__name__, static_url_path="")

@app.route('/')

def shiny_csv():
    readcsv = pd.read_csv('data/employees.csv')
    table = readcsv.to_html()
    return(table)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
