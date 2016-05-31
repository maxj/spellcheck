
from flask import Flask, jsonify, request
import spellcheck

app = Flask(__name__)

@app.route('/check', methods=['POST'])
def checkSpelling():
    error = None
    checkSpell = spellcheck.correct(request.form['word'])
    if checkSpell == request.form['word']:
        return "", 200
    else:
        return jsonify(checkSpell), 303

if __name__ == "__main__":
    app.run()
