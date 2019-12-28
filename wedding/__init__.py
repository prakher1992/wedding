from flask import Flask




app=Flask(__name__)

app.config['SECRET_KEY']='f6854380a4d38593662c150272a571d4'

from wedding import routes