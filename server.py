from flask import Flask, request, jsonify
import pyautogui
import os

app = Flask(__name__)

@app.route('/open_telegram', methods=['POST'])
def open_telegram():
    try:
        # Replace 'Telegram' with the path to your Telegram executable
        os.system("open -a Telegram")  # For macOS
        # os.system("start telegram")  # For Windows
        # os.system("telegram &")  # For Linux
        return jsonify({'status': 'success', 'message': 'Telegram opened'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
