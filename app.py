from flask import Flask, render_template, request, current_app
from espnff import League
app = Flask(__name__)


with app.app_context():
	current_app.jinja_env.line_statement_prefix = '%'

@app.route('/', methods=['POST', 'GET'])
def hello():
	if request.method == 'POST':
		if request.form['league_id'] and request.form['league_year']:
			league_id, league_year = request.form['league_id'], request.form['league_year']
			league = League(league_id, league_year)
			return render_template('main.html', league=league)
		return render_template('main.html')
	return render_template('main.html')


if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5000)
