from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def is_sanitized(input_string):
    # for checking characters which can be used for SQL injection by using a simple regular expression concept
    sql_injection_pattern = re.compile(r'[\';"=]')
    if sql_injection_pattern.search(input_string):
        return False
    return True

@app.route('/v1/sanitized/input/', methods=['POST'])
def check_sanitization():
    try:
        data = request.get_json()

        # for checking if the 'input' key is present in the JSON payload
        input_string = data.get('input')

        if input_string is None:
            #For handling edge cases like missing 'input' key
            return jsonify({'error': 'Missing input key'}), 400

        if not input_string.strip():
            # For handling the cases where 'input' value can be empty
            return jsonify({'error': 'Empty input value'}), 400

        if is_sanitized(input_string):
            result = {'result': 'sanitized'}
        else:
            result = {'result': 'unsanitized'}

        return jsonify(result)

    except Exception as e:
        app.logger.error(f"Error in check_sanitization route: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500


if __name__ == '__main__':
    #For Running the Flask application on port 5000
    app.run(debug=True, port=5000)
