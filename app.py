from flask import Flask
from utils import *

app = Flask(__name__)


@app.route("/")
def page_index():
    """Главная страница."""

    candidates: list[dict] = load_candidates()
    result: str = get_all(candidates)
    return result


@app.route('/candidate/<int:uid>')
def page_candidate(uid):
    """Страница кандидата по ключу id."""

    candidate: dict = get_by_pk(uid)
    result: str = f'<img src="{candidate["picture"]}">'
    result += get_all([candidate])
    return result


@app.route('/skills/<skill>')
def page_skills(skill):
    """Страница кандидатов у которых есть один из навыков по ключу skills."""

    candidate: list[dict] = get_by_skill(skill.lower())
    result = get_all(candidate)
    return result


if __name__ == "__main__":
    app.run()
