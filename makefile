install: # Установить пакет
	poetry install

build: # Собрать проект
	poetry build

publish: # Опубликовать проект
	poetry publish --dry-run

package-install: # Установить проект
	python3 -m pip install --user dist/*.whl

brain-games: # Запустить brain-games
	poetry run brain-games

