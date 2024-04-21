from flask import Flask, request, jsonify
import math

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)
