from flask import Flask, request, jsonify
from crawler.jd import get_jd_price
from crawler.dangdang import get_dangdang_price
from crawler.taobao import get_taobao_price

app = Flask(__name__)

@app.route('/')
def index():
    return "欢迎使用图书价格查询接口"

@app.route('/api/price', methods=['POST'])
def get_price():
    data = request.json
    book_name = data.get("book_name")
    if not book_name:
        return jsonify({"error": "缺少参数：book_name"}), 400

    result = {
        "京东": get_jd_price(book_name),
        "当当": get_dangdang_price(book_name),
        "淘宝": get_taobao_price(book_name)
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
