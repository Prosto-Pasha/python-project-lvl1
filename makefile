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

brain-games: # Запустить brain-games
	poetry run brain-games

