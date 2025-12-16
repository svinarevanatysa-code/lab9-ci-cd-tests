# test_api.py - простой тест для CI/CD
import requests

def test_api_status():
    """Тест статуса API"""
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    assert response.status_code == 200
    print("✓ API возвращает статус 200")

def test_api_json_structure():
    """Тест структуры JSON ответа"""
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    data = response.json()
    
    # Проверяем обязательные поля
    assert 'id' in data
    assert 'title' in data
    assert 'body' in data
    
    # Проверяем типы данных
    assert isinstance(data['id'], int)
    assert isinstance(data['title'], str)
    assert isinstance(data['body'], str)
    
    print(f"✓ JSON структура корректна, id={data['id']}")

def test_api_multiple_posts():
    """Тест нескольких запросов"""
    for post_id in [1, 2, 3]:
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
        assert response.status_code == 200
    print("✓ Все 3 запроса успешны")

if __name__ == "__main__":
    test_api_status()
    test_api_json_structure()
    test_api_multiple_posts()
    print("\n✅ Все тесты прошли успешно!")
