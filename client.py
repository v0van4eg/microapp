import requests
import json

def main():
    numbers = input("Введите одно или два числа через пробел: ").split()

    if len(numbers) == 1:
        # Если введено одно число, отправляем запрос на вычисление квадратного корня
        number = numbers[0]
        response = make_request('http://localhost:5000/sqrt', 'GET', {'base': number})
        process_response(response, number, "квадратного корня")
    elif len(numbers) == 2:
        # Если введены два числа, отправляем запрос на возведение в степень
        base, exponent = numbers
        data = {'base': base, 'exp': exponent}
        response = make_request('http://localhost:5000/pow', 'POST', data)
        process_response(response, f"{base} в степени {exponent}", "степени")
    else:
        print("Пожалуйста, введите одно или два числа.")

def make_request(url, method, data):
    if method == 'GET':
        response = requests.get(url, params=data)
    elif method == 'POST':
        response = requests.post(url, json=data)
    else:
        raise ValueError('Unsupported method')

    return response

def process_response(response, input_data, operation):
    # Проверяем успешность запроса
    if response.status_code == 200:
        data = response.json()
        if 'result' in data:
            result = data['result']
            print(f"Результат {operation} {input_data}: {result}")
        else:
            print("Ошибка: Не удалось получить результат")
    else:
        print(f"Ошибка при обращении к API для операции {operation} {input_data}: {response.text}")

if __name__ == "main":
    main()
