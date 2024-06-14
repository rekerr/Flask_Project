from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/k<int:page_num>')
def page(page_num):
    if 1 <= page_num <= 12:
        return render_template(f'k{page_num}.html')
    else:
        return "Nie znaleziono", 404

if __name__ == '__main__':
    app.run(debug=True)
