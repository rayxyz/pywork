from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    echostr = request.args.get('echostr')
    print('echostr => ', echostr)
    return echostr

@app.route('/test')
def test():
    return 'this is a wechat dev test'

