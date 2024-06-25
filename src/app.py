from flask import Flask, render_template, redirect, url_for, request
from .models import db, Sign
import uuid

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///signs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_request
def before_request():
    if not hasattr(app, 'db_initialized'):
        db.create_all()
        app.db_initialized = True

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/landing')
def landing():
    return render_template('landing.html')

@app.route('/templetes')
def templates():
    return render_template('elements.html')

@app.route('/<sign_id>')
def show_sign(sign_id):
    sign = Sign.query.get(sign_id)
    if sign:
        return render_template('sign.html', sign=sign)
    else:
        return "Sign not found", 404

@app.route('/create', methods=['GET', 'POST'])
def create_sign():
    if request.method == 'POST':
        sign_id = str(uuid.uuid4())
        
        new_sign = Sign(
                    id=sign_id, 
                    opening_time=request.form['opening-time'], 
                    closing_time=request.form['closing-time'],
                    is_open_monday = True if request.form.get('od-monday', False) == 'on' else False,
                    is_open_tuesday = True if request.form.get('od-tuesday', False) == 'on' else False,
                    is_open_wednesday = True if request.form.get('od-wednesday', False) == 'on' else False,
                    is_open_thursday = True if request.form.get('od-thursday', False) == 'on' else False,
                    is_open_friday = True if request.form.get('od-friday', False) == 'on' else False,
                    is_open_saturday = True if request.form.get('od-saturday', False) == 'on' else False,
                    is_open_sunday = True if request.form.get('od-sunday', False) == 'on' else False
                    )
        db.session.add(new_sign)
        db.session.commit()
        return redirect(url_for('show_sign', sign_id=sign_id))
    return render_template('create_sign.html')
