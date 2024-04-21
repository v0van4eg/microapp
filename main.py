from flask import Flask, request, jsonify
import math

app = Flask(__name__)


@app.route('/sqrt', methods=['GET'])
def sqrt():
    number = request.args.get('base')
    if number is None:
        return jsonify({'error': 'Parameter "number" is missing'}), 400

    try:
        number = float(number)
    except ValueError:
        return jsonify({'error': 'Parameter "number" must be a valid float'}), 400

    if number < 0:
        return jsonify({'error': 'Parameter "number" must be non-negative'}), 400

    result = math.sqrt(number)
    return jsonify({'input': number, 'result': result})


@app.route('/pow', methods=['GET'])
def power():
    number = request.args.get('base')
    exponent = request.args.get('exp')
    if number is None or exponent is None:
        return jsonify({'error': 'Parameters "base" and "exp" are missing'}), 400

    try:
        number = float(number)
        exponent = float(exponent)
    except ValueError:
        return jsonify({'error': 'Parameters "number" and "exponent" must be valid floats'}), 400

    result = number ** exponent
    return jsonify({'input': {'number': number, 'exponent': exponent}, 'result': result})


if __name__ == '__main__':
    app.run(debug=True)
