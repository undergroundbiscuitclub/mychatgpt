from flask import Flask, render_template, request, session
from flask_session import Session
import openai
import os

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)
openai.api_key = os.environ.get('OPENAI_API_KEY')
ssl_enabled = os.environ.get('SSL_ENABLED')
ssl_self_signed = os.environ.get('SSL_SELF_SIGNED')

Session(app)

@app.route('/')
def index():
    if 'messages' not in session:
        session['messages'] = []
    return render_template('index.html', messages=session['messages'])


@app.route("/generate-response", methods=["POST"])
def generate_response():
    user_message = request.form["prompt"]
    gpt_version = request.form["gpt_version"]  # Get the GPT version from the form data

    # Validate the GPT version and set the model accordingly
    if gpt_version == "gpt-4":
        model = "gpt-4"
    else:
        model = "gpt-3.5-turbo"
    if 'messages' not in session:
       session['messages'] = []
    session['messages'].append({"role": "user", "content": user_message})

    response = openai.ChatCompletion.create(
        model=model,
        messages=session['messages'],
#        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.8
    )

    response_text = response.choices[0].message["content"].strip()
    session['messages'].append({"role": "assistant", "content": response_text})

    return response_text

@app.route('/clear', methods=['POST'])
def clear():
    session.clear()
    return ''

if __name__ == "__main__":
    if ssl_enabled == "1":
        if ssl_self_signed == "1":
            app.run(debug=False, host="0.0.0.0", ssl_context=('adhoc'))
        else:
            app.run(debug=False, host="0.0.0.0", ssl_context=('ssl/cert.pem', 'ssl/key.pem'))
    else:
        app.run(debug=False, host="0.0.0.0")
