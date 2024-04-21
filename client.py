import requests

def main():
    numbers = input("Введите одно или два числа через пробел: ").split()

    if len(numbers) == 1:
        # Если введено одно число, отправляем запрос на вычисление квадратного корня
        number = numbers[0]
        response = requests.get('http://localhost:5000/sqrt', params={'base': number})
        process_response(response, number, "квадратного корня")
    elif len(numbers) == 2:
        # Если введены два числа, отправляем запрос на возведение в степень
        base, exponent = numbers
        response = requests.get('http://localhost:5000/pow', params={'base': base, 'exp': exponent})
        process_response(response, f"{base} в степени {exponent}", "степени")
    else:
        print("Пожалуйста, введите одно или два числа.")

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
        print(f"Ошибка при обращении к API mainapp для операции {operation} {input_data}")

if __name__ == "__main__":
    main()
