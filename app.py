from flask import Flask, render_template, request, redirect, url_for
import redis

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'add_pair' in request.form:
            key = request.form['key']
            value = request.form['value']
            r.set(key, value)
        elif 'update_pair' in request.form:
            key = request.form['key']
            value = request.form['value']
            r.set(key, value)
        elif 'delete_pair' in request.form:
            key = request.form['key']
            r.delete(key)

        return redirect(url_for('index'))
    
    keys = r.keys()
    key_value_pairs = {key.decode('utf-8'): r.get(key).decode('utf-8') for key in keys}

    return render_template('index.html', key_value_pairs=key_value_pairs) 

if __name__ == '__main__':
    app.run(debug=True, port=8037)
