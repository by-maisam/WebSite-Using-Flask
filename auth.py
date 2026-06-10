from flask import Blueprint ,render_template, request ,flash

auth = Blueprint('auth',__name__)
@auth.route('/login' ,methods=['GET' ,'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html" ,boolean=True)
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"
@auth.route('/signup' ,methods=['GET' ,'POST'])
def signup():
    if request.method=='POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        p1 = request.form.get('password1')
        p2 = request.form.get('password2')
        if len(email)<4:
            flash('email is too short' , category='error')
        elif len(firstname)<4:
            flash('first name is too short' , category='error')
    return render_template("signup.html")