# hadithbot_app.py
from flask import Flask, render_template, request, jsonify
from hadithbot_logic import process_hadith_message
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('hadith_index.html', 
                         initial_message=process_hadith_message("assalam"))

@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        user_message = request.form.get('message', '')
        print(f"Received message: {user_message}")
        return jsonify({'response': process_hadith_message(user_message)})
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'response': "Sorry, I encountered an error processing your Hadith request"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)