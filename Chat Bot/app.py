from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key='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')
messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if user_input:
        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        if response and response.choices:
            reply = response.choices[0].message.content
            messages.append({"role": "assistant", "content": reply})
            return jsonify({"reply": reply})

    return jsonify({"error": "Invalid input or response not received"})

if __name__ == '__main__':
    app.run(debug=True)
