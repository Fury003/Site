from flask import Blueprint , render_template , request , flash

auth = Blueprint('auth' , __name__)

@auth.route("/login" , methods=['GET' , 'POST'])
def login():
    return render_template("login.html" , test='lala' )

@auth.route('/sign-up' , methods=['GET' , 'POST'])
def sign_up():
    if request.method == "POST" :
        #getting the sign up information 
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        userName = request.form.get('userName')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #cheking the sign up information 
        if len(firstName) <2 :
            flash('Your First Name is inccorect', category='error')
        elif len(lastName) <2 :
            flash('Your Last Name is inccorect', category='error') 
        elif len(userName) < 2 :
            flash('Your user name must be between 2 and 14 characters')
        elif len(userName) > 14 :
            flash('Your user name must be between 2 and 14 characters')
        elif len(email) < 4:
            flash('Incorrect email', category='error')
        elif password1 != password2 :
            flash("Your password don't match" , category='error')
        elif len(password1) <8:
            flash('Your password is too short' , category='error')
        else :
            #add user to database 
            flash('Account created!' , category='valid')
            pass

    return render_template("sign_up.html")

@auth.route('/logout')
def logout() :
    return "<p>Logout</p>"

""" #vreau sa fie fara spatii ca un username dar sa includa caracterele de genu _* .......
elif userName.isalnum == False :
    flash('Your user name must be between 2 and 14 characters')"""

""" nu merg nu stiu dc 
elif firstName.isalpha() == False :
    flash('Invalid First 2 name' , category='error')
elif lastName.isalpha() == False :
    flash('Invalid last name' , category='error')
"""