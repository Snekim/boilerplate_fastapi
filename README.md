## 📦 Установка
### Локально без Docker
```
git clone git-url
cd yourproject
pyenv install $(cat .python-version)
pyenv local $(cat .python-version)
poetry install
poetry shell (!!!! Обязательно после версии poetry 2.0 необходимо установить poetry self add poetry-plugin-shell)
```

### Локально через Docker


## Запуск тестов
### Запуск всех тестов
```poetry run pytest```
### Запуск конкретного теста
```poetry run pytest tests/test_main.py::test_read_root -v```
### Запуск тестов с покрытием
```poetry run pytest --cov=app --cov-report=html```
## 🔍 Линтеры и форматирование
Проект использует ruff
### Проверка кода
```poetry run ruff check .```
### Автоисправление ошибок
```poetry run ruff check --fix .```
### Форматирование кода
```poetry run ruff format .```
### Проверка типов
```poetry run mypy .```
