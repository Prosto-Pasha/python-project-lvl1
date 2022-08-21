install: # Установить пакет
	poetry install

build: # Собрать пакет
	poetry build

publish: # Опубликовать пакет
	poetry publish --dry-run

package-install: # Установить пакет
	python3 -m pip install --user dist/*.whl

package-reinstall: # Переустановить пакет
	python3 -m pip install --force-reinstall --user dist/*.whl

make lint: # Проверить пакет
	poetry run flake8 brain_games

brain-games: # Запустить brain-games
	poetry run brain-games

brain-even: # Запустить игру 'Проверка на чётность'
	poetry run brain-even

brain-calc: # Запустить игру 'Калькулятор'
	poetry run brain-calc
