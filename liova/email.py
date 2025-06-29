import difflib
import os
import openai
from flask import Blueprint, render_template, request
from flask_login import login_required

email_bp = Blueprint('email', __name__)


@email_bp.route('/refactor', methods=['GET', 'POST'])
@login_required
def refactor():
    original = ''
    refactored = ''
    diff = ''
    if request.method == 'POST':
        original = request.form['email']
        refactored = refactor_email(original)
        diff = generate_diff(original, refactored)
    return render_template('refactor.html', original=original,
                           refactored=refactored, diff=diff)


def refactor_email(text: str) -> str:
    """Use OpenAI API to refactor email text."""
    try:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "Refactor the email for clarity and professionalism."},
                     {"role": "user", "content": text}],
            temperature=0.3,
        )
        return response.choices[0].message['content'].strip()
    except Exception:
        return text


def generate_diff(a: str, b: str) -> str:
    diff = difflib.ndiff(a.splitlines(), b.splitlines())
    return '\n'.join(diff)
