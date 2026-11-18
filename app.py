from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def index():
    massa = None
    altura = None
    diagnostico = None
    result = None
    if request.method == 'POST':
        massa = float(request.form.get('massa','').replace(',', '.'))
        altura = float(request.form.get('altura','').replace(',', '.'))
        imc = massa/(altura**2)
        if imc < 18.5:
            diagnostico = 'você esta abaixo do peso.'
        elif imc < 25:
            diagnostico = 'você esta no peso ideal'
        elif imc < 30:
            diagnostico = 'você esta a cima do peso'
        elif imc < 35:
            diagnostico = 'você esta gordo'
        elif imc < 40:
            diagnostico = 'Você esta imenso'
        elif imc < 50:
            diagnostico = 'Você tem gravidade propria'
        else:
            diagnostico = 'Você esta com obesidade morbida'
        result = f"<hr><h3>Seu imc é{imc:.2f}<br>{diagnostico}</3>"

             
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)