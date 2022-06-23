import email
from flask import *
import flask
from dbconnect import *
import os,sys
from werkzeug.utils import secure_filename

app=Flask(__name__)
app.secret_key="bnm"


@app.route('/')
def home():
    session.pop('_flashes', None)
    return render_template('home.html')

@app.route('/event')
def event():
    val=selectcond("select * from event where status=%s",("Approved"))
    return render_template('event.html',val=val)

@app.route('/logout')
def logout():
    session.pop('_flashes', None)
    
    session['email']=None
    return redirect('/')


@app.route('/Index',methods=['POST','GET'])
def index():
    session.pop('_flashes', None)

    if session['email']==None:
        return redirect('/login')
    if session['email']!=None:
        result=selectonecond("select * from login where email=%s ",(session['email']))
        result2=selectonecond("select * from admin where email=%s ",(session['email']))
        if result==None:
            if result2!=None:
                val=selectcond("select * from login where active=%s",('None'))
                session.pop('_flashes', None)
                flash("Welcome Admin")
                return render_template('Admin.html',val=val)
            else:
                session['email']==None
                session.pop('_flashes', None)
                flash("Invalid Email or Password")
                return render_template('Login.html',msg="Invalid Email or Password")
        else:
            if result[9]=='Active':
                return redirect('/Profile')
            elif result[9]=='rejected':
                session['email']!=None
                flash("Account is Rejected")
                return render_template('Login.html',msg="Account is Rejected")
                
            else:
                session['email']!=None
                session.pop('_flashes', None)
                flash("Account not activated")
                return render_template('Login.html',msg="Account not activated")
    


@app.route('/login')
def login():
    if session.get('email') is not None:
        return redirect('/Index')
    else:
        session.pop('_flashes', None)
        return render_template('Login.html')


@app.route('/register')
def register():
    if session.get('email') is not None:
        return redirect('/Index')
    else:
        session.pop('_flashes', None)
        return render_template('Registartion.html')
    

@app.route('/logincheck',methods=['POST','GET'])
def logincheck():
    session.pop('_flashes', None)
    if request.method != 'POST':
        return redirect('/Index')
    email=request.form['email']
    if email=='':
        return redirect('/Index')
    password=request.form['password']
    result=selectonecond("select * from login where email=%s and pass=%s",(email,password))
    result2=selectonecond("select * from admin where email=%s and pass=%s",(email,password))
    print(result)
    if result2!=None:
    
        print("admin")
        session['email']=email
        return redirect('/Index')
    
    elif result!=None:
        if result[9]=='Active':
            print("sesstion")
            session['email']=email
            return redirect('/Profile')
        elif result[9]=='rejected':
            session.pop('_flashes', None)
            flash("Account is Rejected")
            return render_template('Login.html')
        else:
            session.pop('_flashes', None)
            flash("Account not activated")
            return render_template('Login.html')
    else:
            session.pop('_flashes', None)
            flash("Invalid Email or Password")
            return render_template('Login.html')   
    
@app.route('/signupcheck',methods=['POST'])
def signup():
    email=request.form['email']
    password=request.form['password']
    name=request.form['name']
    gender=request.form['gender']
    regno=request.form['regno']
    admission=request.form['admission']
    phone=request.form['phone']
    department=request.form['department'] 
    year=request.form['year']
    photo=request.files['photo']
    phototname=secure_filename(photo.filename)
    photourl='../static/profileimage/'+phototname
    photo.save(os.path.join(app.root_path, 'static/profileimage/'+phototname))
    Active='None'
    result=iud("insert into login(Email,Pass,Name,Gender,Regno,Admissionno,Phoneno,Department,academicYear,Active,photo ) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(email,password,name,gender,str(regno),str(admission),str(phone),department,str(year),Active,photourl))
    return render_template('home.html')
@app.route('/Profile')
def Profile():
    if session['email']!=None:
        result=selectonecond("select * from login where email=%s",(session['email']))
        return render_template('Profile.html',result=result)
    else:
        return redirect('/')

@app.route('/update')
def update():
    if session['email']!=None:
        val=selectonecond("select * from login where email=%s",(session['email']))
        return render_template('update.html',val=val)
    else:
        return redirect('/')

@app.route('/updateprofile',methods=['POST'])
def updateprofile():
    email=request.form['email']
    if email!=None:
        result=iud("update login set email=%s where email=%s",(email,session['email']))
        session['email']=email
    password=request.form['password']
    if password!=None:
        result=iud("update login set Pass=%s where email=%s",(password,session['email']))
    name=request.form['name']
    if name!=None:
        result=iud("update login set Name=%s where email=%s",(name,session['email']))
    gender=request.form['gender']
    if gender!=None:
        result=iud("update login set Gender=%s where email=%s",(gender,session['email']))
    regno=request.form['regno']
    if regno!=None:
        result=iud("update login set Regno=%s where email=%s",(regno,session['email']))
    admission=request.form['admission']
    if admission!=None:
        result=iud("update login set Admissionno=%s where email=%s",(admission,session['email']))
    phone=request.form['phone']
    if phone!=None:
        result=iud("update login set Phoneno=%s where email=%s",(phone,session['email']))
    department=request.form['department'] 
    if department!=None:
        result=iud("update login set Department=%s where email=%s",(department,session['email']))
    year=request.form['year']
    if year!=None:
        result=iud("update login set academicYear=%s where email=%s",(year,session['email']))
    photo=request.files['photo']
    if photo.filename!=None:
        phototname=secure_filename(photo.filename)
        photourl='../static/profileimage/'+phototname
        photo.save(os.path.join(app.root_path, 'static/profileimage/'+phototname))
        result=iud("update login set photo=%s where email=%s",(photourl,session['email']))
    return redirect('/Index')

@app.route('/approved')
def approved():
    if session['email']!=None:
        val=selectcond("select * from login where  active=%s",("Active"))
        print(val)
        return render_template('approvedmembers.html',val=val)
    else:
        return redirect('/Index')

@app.route('/rejected')
def rejected():
    if session['email']!=None:
        val=selectcond("select * from login where  active=%s",("rejected"))
        print(val)
        return render_template('rejectedmembers.html',val=val)
    else:
        return redirect('/Index')



@app.route('/viewprofile/<id>')
def viewprofile(id):
    if session['email']!=None:
        result=selectonecond("select * from login where id=%s",(session['email']))
        return render_template('Profile.html',result=result)
    else:
        return redirect('/')



@app.route('/sucessuser/<id>')
def sucessuser(id):
    if session['email']!=None:
        val=iud("update login set active=%s where id=%s",("Active",id))
        return redirect('/Index')
    else:
        return redirect('/Index')

@app.route('/rejeactuser/<id>')
def rejeactuser(id):
    if session['email']!=None:
        val=iud("update login set active=%s where id=%s",("rejected",id))
        return redirect('/Index')
    else:
        return redirect('/Index')

@app.route('/Search')
def Search():
    if session['email']!=None:
        val=selectcond("select * from login where  active=%s and email!=%s",("Active",session['email']))
        return render_template('Search.html',val=val)
    else:
        return redirect('/Index')

@app.route('/rejectall')
def rejectall():
    if session['email']!=None:
        val=iud("update login set active=%s where active=%s",("rejected","None"))
        return redirect('/Index')
    else:
        return redirect('/Index')

@app.route('/activateall')
def activateall():
    if session['email']!=None:
        val=iud("update login set active=%s where active=%s",("Active","None"))
        return redirect('/Index')
    else:
        return redirect('/Index')




@app.route('/rejectallc')
def rejectallc():
    if session['email']!=None:
        val=iud("update login set active=%s where active=%s",("rejected","Active"))
        return redirect('/approved')
    else:
        return redirect('/Index')

@app.route('/activateallc')
def activateallc():
    if session['email']!=None:
        val=iud("update login set active=%s where active=%s",("Active","rejected"))
        return redirect('/rejected')
    else:
        return redirect('/Index')

@app.route('/addeventpage')
def addeventpage():
    if session['email']!=None:
        result=selectcond("select * from event where author=%s",(session['email']))
        return render_template('addevent.html',result=result)
    else:
        return redirect('/')

@app.route('/addevent',methods=['POST'])
def addevent():
    if request.form['ename']==None:
        session.pop('_flashes', None)
        result=selectcond("select * from event where author=%s",(session['email']))
        return redirect('/addeventpage')
    if session['email']!=None:
        name=request.form['ename']
        description=request.form['description']
        date=request.form['date']
        print(date)
        result=iud("insert into event(eventname,description,lastdate,author,status) values(%s,%s,%s,%s,%s)",(name,description,date,session['email'],"None"))
        session.pop('_flashes', None)
        flash("Addevent Sucessfully")
        result=selectcond("select * from event where author=%s",(session['email']))
        return redirect('/addeventpage')
    else:
        session.pop('_flashes', None)
        return redirect('/')

@app.route('/devent/<id>')
def devent(id):
    if session['email']!=None:

        result=iud("delete from event where id=%s",(id))

        if result==0:
            session.pop('_flashes', None)
            flash("Event to be deleted is not present")
            result=selectcond("select * from event where author=%s",(session['email']))
            return redirect('/addeventpage')
        session.pop('_flashes', None)
        flash("Delete Sucessfully")
        return redirect('/addeventpage')
    else:
        session.pop('_flashes', None)
        return redirect('/')


@app.route('/eventdisplay')
def eventdisplay():
    if session['email']!=None:
        result=selectcond("select * from event where status=%s",("None"))
        return render_template('eventapprovel.html',val=result)
    else:
        return redirect('/Index')

@app.route('/approveevent/<id>')
def approveevent(id):
    if session['email']!=None:
        val=iud("update event set status=%s where id=%s",("Approved",id))
        return redirect('/eventdisplay')
    else:
        return redirect('/Index')

@app.route('/rejectevent/<id>')
def rejectevent(id):
    if session['email']!=None:
        val=iud("update event set status=%s where id=%s",("rejected",id))
        return redirect('/eventdisplay')
    else:
        return redirect('/Index')


if __name__ == "__main__":
  app.run(debug=True)