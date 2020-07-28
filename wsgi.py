from flask import Flask
from POSTag import postag

app = Flask(__name__)
app.register_blueprint(postag, url_prefix='/v1/pos-tag')

app.run()