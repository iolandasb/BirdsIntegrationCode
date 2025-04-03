from flask import Flask, jsonify, render_template
import pandas as pd

app = Flask(__name__)

from flask import Flask, jsonify, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/birds', methods=['GET'])
def get_birds():
    try:
        df = pd.read_excel('birds.xlsx')  # Lê o arquivo Excel
        birds = df.to_dict(orient='records')  # Converte para lista de dicionários
        return jsonify(birds)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)