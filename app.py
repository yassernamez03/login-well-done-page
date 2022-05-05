from dbroles import Role, app,User,db
from flask import redirect, render_template, session, url_for
from classes import Login,Signup


app.config['SECRET_KEY'] = '210398r7214311#!#r!r*'

@app.route('/')
def home():
    if "user" in session:
        return render_template("users.html",users=User.query.all())
    return redirect(url_for('login'))
@app.route('/login',methods=['POST','GET'])
def login():
    form = Login()
    print('hi')
    if form.validate_on_submit():
        name = form.name.data
        x = User.query.filter_by(name=name).first()
        if x == None:
            return redirect(url_for('signup'))
        elif x.role_id == 1:
            session['user'] = x.name
            return redirect(url_for('home'))
        else:
            return f"you cant go in you dont have a role Dmin"  
    return render_template('login.html',form=form)


@app.route('/signup',methods=['POST','GET'])
def signup():
    form = Signup()
    if form.validate_on_submit():
        if form.name.data == 'God':
            u = User(name=form.name.data,password=form.password.data,email=form.email.data,role_id=1)
            db.session.add(u)
            db.session.commit()
        else:
            u = User(name=form.name.data,password=form.password.data,email=form.email.data,role_id=2)
            db.session.add(u)
            db.session.commit()
        return redirect(url_for('login'))
    return render_template("signup.html",form=form)

@app.route('/logout')
def logout():
    if "user" in session :
        session.pop("user")
    return redirect(url_for('home'))  
    
if __name__=="__main__":
    app.run(debug=True)



