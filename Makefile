.PHONY: dev django tailwind install static

dev:
	make -j2 tailwind django

django:
	uv run python manage.py runserver

tailwind:
	npm run dev

install:
	uv sync
	npm install

static:
	npm run build
	uv run python manage.py collectstatic --noinput