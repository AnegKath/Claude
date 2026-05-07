# OmniConvert

Браузерный хаб конвертеров файлов. Все преобразования происходят **в браузере пользователя** — файлы никуда не отправляются. Это и SEO-нарратив, и cost-модель проекта.

Стек: Flask 3 + Jinja2 + DuckDB (read-only) + vanilla JS ESM. Без React/Next/Svelte/Vue. Без CDN.

## Перед тем как что-то делать

Прочитай в таком порядке:

1. [CONTRIBUTING.md](CONTRIBUTING.md) — правила работы, hard anti-patterns, как открывать PR.
2. [docs/00_strategy/omniconvert-brief.md](docs/00_strategy/omniconvert-brief.md) — продуктовый бриф.
3. [docs/06_tech/phase1-plan.md](docs/06_tech/phase1-plan.md) — что делаем сейчас.
4. [docs/FIRST_TASKS.md](docs/FIRST_TASKS.md) — список изолированных задач, которые можно взять прямо сейчас.

## Quickstart

```bash
git clone git@github.com:klaschukk/convertor.git
cd convertor

python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
# открой .env, поставь SECRET_KEY (любая 32-байтная hex-строка) и FLASK_ENV=development

# первая инициализация БД (когда seed_db.py будет готов)
python scripts/seed_db.py

# dev-запуск
FLASK_ENV=development python -c "from wsgi import app; app.run(host='127.0.0.1', port=8003, debug=True)"

# прод-запуск (как на сервере)
gunicorn -w 2 --max-requests 500 -b 127.0.0.1:8003 wsgi:app

# тесты
pytest -q
```

После старта открывай http://127.0.0.1:8003.

## Структура

```
omniconvert/      # Flask app: routes, models, services, i18n
templates/        # Jinja2: base, partials, tools/widget_*.html
static/           # css, js, vendor (ffmpeg/tesseract/jspdf/mammoth/marked — локально, без CDN)
data/seed/        # tools.json, format_pairs.json, guides/*.md
docs/             # стратегия, бриф, phase-планы, DESIGN.md
infra/            # nginx, systemd
scripts/          # seed_db.py
tests/            # pytest
```
