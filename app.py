from flask import Flask, render_template, request, json
from cipher.vigenere import VigenereCipher

app = Flask(__name__)

@app.route('/')
def vigenere():
    return render_template('vigenere.html')

@app.route('/encrypt', methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = str(request.form['inputKeyCipher'])
    Vigenere = VigenereCipher()
    encrypt_text = VigenereCipher.vigenere_encrypt(text, key)
    return f"text: {text}<br/> key: {key}<br/> encrypted text: {encrypt_text}"

@app.route('/decrypt', methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = str(request.form['inputKeyCipher'])
    Vigenere = VigenereCipher()
    decrypted_text = Vigenere.decrypt(text, key)
    return f"text: {text}<br/> key: {key}<br/> decrypted text: {decrypted_text}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050, debug=True)
    