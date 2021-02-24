from flask import *
from search import search
from excel import convert
import pyrebase

config = {
    "apiKey": "AIzaSyBCIbtpg5Yavq_GmwhbRTPZfTC9sie68Xw",
    "authDomain": "tracker-46be3.firebaseapp.com",
    "databaseURL": "https://tracker-46be3-default-rtdb.firebaseio.com",
    "projectId": "tracker-46be3",
    "storageBucket": "tracker-46be3.appspot.com",
    "messagingSenderId": "72969024232"
}


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__)



# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if(request.method == 'POST'):
#         some_json = request.get_json()
#         return jsonify({'you sent': some_json}), 201
#     else:
#         return jsonify({"about": "Hellow World!"})


# @app.route('/multi/<int:num.', methods=['GET'])
# def get_multiply10(num):
#     return jsonify({'result': num*10})

# @app.route('/')
# def hello_world():
#     try:
#     # To sign in user using email and password
#         sign_user=auth.sign_in_with_email_and_password(
#             "Parasmani300@gmail.com", "1234567")

#         # before the 1 hour expiry:
#         sign_user=auth.refresh(sign_user['refreshToken'])
#         # now we have a fresh token
#         print(sign_user['idToken'])
#         session['user']=sign_user['idToken']
#         print("sign In Successfull")

#         #Sending the account confirmation mail to the user email on successfull sign in
#         # auth.send_email_verification(sign_user['idToken'])
#     except:
#         print("Some thing happend!! could not sign in")
#     return render_template('index.html')

# @ app.route('/reset_password')
# def reset():
#     token=session['user']
#     # Sending Password reset email
#     reset_email=auth.send_password_reset_email("Parasmani300@gmail.com")
#     return render_template("index.html")


@app.route("/api/regPerson", methods=['POST', 'GET'])
def regPerson():
    try:
        if request.method == 'POST':
            if request.form['submit'] == 'add':

                fname = request.form['fname']
                lname = request.form['lname']
                email = request.form['email']
                semail = request.form['semail']
                phone = request.form['phone']
                mphone = request.form['mphone']
                address = request.form['address']
                city = request.form['city']
                province = request.form['province']
                postal = request.form['postal']
                supportlvl = request.form['supportlvl']
                volunteer = request.form['volunteer']
                tag = request.form['tag']

                # sending data to db
                db.child('people').push({'fname': fname, 'lname': lname, "email": email, "semail": semail,
                                         "phone": phone, "mphone": mphone, "address": address, "city": city, "province":province, 'postal': postal, 'supportlvl': supportlvl, "volunteer": volunteer, 'tag':tag})
                
                # displaying existing data
                people = db.child("people").get()
                to = people.val()
                return render_template('regPerson.html', t=to.values())
            elif request.form['submit'] == 'file':
                if request.files:
                    file = request.files["file"]
                    convert(file)

                    return render_template('regPerson.html')
                return render_template('regPerson.html')
            return render_template('regPerson.html')
        return render_template('regPerson.html')

    except:
        raise Exception('Error: Cannot add data.')


@app.route("/api/searchPerson", methods=['GET', 'POST'])
def searchPerson():
    try:
        if request.method == 'POST':
            if request.form['submit'] == 'search':

                lname = request.form['lname']
                fname = request.form['fname']
                email = request.form['email']
                city = request.form['city']
                phone = request.form['phone']
                tag = request.form['tag']

                # recieving all data from db
                data = db.child("people").get()

                # creatting new array with values of people
                result = data.val().values()


                #filtering and retturning new array
                if lname != "":
                    result = search(result, 'lname', lname)
                if fname != "":
                    result = search(result, 'fname', fname)
                if email != "":
                    result = search(result, 'email', email)
                if city != "":
                    result = search(result, 'city', city)
                if phone != "":
                    result = search(result, 'phone', phone)
                if tag != "":
                    result = search(result, 'tag', tag)
                    
                    
                return render_template('search.html', t=result)
            elif request.form['submit'] == 's':

                lname = request.form['lname']
                data = db.child("people").get()
                result = data.val().values()
                if lname != "":
                    result = search(result, 'lname', lname)
                return render_template('search.html', t=result)
            else:
                return render_template('search.html')
            return render_template('search.html')
        return render_template('search.html')
    except:
        raise Exception('Error: Cannot get data.')



@app.route('/api/updatePerson', methods=['GET', 'POST'])
def updatePerson():
    try:
        if request.method == 'POST':
            if request.form['submit'] == 'update':
                
                
                id = request.form['idd']
                fname = request.form['fname']
                lname = request.form['lname']
                email = request.form['email']
                semail = request.form['semail']
                phone = request.form['phone']
                mphone = request.form['mphone']
                address = request.form['address']
                city = request.form['city']
                province = request.form['province']
                postal = request.form['postal']
                supportlvl = request.form['supportlvl']
                volunteer = request.form['volunteer']
                tag = request.form['tag']
               
                if fname != "":
                    data = db.child('people').child(
                        id).update({"fname": fname})
                if lname != "":
                    data = db.child('people').child(
                        id).update({"lname": lname})
                if email != "":
                    data = db.child('people').child(
                        id).update({"email": email})
                if semail != "":
                    data = db.child('people').child(
                        id).update({"semail": semail})
                if phone != "":
                    data = db.child('people').child(
                        id).update({"phone": phone})
                if mphone != "":
                    data = db.child('people').child(
                        id).update({"mphone": mphone})
                if address != "":
                    data = db.child('people').child(
                        id).update({"address": address})
                if city != "":
                    data = db.child('people').child(
                        id).update({"city": city})
                if province != "":
                    data = db.child('people').child(
                        id).update({"province": province})
                if postal != "":
                    data = db.child('people').child(
                        id).update({"postal": postal})
                if supportlvl != "":
                    data = db.child('people').child(
                        id).update({"supportlvl": supportlvl})
                if volunteer != "":
                    data = db.child('people').child(
                        id).update({"volunteer": volunteer})
                if tag != "":
                    data = db.child('people').child(
                        id).update({"tag": tag})
                

                data = db.child('people').child(id).get()
                
                snapshot = data.val()
                
                return render_template('update.html', t=snapshot)

            elif request.form['submit'] == 'remove':
                id = request.form['idd']
                db.child("people").child(id).remove()
                return render_template('update.html' )
          

            else:
                return render_template('update.html')
            return render_template('update.html')
        return render_template('update.html')
        

    except:
        raise Exception('Error: Cannot update data.')


@app.route('/api/createTag', methods=['GET', 'POST'])
def createTag():
    try:
        if request.method == 'POST':
            if request.form['submit'] == 'find':

                id = request.form['id']

                data = db.child('people').child(id).get()
                snapshot = data.val().values()
                # array =  []
                # for i in snapshot:
                #     array.append(i)
                
                
                return render_template('createTag.html', t=snapshot)
            elif request.form['submit'] == 'create':

                tag = request.form['tag']
                id = request.form['id']

                data = db.child('people').child(
                    id).update({'tag':tag})

                data = db.child('people').child(id).get()
                snapshot = data.val().values()
                return render_template('createTag.html', t=snapshot)
            else:
                return render_template('createTag.html')
            return render_template('createTag.html')
        return render_template('createTag.html')
    except:
        raise Exception('Error: Cannot create tag.')




if __name__ == '__main__':
    app.run(debug=True)
 
