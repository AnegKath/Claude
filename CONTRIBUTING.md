# CONTRIBUTING

Привет. Это приватный репо OmniConvert. Прочитай этот файл целиком до того как начнёшь кодить — здесь правила, нарушение которых уронит проект или его SEO-стратегию.

---

## TL;DR

- **Никогда не пушь напрямую в `main`.** Только через PR.
- Каждая задача = отдельная ветка `feat/<short-name>` или `fix/<short-name>`.
- Перед тем как взять задачу — напиши в чат, что её берёшь. Чтобы не дублировались.
- Если что-то непонятно или библиотека не работает в браузере — **спроси, не импровизируй**.
- Комментарии и текст в чате — по-русски. Код, имена файлов, идентификаторы, commit messages, PR title/body — по-английски.

---

## Hard anti-patterns (не нарушать без согласования)

Это правила из [docs/00_strategy/omniconvert-brief.md](docs/00_strategy/omniconvert-brief.md). Любое их нарушение = отклонённый PR.

1. **Никакого React / Next / Svelte / Vue.** Только vanilla JS ESM-модули. Alpine.js или Petite Vue допустимы только для сложного UI и только после согласования.
2. **Никаких серверных конвертеров.** Все преобразования файлов происходят в браузере. Сервер не должен принимать файлы пользователя ни при каких условиях. Это убьёт privacy-нарратив и положит сервер.
3. **Никаких заглушек или незаконченных инструментов в проде.** Если инструмент не работает полностью — `available=false` в seed, его нет в sitemap и в навигации.
4. **Никаких generic-шаблонных гайдов.** Каждый гайд уникален, ≥600 слов, осмысленный текст (не AI-вода).
5. **AdSense не активируется до 1000 визитов/мес.** Слоты в коде разметить можно, скрипт не подключать.
6. **Никаких глобальных `COOP`/`COEP` заголовков.** Только на тех роутах, которым реально нужен `SharedArrayBuffer` (FFmpeg.wasm). Глобально — ломает AdSense.
7. **FFmpeg.wasm и Tesseract.js не загружаются на `DOMContentLoaded`.** Только по клику пользователя на «Start». Иначе вес страницы убивает Lighthouse и Core Web Vitals.
8. **URL без query-параметров для основных страниц.** Чистые `/tools/<slug>`, не `?from=mp3&to=wav`.
9. **Не коммитим:** `.env`, `*.duckdb`, `*.duckdb.wal`, `node_modules/`, `venv/`, `__pycache__/`. Проверяет `.gitignore`, но всё равно следи глазами.
10. **Никаких CDN для критичных JS-библиотек.** Все vendor-библиотеки лежат локально в `static/vendor/`. Это уже сделано — не меняй.
11. **Phase gating.** Проект разбит на Phase 0–5. Сейчас Phase 1. Не делай ничего из будущих фаз без согласования. Если не уверен — спроси.

---

## Workflow

### 1. Перед тем как начать

```bash
git checkout main
git pull
git checkout -b feat/<short-task-name>
```

Имя ветки — по-английски, kebab-case, отражает суть. Примеры:
- `feat/base64-js-module`
- `feat/sql-formatter-guide`
- `fix/sitemap-missing-locale`
- `docs/contributing-tweaks`

### 2. Пока кодишь

- Делай маленькие, осмысленные коммиты. Один коммит = одна логическая единица.
- Commit message — по-английски, в imperative mood: `add base64 js module`, не `added` и не `adding`.
- Не смешивай рефакторинг и фичу в одном коммите.
- Перед каждым коммитом запусти `pytest -q` — должно быть зелёным.

### 3. Открываешь PR

```bash
git push -u origin feat/<short-task-name>
```

Идёшь на github.com → Compare & pull request. В описании:

- **Что сделал** (1–3 пункта)
- **Что НЕ делал** (если scope мог расползтись)
- **Как проверить** (команды/URL'ы)
- **Связанная задача** из [docs/FIRST_TASKS.md](docs/FIRST_TASKS.md) или phase-плана

PR должен быть **маленьким**. Если ты потратил больше дня на одну ветку — скорее всего scope раздулся, остановись и обсуди.

### 4. Review

- Один аппрув от @klaschukk обязателен. Без него merge не пройдёт.
- На замечания в review отвечаешь в треде, не «ну я вот так подумал». Аргумент → правка → запрос re-review.
- Не делай force-push в общий PR без явной просьбы.
- После merge — удали ветку (GitHub предложит кнопку).

### 5. Никогда

- Не пуш в `main` напрямую.
- Не делай `git push --force` в `main` (он защищён).
- Не мержи свой собственный PR без апрува.
- Не комить `.env`, `*.duckdb`, ключи, токены. Если случайно закомитил — скажи СРАЗУ, не пытайся «тихо переписать историю».

---

## Стиль кода

### Python

- Python 3.12.
- Прямые SQL-запросы к DuckDB через cursor, **только параметризованные** `?`-плейсхолдеры. Никакой f-string-конкатенации в SQL.
- Никаких ORM.
- Никаких generic-абстракций «на будущее». Three similar lines is better than a premature abstraction.
- Комментарии в коде — только если объясняют **почему**, не **что**. Имя функции уже говорит что.
- Имена — английские, snake_case для функций/переменных, PascalCase для классов.

### JavaScript

- ES modules (`import`/`export`), `type="module"` в `<script>`.
- Без зависимостей в рантайме. Vendor-библиотеки — из `static/vendor/`, не из npm-import.
- Не оборачивай всё в классы. Простые функции > классы.
- Lazy-load тяжёлых либ (FFmpeg, Tesseract) — только по клику пользователя.

### CSS

- Один файл `static/css/app.css`, mobile-first.
- 0 `!important`.
- CSS-переменные из [docs/06_tech/DESIGN.md](docs/06_tech/DESIGN.md).
- Без Tailwind на Phase 1.

### HTML / Jinja

- Семантика: `<main>`, `<article>`, `<nav>`, `<button>` (не `<div onclick>`).
- `aria-*` где осмысленно (lang switcher, кнопки без текста).
- `:focus-visible` стили — обязательно.

---

## Где что лежит

- **Маршруты:** `omniconvert/routes/`
- **Модели данных:** `omniconvert/models/`
- **Сервисы (SEO, sitemap, telegram):** `omniconvert/services/`
- **i18n словари:** `omniconvert/i18n/{en,ru,sr}.json`
- **Шаблоны:** `templates/`. Партиалы — в `templates/partials/`. Виджеты инструментов — `templates/tools/widget_<slug>.html`.
- **CSS:** `static/css/app.css`
- **JS-ядро:** `static/js/core.js`. JS-модули инструментов — `static/js/tools/<slug>.js`.
- **Вендорные либы:** `static/vendor/<lib>/` (НЕ ТРОГАТЬ без согласования).
- **Seed-данные:** `data/seed/tools.json`, `format_pairs.json`, `guides/*.md`.
- **Тесты:** `tests/test_*.py`.
- **Документация продукта:** `docs/00_strategy/`, `docs/06_tech/`.

---

## Если застрял

1. Перечитай [docs/06_tech/phase1-plan.md](docs/06_tech/phase1-plan.md).
2. Если библиотека не работает в браузере, конфликт с anti-patterns, или непонятно что делать — **остановись и спроси в чате**. Не придумывай workaround сам — это явное правило проекта.
3. Если PR ревью затягивается — пинг в чат.

---

Спасибо что читаешь. Удачи.
