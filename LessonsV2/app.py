from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, suport_credentials=True)
from ReqWhut import req


@app.route('/')
def hello_world():
    return '<h1>当前服务已经启动</h1>!'


@app.route('/getInfo')
def get_info():
    try:
        return jsonify({
            'status': 200,
            'msg': '查询成功',
            'data': {
                'is_updated': False,
                'downloadURL': '',
                'start_date': [2020, 8, 7],
                'title': '同学，你好！',
                'message': '欢迎使用武汉理工大学课表V2（可离线）。请使用教务管理系统登录，如仍然提示密码错误，可能是由于密码难度低，需要前往教务管理网提高密码难度。',
                'three_pic': ['https://xgpax.top/whutv2imgs/sky.jpg', 'https://xgpax.top/whutv2imgs/lakesi.jpg',
                              'https://xgpax.top/whutv2imgs/bingqueen.jpg']
            }
        })
    except Exception as e:
        with open('error.log', 'w+', encoding='utf8') as fp:
            fp.write(str(e))


@app.route('/api/lesson')
def request_data():
    try:
        username = request.args.get('username')
        password = request.args.get('password')
        data = req(username, password)
    except Exception as e:
        with open('error.log', 'w+', encoding='utf8') as fp:
            fp.write(str(e))
        return jsonify({
            'status': 500,
            'msg': '查询失败',
            'data': []
        })

    return jsonify({
        'status': 200,
        'msg': '查询成功',
        'data': data
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10086)
