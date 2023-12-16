from flask import Flask, render_template, request

app = Flask(__name__)

# Grundkonstanten
MAX_SCORE = 10

@app.route('/')
def index():
    """ Zeigt das Hauptformular an. """
    return render_template('score_calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    """ Berechnet die Endnote basierend auf den Formulareingaben. """
    try:
        difficulty = float(request.form['difficulty'])
        deductions = float(request.form['deductions'])

        # Berechnung der Ausführungsnote
        execution = MAX_SCORE - deductions

        # Berechnung der Endnote
        final_score = difficulty + execution

        return render_template('score_calculator.html', 
                               difficulty=difficulty, 
                               execution=execution, 
                               final_score=final_score)
    except ValueError:
        # Fehlerbehandlung für ungültige Eingaben
        return "Ungültige Eingabe. Bitte geben Sie gültige Zahlen ein.", 400

if __name__ == '__main__':
    app.run(debug=True)
