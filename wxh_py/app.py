
from flask import Flask, make_response

__author__ = 'wxh'

app = Flask(__name__)

# @app.route('/hello')  看下面add方法
def hello():
    # 基于类的视图（即插视图）
    return 'hello wxh'

# 不建议使用
@app.route('/hello1/')
def hello1():
    # 兼容 /  和 非/
    #  访问hello1 时会默认添加为 hello1/
    # 基于类的视图（即插视图）
    return 'hello wxh1'

@app.route('/html')
def html():
    print('进入该页面--')
    headers = {
        'content - type': 'text/plain'
    }
    response = make_response('<html></html>', 404)
    response.headers = headers
    return response

# 跳转至 bing
@app.route('/html/bing')
def html_bing():
    headers = {
        'content - type': 'text/plain',
        'location': 'http://www.bing.com'
    }
    # response = make_response('<html></html>', 301)
    # response.headers = headers
    # return response
    return '<html></html>', 301, headers


# 这种情况也可以（建议少使用）
app.add_url_rule('/hello',view_func=hello)
# 载入配置文件，读取
app.config.from_object('config')
# from_object 要求导入的为大写
print('debug : '+str(app.config['DEBUG']))


# app.run()
# 调试模式
# 异常信息也会在浏览器上显示
# 但是只能通过127.0.0.1 访问，外网访问不了
# app.run(debug=True)
# 此时 192.168.0.101 外网可以访问
# app.run(host='192.168.0.101',debug=True)
# 此时任意外网可以访问
# app.run(host='0.0.0.0',debug=True)
# 此时任意外网可以访问,可以添加端口
# app.run(host='0.0.0.0',debug=Truep,port=81)
# 此时任意外网可以访问,可以添加端口
# 确保以下app 只在main 方法运行
# 生产环境会使用 nginx + uwsgi
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=app.config['DEBUG'], port=81)

