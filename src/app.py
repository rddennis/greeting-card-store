from flask import Flask, render_template
from livereload import Server
from moltin.moltin import Moltin 

import urllib2
import json
import pprint

app = Flask(__name__)
app.debug = True

m = Moltin("CKVntdOscTXDWG216d0g4j9VEs15D4sIrXB7zbLnc8", "j5MDDb3eyqThYwfwUNcYF1vv8ivKXh2xcBobPk5uqd")
access_token = m.authenticate()

@app.route("/")
def home():
	return render_template('home.html')

@app.route("/shop")
def shop():
	products = m.Product.list()
	return render_template('shop.html', products = products)

@app.route("/shop/<product_slug>")
def product_search(product_slug):
	print product_slug
	item = m.Product.find({'slug': product_slug})
	pprint.pprint(item)
	return render_template('product.html', product = item)

Server(app.wsgi_app).serve()