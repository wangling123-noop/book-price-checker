import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from crawler.taobao import search_price as taobao_price
from crawler.jd import search_price as jd_price
from crawler.dangdang import search_price as dangdang_price

app = Flask(__name__)
CORS(app)  # 允许所有来源跨域请求

@app.route('/api/price', methods=['POST'])
def price():
    data = request.json
    book_name = data.get("book_name", "").strip()
    if not book_name:
        return jsonify({"error": "请提供书名"}), 400

    try:
        prices = {
            "淘宝": taobao_price(book_name),
            "京东": jd_price(book_name),
            "当当": dangdang_price(book_name)
        }
        return jsonify({
            "book_name": book_name,
            "prices": prices
        })
    except Exception as e:
        return jsonify({"error": f"查询失败: {str(e)}"}), 500

@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
