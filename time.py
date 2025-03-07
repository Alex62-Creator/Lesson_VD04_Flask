from flask import Flask
#from datetime import datetime
import time

app = Flask(__name__)

@app.route("/")
def current_date():
    #return f"Текущее время: {datetime.now()}"
    return f"Текущее время: {time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())}"

if __name__ == "__main__":
    app.run()