from flask import Flask, request, jsonify
import pyautogui
import os

app = Flask(__name__)

@app.route('/open_telegram', methods=['POST'])
def open_telegram():
    try:
        # Reemplaza 'Telegram' con la ruta al ejecutable de Telegram en tu sistema
        os.system("start telegram")  # Windows
        # os.system("open -a Telegram")  # macOS
        # os.system("telegram &")  # Linux
        return jsonify({'status': 'success', 'message': 'Telegram opened'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
