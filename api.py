from flask import Flask, request, jsonify, send_from_directory
import math

app = Flask(__name__)
# Разрешаем кросс-доменные запросы для всех ресурсов

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/calc', methods=['POST'])
def calculate():
    print("Выполняем запрос")
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

@app.route('/sqrt', methods=['GET', 'POST'])
def sqrt():
    if request.method == 'GET':
        number = request.args.get('base')
    elif request.method == 'POST':
        data = request.get_json()
        number = data.get('base')
    else:
        return jsonify({'error': 'Unsupported method'}), 405

    if number is None:
        return jsonify({'error': 'Parameter "base" is missing'}), 400

    try:
        number = float(number)
    except ValueError:
        return jsonify({'error': 'Parameter "base" must be a valid float'}), 400

    if number < 0:
        return jsonify({'error': 'Parameter "base" must be non-negative'}), 400

    result = math.sqrt(number)
    return jsonify({'input': number, 'result': result})


@app.route('/pow', methods=['GET', 'POST'])
def power():
    if request.method == 'GET':
        number = request.args.get('base')
        exponent = request.args.get('exp')
    elif request.method == 'POST':
        data = request.get_json()
        number = data.get('base')
        exponent = data.get('exp')
    else:
        return jsonify({'error': 'Unsupported method'}), 405

    if number is None or exponent is None:
        return jsonify({'error': 'Parameters "base" and "exp" are missing'}), 400

    try:
        number = float(number)
        exponent = float(exponent)
    except ValueError:
        return jsonify({'error': 'Parameters "base" and "exp" must be valid floats'}), 400

    result = number ** exponent
    return jsonify({'input': {'number': number, 'exponent': exponent}, 'result': result})


@app.route('/')
def index():
    return send_from_directory('.', 'calc.html')

@app.route('/health')
def health_check():
    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

