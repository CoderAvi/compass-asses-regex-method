# compass-asses-regex-method
Built an API using Flask to receive a JSON payload via POST request for checking the input string for any SQL injection characters and in result it return a JSON response stating that given input is sanitized or unsanitized. Wrote unit test cases as well using pytest.

In this project i have used the regular expression method to check whether the given input consist any characters that can be used for SQL injection. i have used `r'[\';"=]'` for checking the presence of characters like single quote('), semicolon(;), double quote("), and equal sign (=) in the input string because these characters are commonly used in AQL injection attempts.

For this project i have created one virtual env and inside that i have installed Flask , pytest for running and testing this project successfully without having anyt dependency from system environment.

To run the API on local use command -- python app.py or flask run
To run the unit test case use command -- pytest test_app.py
