import os
import logging
from flask import Flask, session, redirect, render_template, request


logging.warn('app start!')

# Start Flask
app = Flask(__name__)

# Set key to use session of flask
#app.secret_key = os.environ['SECRET_KEY']

# Set root page
@app.route('/')
def index():

	return render_template('index.html')

#if __name__ == '__main__':
#	app.run()
