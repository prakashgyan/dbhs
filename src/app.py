from flask import Flask, render_template, redirect, url_for, request, jsonify
from .models import db, Sign
import uuid
from datetime import datetime, timedelta  
# import pytz  

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
        return render_template('sign.html', sign=sign, sign_id=sign_id)
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


@app.route('/get_schedule_info')  
def get_schedule_info():  
    sign_key = request.args.get('sign_key', default = "", type = str)  
    local_time = request.args.get('local_time', default = "", type = str)  
    local_time = datetime.strptime(local_time, '%Y-%m-%dT%H:%M:%S.%fZ')  # assuming local time is sent as a string in ISO format  
  
    weekday = local_time.strftime('%A').lower()  
  
    sign = Sign.query.filter_by(id=sign_key).first()  
  
    if getattr(sign, f'is_open_{weekday}'):  
        open_time = datetime.strptime(sign.opening_time, '%H:%M')  
        close_time = datetime.strptime(sign.closing_time, '%H:%M')  
  
        if open_time.time() <= local_time.time() <= close_time.time():  
            state = 'OPEN'  
            change_time = local_time.replace(hour=close_time.hour, minute=close_time.minute) - local_time  
        else:  
            state = 'CLOSED'  
            change_time = local_time.replace(hour=open_time.hour, minute=open_time.minute) - local_time  
    else:  
        state = 'CLOSED'  
        change_time = timedelta(days=1)  
  
    return jsonify({'state': state, 'change_time': str(change_time.total_seconds() // 3600)})  

