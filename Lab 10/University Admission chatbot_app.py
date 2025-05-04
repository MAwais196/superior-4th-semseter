from flask import Flask, render_template, request, jsonify
from chatbot_Logic import process_message
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html', initial_message=process_message("hi"))

@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        user_message = request.form.get('message', '')
        print(f"Received message: {user_message}")  # Server-side logging
        return jsonify({'response': process_message(user_message)})
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'response': "Sorry, I encountered an error"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)