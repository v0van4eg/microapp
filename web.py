from flask import Flask, request, jsonify, send_from_directory
import math

app = Flask(__name__)

@app.route('/calc', methods=['POST'])
def calculate():
    data = request.get_json()

    operation = data.get('operation')
    number1 = data.get('number1')
    number2 = data.get('number2')

    if operation not in ['sqrt', 'pow']:
        return jsonify({'error': 'Неподдерживаемая операция'}), 400

    if operation == 'sqrt' and number1 is None:
        return jsonify({'error': 'Отсутствует параметр "number1"'}), 400

    if operation == 'pow' and (number1 is None or number2 is None):
        return jsonify({'error': 'Отсутствуют параметры "number1" или "number2"'}), 400

    try:
        number1 = float(number1)
        if operation == 'pow':
            number2 = float(number2)
    except ValueError:
        return jsonify({'error': 'Параметры должны быть числами'}), 400

    if operation == 'sqrt' and number1 < 0:
        return jsonify({'error': 'Число должно быть неотрицательным'}), 400

    if operation == 'pow' and number2 < 0:
        return jsonify({'error': 'Степень должна быть неотрицательной'}), 400

    if operation == 'sqrt':
        result = math.sqrt(number1)
    elif operation == 'pow':
        result = number1 ** number2

    response = jsonify({'result': result})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/')
def index():
    return send_from_directory('.', 'calc.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
