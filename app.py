from flask import Flask, request, render_template
from analysis import analyse, compare_sequences

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sequence = request.form['sequence']
        result = analyse(sequence)
        return render_template('result.html', result=result)
    return render_template('index.html')

@app.route('/compare', methods=['GET', 'POST'])
def compare():
    if request.method == 'POST':
        seq1 = request.form['seq1']
        seq2 = request.form['seq2']
        result = compare_sequences(seq1, seq2)
        return render_template('compare.html', result=result)
    return render_template('compare.html')

if __name__ == '__main__':
    app.run(debug=True)