from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/contact', methods=['POST'])
def contact():
    data = request.form
    print(data)
    return jsonify({'message': 'Contact form submitted successfully!'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
