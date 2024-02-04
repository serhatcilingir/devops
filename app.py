from flask import Flask, render_template, request

app = Flask(__name__)

def isimleri_sirala(isim_listesi):
    sirali_isimler = sorted(isim_listesi)
    return sirali_isimler

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        isimler = request.form['isimler'].split(',')
        sirali_isimler = isimleri_sirala(isimler)
        return render_template('index.html', sirali_isimler=sirali_isimler)
    return render_template('index.html')

if __name__ == "__main__":
    with app.app_context():
        app.run(host="0.0.0.0", port=5000)
