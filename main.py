from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # Das Hauptformular wird angezeigt.
    return render_template('score_calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Eingaben aus dem Formular werden abgerufen.
    difficulty = float(request.form['difficulty'])
    deductions = float(request.form['deductions'])

    # Berechnung der Ausführungsnote.
    execution = 10 - deductions

    # Berechnung der Endnote.
    final_score = difficulty + execution

    # Ergebnis wird zurück an das HTML-Formular gesendet.
    return render_template('score_calculator.html', difficulty=difficulty, execution=execution, final_score=final_score)

if __name__ == '__main__':
    app.run(debug=True)

