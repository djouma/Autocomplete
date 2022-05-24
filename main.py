import os, json
from app import app
from collections import Counter
from flask import Flask, jsonify, request, redirect, render_template
	
@app.route('/')
def upload_form():
	return render_template('autocomplete.html')

@app.route('/search', methods=['POST'])
def search():
	
	term = request.form["q"]
	print ('term: ', term)
	
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	json_url = os.path.join(SITE_ROOT, "data", "results.json")
	json_data = json.loads(open(json_url).read())
	
	filtered_dict = [v for v in json_data if term.casefold() in v.casefold()]	
	res = [key for key, value in Counter(filtered_dict).most_common()]
	res = str(res[:4])
	resp = jsonify(res)
	resp.status_code = 200
	print(res)
	return resp


if __name__ == "__main__":
    app.run()