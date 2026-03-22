from flask import Flask, render_template, request, session, redirect, jsonify
from DBConnection import Db
from qr import gen_qrcode

app = Flask(__name__)
app.secret_key = "super"
staticpath = "F:\\doc_backup\\web\\DOC_TAG\\static\\"

# login page
@app.route('/')
def login():
    return render_template('login index.html')

@app.route('/login_post', methods = ['post'])
def login_post():
    username = request.form['textfield']
    password = request.form['textfield2']
    db = Db()
    qry = "SELECT * FROM `login` WHERE  `Username` = '"+username+"' AND `Password` = '"+password+"'"
    res = db.selectOne(qry)
    if res is not None:
        session['lid'] = res['Login_id']
        if res['Login_type'] == 'admin':
            # return adm_home()
            return '''<script>window.location="/adm_home"</script>'''
        elif res['Login_type'] == 'authority':
            return redirect('/authority_home')
        else:
            return '''<script>alert('invalid password or username');window.location="/"</script>'''
    else:
        return '''<script>alert('invalid password or username');window.location="/"</script>'''


@app.route('/change_password')
def change_paswrd():
    return render_template('admin/change_password.html')

@app.route('/change_pswrd_post',methods=['post'])
def changePswrd_post():
    cur_pswrd =request.form['textfield']
    new_pswrd = request.form['textfield2']
    confirm_paswrd = request.form['textfield4']
    qry="SELECT * FROM `login` WHERE `Password`='"+cur_pswrd+"' AND `Login_type`='admin' "
    db = Db()
    res = db.selectOne(qry)
    print(res)
    if res is not None:
        if new_pswrd==confirm_paswrd:
            qry = "UPDATE `login` SET `Password` = '"+confirm_paswrd+"'  WHERE  `Login_id` = '"+str(session['lid'])+"'"
            res = db.update(qry)
            return redirect('/')
        else:
            '''<script>alert('invalid password or username');window.location="/"</script>'''
    else:
        '''<script>alert('invalid password or username');window.location="/"</script>'''



#---------------------admin
@app.route('/adm_home')
def adm_home():
    # return render_template('admin/home.html')
    return render_template('admin/adindex.html')

# adding authority
@app.route('/add_authority')
def add_authority():
    return render_template('admin/add authority.html')


@app.route('/add_authority_post', methods = ['post'])
def add_authority_post():
    name = request.form['textfield']
    phone = request.form['textfield2']
    city = request.form['textfield3']
    place = request.form['textfield4']
    post = request.form['textfield7']
    pin = request.form['textfield8']
    district = request.form['textfield5']
    state = request.form['textfield6']
    longitude = request.form['textfield9']
    latitude = request.form['textfield10']
    category = request.form['textfield11']
    description = request.form['textfield12']
    logo = request.files['textfield13']
    email = request.form['textfield14']
    db = Db()
    import datetime

    dd=datetime.datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
    logo.save("F:\\doc_backup\\web\\DOC_TAG\\static\\Logo\\"+dd)
    path="/static/Logo/"+dd

    import random
    pwd=str(random.randint(1000,10000))
    qry2 = "INSERT INTO login(Username,PASSWORD,Login_type) VALUES('"+email+"','"+pwd+"','authority')"
    lid=str(db.insert(qry2))
    qry = "INSERT INTO authority(Authority_name,Place,Post,Pin,District,State,Latitude,Longitude,Authority_lid,Category,City,Phone,Email,Description,Logo) VALUES ('"+name+"','"+place+"','"+post+"','"+pin+"','"+district+"','"+state+"','"+latitude+"','"+longitude+"','"+lid+"','"+category+"','"+city+"','"+phone+"','"+email+"','"+description+"','"+path+"')"
    print(qry)
    res = db.insert(qry)
    return '''<script>alert('authority added');window.location='/add_authority'</script>'''























# view authority
@app.route('/view_authority')
def view_authority():
    db = Db()
    qry="select * from authority"
    res=db.select(qry)
    return render_template('admin/view_authority.html',data=res)
@app.route('/view_authority_search', methods=['post'])
def view_authority_search():
    db = Db()
    name = request.form['textfield']
    qry="SELECT * FROM authority WHERE Authority_name LIKE '%"+name+"%'"
    res=db.select(qry)
    return render_template('admin/view_authority.html',data=res)





# editing authority
@app.route('/edit_authority/<id>')
def edit_authority(id):
    try:
        int(id)
    except ValueError:
        return adm_home()
    qry = "select * from authority where Authority_id='" + id + "'"
    db = Db()
    res = db.selectOne(qry)
    return render_template('admin/edit authority.html', data=res)


@app.route('/edit_authority_post', methods=['post'])
def edit_authority_post():
    authority_id = request.form['textid']
    name = request.form['textfield']
    phone = request.form['textfield2']
    city = request.form['textfield3']
    place = request.form['textfield4']
    post = request.form['textfield7']
    pin = request.form['textfield8']
    district = request.form['textfield5']
    state = request.form['textfield6']
    longitude = request.form['textfield9']
    latitude = request.form['textfield10']
    category = request.form['textfield11']
    description = request.form['textfield12']
    email = request.form['textfield3']
    if 'textfield13' in request.files:
        logo = request.files['textfield13']
        if logo.filename !="":
            import datetime
            dd = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
            logo.save("F:\\doc_backup\\web\\DOC_TAG\\static\\Logo\\" + dd)
            path = "/static/Logo/" + dd
            db = Db()
            qry = "UPDATE `authority` SET `Authority_name`= '"+name+"',`Place` = '"+place+"',`Post` = '"+post+"', `Pin` = '"+pin+"', `District` = '"+district+"', `State` = '"+state+"', `Latitude` = '"+latitude+"', `Longitude` = '"+longitude+"', `Category` = '"+category+"', `City` = '"+city+"', `Phone` = '"+phone+"', `Email` = '"+email+"', `Description` = '"+description+"', `Logo` = '"+path+"' where Authority_id = '"+authority_id+"'"
            res = db.update(qry)
        else:
            db = Db()
            qry = "UPDATE `authority` SET `Authority_name`= '" + name + "',`Place` = '" + place + "',`Post` = '" + post + "', `Pin` = '" + pin + "', `District` = '" + district + "', `State` = '" + state + "', `Latitude` = '" + latitude + "', `Longitude` = '" + longitude + "', `Category` = '" + category + "', `City` = '" + city + "', `Phone` = '" + phone + "', `Email` = '" + email + "', `Description` = '" + description + "' where Authority_id = '" + authority_id + "'"
            res = db.update(qry)

    else:
        db = Db()
        qry = "UPDATE `authority` SET `Authority_name`= '" + name + "',`Place` = '" + place + "',`Post` = '" + post + "', `Pin` = '" + pin + "', `District` = '" + district + "', `State` = '" + state + "', `Latitude` = '" + latitude + "', `Longitude` = '" + longitude + "', `Category` = '" + category + "', `City` = '" + city + "', `Phone` = '" + phone + "', `Email` = '" + email + "', `Description` = '" + description + "' where Authority_id = '" + authority_id + "'"
        res = db.update(qry)
    return view_authority()


@app.route('/delete_authority/<id>')
def delete_authority(id):
    qry="delete from authority where Authority_id='"+id+"'"
    db = Db()
    res = db.delete(qry)
    return '''<script>window.location='/view_authority'</script> '''

# feedback
@app.route('/view_feedback')
def feedback():
    db = Db()
    qry = "SELECT * FROM `feedback` INNER JOIN `user` ON `user`.`User_lid`=`feedback`.`User_lid`"
    res = db.select(qry)
    return render_template('admin/feedback.html',data=res)


@app.route('/view_feedback_post', methods=['post'])
def view_feedback_post():
    a = request.form["a"]
    b = request.form['b']
    db = Db()
    qry = "SELECT * FROM `feedback` INNER JOIN `user` ON `user`.`User_lid`=`feedback`.`User_lid` where date BETWEEN '"+a+"' and '"+b+"'"
    res = db.select(qry)
    return render_template('admin/feedback.html', data=res)



# view user
@app.route('/view_user')
def view_user():
    db = Db()
    qry = "SELECT * FROM `user`"
    res = db.select(qry)
    return render_template('admin/view user.html', data=res)

@app.route('/view_user_post', methods=['post'])
def view_user_post():
    db = Db()
    first_name = request.form['textfield']
    qry = "SELECT * FROM `user` WHERE `First_name` LIKE '%" + first_name + "%'"
    if ' ' in first_name:
        first_name, last_name = first_name.split(" ", 1)
        qry = "SELECT * FROM `user` WHERE `First_name` LIKE '%" + first_name + "%' AND `Last_name` LIKE '%" + last_name + "%'"

    res = db.select(qry)
    print(res)
    return render_template('admin/view user.html', data=res)

# view_report
@app.route('/report')
def report():
    db = Db()
    qry = "SELECT *,`authority`.`Phone` AS Aphone,`user`.`Phone` AS Uphone,`report`.`Status` AS Rstatus FROM `report` JOIN `user` ON `user`.`User_id` = `report`.`User_lid` JOIN `authority` ON `authority`.`Authority_lid` = `report`.`Authority_lid` JOIN `document` ON `document`.`Doc_id` = `report`.`Document_lid` ORDER BY Rstatus ASC"
    # qry = "SELECT `authority`.`Phone` AS aPhone,`authority`.*,`document`.*,`report`.*,`user`.* FROM `report` INNER JOIN `user` ON `report`.`User_lid`=`user`.`User_lid` JOIN `authority` ON `report`.`Authority_lid`=`authority`.`Authority_id` JOIN `document` ON `report`.`Document_lid`=`document`.`Doc_id` AND `document`.`User_lid`=`user`.`User_lid` AND `document`.`Authority_lid`=`authority`.`Authority_id`"
    res = db.select(qry)
    print(res)
    return render_template('admin/Report.html',data=res)


@app.route('/report_post', methods=['post'])
def report_post():
    db = Db()
    a = request.form["a"]
    b = request.form["b"]
    qry = "SELECT `authority`.`Phone` AS aPhone,`authority`.*,`document`.*,`report`.*,`user`.* FROM `report` INNER JOIN `user` ON `report`.`User_lid`=`user`.`User_lid` JOIN `authority` ON `report`.`Authority_lid`=`authority`.`Authority_id` JOIN `document` ON `report`.`Document_lid`=`document`.`Doc_id` AND `document`.`User_lid`=`user`.`User_lid` AND `document`.`Authority_lid`=`authority`.`Authority_id` AND `report`.`Status`='pending' where Date BETWEEN '"+a+"' and '"+b+"'"
    res = db.select(qry)
    print(res)
    return render_template('admin/Report.html',data=res)


# complaint
@app.route('/complaint')
def complaint():
    db = Db()
    qry = "SELECT * FROM `complaint` INNER JOIN `user` ON `user`.`User_lid`=`complaint`.`User_lid`"
    res = db.select(qry)
    return render_template('admin/view complaint.html',data=res)

@app.route('/view_complaint', methods=['post'])
def view_complaint():
    a = request.form["a"]
    b = request.form["b"]
    db = Db()
    qry = "SELECT * FROM `complaint` INNER JOIN `user` ON `user`.`User_lid`=`complaint`.`User_lid` where date BETWEEN '"+a+"' and '"+b+"'"
    res = db.select(qry)
    return render_template('admin/view complaint.html',data=res)

# reply
@app.route('/Reply/<id>')
def reply(id):
    return render_template('admin/Reply.html',id=id)

@app.route('/reply_post', methods = ['post'])
def reply_post():
    reply= request.form['textarea']
    cid = request.form['cid']
    qry="UPDATE `complaint` SET `Reply`='"+reply+"' , `Status`='Replied' WHERE `Complaint_id`='"+cid+"'"
    db=Db()
    db.update(qry)
    return complaint()

#-------------------------------------------------------------------------------------------------------------
#     authority

# authority home
@app.route('/authority_home')
def authority_home():
    return render_template('authority/auth_home.html')


@app.route('/auth_change_password')
def auth_change_password():
    return render_template('authority/change_password.html')

@app.route('/auth_change_pswrd_post',methods=['post'])
def auth_change_pswrd_post():
    cur_pswrd =request.form['textfield']
    new_pswrd = request.form['textfield2']
    confirm_paswrd = request.form['textfield4']
    qry="SELECT * FROM `login` WHERE `Password`='"+cur_pswrd+"' AND `Login_id` = '"+str(session['lid'])+"'"
    db = Db()
    res = db.selectOne(qry)
    print(res)
    if res is not None:
        if new_pswrd==confirm_paswrd:
            qry = "UPDATE `login` SET `Password` = '"+confirm_paswrd+"'  WHERE  `Login_id` = '"+str(session['lid'])+"'"
            res = db.update(qry)
            return redirect('/')
        else:
            '''<script>alert('invalid password or username');window.location="/auth_change_password"</script>'''
    else:
        '''<script>alert('invalid password or username');window.location="/auth_change_password"</script>'''



@app.route('/authority_details')
def authority_details():
    db = Db()
    qry = "SELECT * FROM `authority` WHERE `Authority_lid` = '"+str(session['lid'])+"' "
    res = db.selectOne(qry)
    print(res, session['lid'])
    return render_template("authority/authority_details.html", data=res)



# authority_view_user
@app.route('/authority_view_user')
def authority_view_user():
    db = Db()
    qry = "SELECT * FROM `user`"
    res = db.select(qry)
    return render_template('authority/view_user.html', data=res)

@app.route('/authority_view_user_post', methods=['post'])
def authority_view_user_post():
    db = Db()
    first_name = request.form['textfield']
    qry = "SELECT * FROM `user` WHERE `First_name` LIKE '%" + first_name + "%'"
    if ' ' in first_name:
        first_name, last_name = first_name.split(" ", 1)
        qry = "SELECT * FROM `user` WHERE `First_name` LIKE '%" + first_name + "%' AND `Last_name` LIKE '%" + last_name + "%'"


    res = db.select(qry)
    return render_template('authority/view_user.html', data=res)

# detailed_user_info
@app.route('/detailed_user_info/<id>')
def detailed_user_info(id):
    db = Db()
    qry = "SELECT * FROM `user` where `User_lid` = '" +id+"'"
    res = db.selectOne(qry)
    return render_template('authority/User_info.html', data=res)


@app.route('/view_document/<id>')
def view_document(id):
    db = Db()
    # qry = "SELECT * FROM `document` where `User_lid` = '" + +"'"
    # qry = "SELECT * FROM `document` JOIN `user` ON `user`.`User_lid` = `document`.`User_lid` WHERE `user`.`User_lid` = '"+id+"'"
    qry = " SELECT `document`.`Description` AS Ddescription, `Document_name`, `Date_of_issuing`, `Valid_till`, `Status`, `Category`, `Doc_id` FROM `document` JOIN `authority` ON `authority`.`Authority_lid` = `document`.`Authority_lid` JOIN `user` ON `user`.`User_lid` = `document`.`User_lid` WHERE `user`.`User_lid` = '"+id+"'"

    res = db.select(qry)
    return render_template('authority/view_document.html', data=res)

@app.route('/block_document/<id>')
def block_document(id):
    db = Db()
    qry = "UPDATE `document` SET `Status` = 'blocked' WHERE `Doc_id` = '"+id+"'"
    res = db.update(qry)
    return '''<script>alert('blocked successfully');window.location='/authority_view_user'</script> '''



@app.route('/add_document/<id>')
def add_document(id):
    return render_template('authority/add_document.html', data=id)

@app.route('/add_document_post', methods=['post'])
def add_document_post():
    document_name = request.form["textfield"]
    import time
    from _datetime import datetime
    path = request.files["fileField"]

    dt = datetime.now().strftime("%y%m%d-%H%M%S")
    path.save(staticpath+"document\\"+ dt +path.filename)
    url = "/static/document/"+ dt +path.filename
    print(path, url)

    description = request.form['textarea']
    print(description)
    date_of_issuing = request.form["textfield2"]
    valid_till = request.form["textfield3"]
    print(document_name, path, description, date_of_issuing, valid_till)
    db = Db()
    id = request.form["id"]
    qry = "INSERT INTO document(`User_lid`,`Authority_lid`,`Document_name`,`Description`,`Path`,`Status`,`Date_of_issuing`,`Valid_till`) VALUES ('"+id+"','"+str(session['lid'])+"', '"+document_name+"', '"+description+"', '"+url+"', '"+'available'+"', '"+date_of_issuing+"', '"+valid_till+"')"
    res = db.insert(qry)
    return render_template('authority/add_document.html', data=id)

@app.route('/authority_change_password')
def authority_change_password():
    return render_template('authority/change_password.html')

@app.route('/authority_view_report')
def authority_view_report():
    db = Db()
    qry = "SELECT *,`authority`.`Phone` AS Aphone,`user`.`Phone` AS Uphone,`report`.`Status` AS Rstatus, Report_id FROM `report` JOIN `user` ON `user`.`User_id` = `report`.`User_lid` JOIN `authority` ON `authority`.`Authority_lid` = `report`.`Authority_lid` JOIN `document` ON `document`.`Doc_id` = `report`.`Document_lid` ORDER BY Rstatus"
    res = db.select(qry)
    return render_template('authority/view_report.html', data=res)


@app.route('/authority_view_report_post', methods=['post'])
def authority_view_report_post():
    db = Db()
    a = request.form['a']
    b = request.form['b']
    qry = "SELECT *,`authority`.`Phone` AS Aphone,`user`.`Phone` AS Uphone,`report`.`Status` AS Rstatus FROM `report` JOIN `user` ON `user`.`User_id` = `report`.`User_lid` JOIN `authority` ON `authority`.`Authority_lid` = `report`.`Authority_lid` JOIN `document` ON `document`.`Doc_id` = `report`.`Document_lid` WHERE Date BETWEEN '"+a+"' AND '"+b+"'"
    res = db.select(qry)
    return render_template('authority/view_report.html', data=res)

@app.route('/report_status/<id>', methods=['post','get'])
def report_status(id):
    db = Db()
    qry = "UPDATE `report` SET `Status`='viewed' WHERE `Report_id`='" + id + "'"
    res = db.update(qry)
    return redirect("/authority_view_report")



###################################      ANDROID      #################

@app.route('/and_loginpost', methods=['POST'])
def and_login():
    db = Db()
    username=request.form['username']
    password=request.form['password']
    qry = "SELECT * FROM `login` WHERE `Username` = '"+username+"' AND `Password` = '"+password+"' AND `Login_type` = 'user'"
    res = db.selectOne(qry)
    if res is not None:
        qry2="SELECT * FROM `user` WHERE `User_lid`='"+str(res['Login_id'])+"'"
        db=Db()
        res2=db.selectOne(qry2)
        return jsonify(status="ok", data=res,lid=res['Login_id'],type=res['Login_type'],fname=res2['First_name'],lname=res2['Last_name'])
    else:
        return jsonify(status="no")

@app.route('/and_user_sign_in', methods=['POST'])
def and_user_sign_in():
    password = request.form['password']
    first_name = request.form['firstname']
    last_name = request.form['lastname']
    mothers_name = request.form['mothersname']
    fathers_name = request.form['fathersname']
    gender = request.form['gender']
    dob = request.form['dob']
    blood_group = request.form['bloodgroup']
    nationality = request.form['nationality']
    place_of_birth = request.form['pob']
    place = request.form['place']
    pin = request.form['pin']
    post = request.form['post']
    city = request.form['city']
    state = request.form['state']
    email = request.form['emailid']
    phone = request.form['phonenumber']
    adhar_no = request.form['aadharnumber']
    pancard_no = request.form['pancardnumber']
    qry = "INSERT INTO `login` (`Username`,`Password`,`Login_type`) VALUES ('"+email+"','"+password+"','user')"
    db = Db()
    lid = str(db.insert(qry))


    qry = "INSERT INTO `user`(`User_lid`,`First_name`,`Last_name`,`Gender`,`Dob`,`Blood_group`,`Place_of_birth`,`Place`,`Pin`,`Post`,`City`,`State`,`Mail_id`,`Phone`,`Adhar_no`,`Pancard_no`,`Nationality`,`Mother's_name`,`Father's_name`) VALUES ('"+lid+"','"+first_name+"','"+last_name+"','"+gender+"','"+dob+"','"+blood_group+"','"+place_of_birth+"','"+place+"','"+pin+"','"+post+"','"+city+"','"+state+"','"+email+"','"+phone+"','"+adhar_no+"','"+pancard_no+"','"+nationality+"', '"+mothers_name+"', '"+fathers_name+"')"
    res = db.insert(qry)
    gen_qrcode(lid)
    return jsonify(status="ok")



@app.route('/and_change_password', methods=['POST'])
def and_change_password():
    db = Db()
    lid = request.form['lid']
    current_password = request.form['old_password']
    change_password = request.form['new_password']
    qry="SELECT * FROM `login` WHERE `Password`='"+current_password+"' AND `Login_id`='"+lid+"' "
    db=Db()
    res=db.selectOne(qry)
    if res is not None:

        qry = "UPDATE `login` SET `Password` = '"+change_password+"' WHERE `Login_id` = '"+lid+"' AND `Password` = '"+current_password+"'"
        res = db.update(qry)
        return jsonify(status="ok")
    else:
        return jsonify(status="no")









@app.route('/and_view_profile', methods=['POST'])
def and_view_profile():
    lid = request.form['lid']
    db=Db()
    qry="SELECT * FROM `user` WHERE `User_lid`='"+lid+"'"
    res=db.selectOne(qry)
    return jsonify(status="ok",data=res)




@app.route('/and_edit_profile', methods=['POST'])
def and_edit_profile():
    db = Db()
    user_lid = request.form['lid']
    first_name = request.form['firstname']
    last_name = request.form['lastname']
    mothers_name = request.form['mothersname']
    fathers_name = request.form['fathersname']
    gender = request.form['gender']
    dob = request.form['dob']
    blood_group = request.form['bloodgroup']
    nationality = request.form['nationality']
    place_of_birth = request.form['pob']
    place = request.form['place']
    pin = request.form['pin']
    post = request.form['post']
    city = request.form['city']
    state = request.form['state']
    email = request.form['emailid']
    phone = request.form['phonenumber']
    adhar_no = request.form['aadharnumber']
    pancard_no = request.form['pancardnumber']
    qry = "UPDATE `user` SET `Dob`='"+dob+"',`Blood_group`='"+blood_group+"',`Nationality`='"+nationality+"',`Place_of_birth`='"+place_of_birth+"',`First_name`='"+first_name+"',`Last_name`='"+last_name+"',`Mother's_name`='"+mothers_name+"',`Father's_name`='"+fathers_name+"',`Gender`='"+gender+"',`Place`='"+place+"',`Pin`='"+pin+"',`Post`='"+post+"',`City`='"+city+"',`State`='"+state+"',`Mail_id`='"+email+"',`Phone`='"+phone+"',`Adhar_no`='"+adhar_no+"',`Pancard_no`='"+pancard_no+"' WHERE `User_lid`='"+user_lid+"'"
    res = db.update(qry)
    return jsonify(status="ok")




# @app.route('/and_view_documents', methods=['POST'])
# def and_view_documents():
#     user_lid = request.form['user_lid']
#     db = Db()
#     qry = "SELECT * FROM `document` JOIN `authority` ON `authority`.`Authority_lid` = `document`.`Authority_lid` JOIN `user` ON `document`.`User_lid` =  `user`.`User_lid` WHERE `User_lid` = '"+user_lid+"'"
#     res = db.select(qry)
#     return jsonify(status="ok")
#
#
# #
#
#
# @app.route('/manage_access_rights', methods=['POST'])
# def manage_access_rights():
#     return jsonify(status="ok")
#
# @app.route('/and_view_history', methods=['POST'])
# def and_view_history():
#     user_lid = request.form
#     db = Db()
#     qry = "SELECT * FROM `history` JOIN `document` ON `document`.`Doc_id` = `history`.`Doc_id` JOIN `user` ON `user`.`User_lid` = `history`.`Viewer_id` WHERE `User_lid` = '"+user_lid+"'"
#     res = db.select(qry)
#     return jsonify(status="ok")
#
# @app.route('/and_user_report', methods=['POST'])
# def and_user_report():
#     doc_id = request.form['doc_id']
#     user_lid = request.form['user_lid']
#     report = request.form['report']
#     db = Db()
#     qry = "INSERT INTO `report` (`User_lid`,`Authority_lid`,`Document_lid`,`Date`,`Status`,`Report`) VALUES ('"+user_lid+"','"++"','"+doc_id+"',curdate(),'pending','"+report+"')"
#     res = db.insert(qry)
#     return jsonify(status="ok")
#
# @app.route('/and_feedback', methods=['POST'])
# def and_feedback():
#     feedback = request.form['feedback']
#     user_lid = request.form['user_lid']
#     db = Db()
#     qry = "INSERT INTO `feedback` (`User_lid`,`Date`,`Feedback`) VALUE ('"+user_lid+"',curdate(),'"+feedback+"')"
#     res = db.select(qry)
#     return jsonify(status="ok")
#
# @app.route('/and_send_complaint', methods=['POST'])
# def and_send_complaint():
#     complaint =request.form['complaint']
#     user_lid = request.form['user_lid']
#     db = Db()
#     qry = "INSERT INTO `complaint` (`User_lid`,`Date`,`Complaint`,`Status`) VALUES ('"+user_lid+"',curdate(),'"+complaint+"','pending')"
#     res = db.insert(qry)
#     return jsonify(status="ok")
#
#
# @app.route('/and_view_reply', methods=['POST'])
# def and_view_reply():
#     user_lid = request.form['user_lid']
#     db = Db()
#     qry = "SELECT * FROM `complaint` WHERE `User_lid` = '"+user_lid+"'"
#     res = db.select(qry)
#     return jsonify(status="ok")
#
#
# @app.route('/and_scan_qr', methods=['POST'])
# def and_scan_qr():
#     return jsonify(status="ok")
#









@app.route('/and_view_documents', methods=['POST'])
def and_view_documents():
    lid=request.form['lid']
    db=Db()
    qry="SELECT *,`document`.Description as dd FROM `document` JOIN `authority`ON `document`.`Authority_lid`=`authority`.`Authority_lid` JOIN `user` ON `document`.`User_lid`=`user`.`User_lid` WHERE `user`.`User_lid`='"+lid+"'"
    res=db.select(qry)
    return jsonify(status="ok",data=res)



@app.route('/and_manage_access_rights', methods=['POST'])
def and_manage_access_rights():
    db=Db()
    document=request.form['document']
    lid=request.form['lid']
    qry="INSERT INTO `acces rights`(`User_lid`,`Doc_lid`) VALUES('"+lid+"','"+document+"')"
    res=db.insert(qry)
    return jsonify(status="ok")


@app.route('/and_view_access_rights', methods=['POST'])
def and_view_access_rights():
    lid=request.form['lid']
    uid=request.form['uid']
    db=Db()
    qry="SELECT *,`document`.Description as dd FROM `acces rights` JOIN `document` ON `document`.`Doc_id`=`acces rights`.`Doc_lid`  JOIN `authority` ON `document`.`Authority_lid`=`authority`.`Authority_lid` JOIN `user` ON `user`.`User_lid`=`acces rights`.`User_lid` WHERE `acces rights`.`User_lid`='"+lid+"' AND `document`.`User_lid`='"+uid+"'"
    res=db.select(qry)
    return jsonify(status="ok",data=res)



@app.route('/and_view_history', methods=['POST'])
def and_view_history():
    lid=request.form['lid']
    db=Db()
    qry="SELECT * FROM `acces rights` JOIN `document` ON `document`.`Doc_id`=`acces rights`.`Doc_lid` JOIN `user` ON `user`.`User_lid`=`acces rights`.`User_lid` WHERE `document`.`User_lid`='"+lid+"'"
    res=db.select(qry)
    return jsonify(status="ok",data=res)


@app.route('/and_remove_access', methods=['POST'])
def and_remove_access():
    acid = request.form['acid']
    qry="DELETE FROM `acces rights` WHERE `Ar_id`='"+acid+"'"
    db=Db()
    db.update(qry)
    return jsonify(status="ok")



@app.route('/and_report_issue', methods=['POST'])
def and_report_issue():
    db=Db()
    authority=request.form['authority']
    document=request.form['document']
    lid=request.form['lid']
    report=request.form['report']
    qry="INSERT INTO `report`(`User_lid`,`Authority_lid`,`Document_lid`,`Date`,`Report`,`status`)VALUES('"+lid+"','"+authority+"','"+document+"',CURDATE(),'"+report+"','pending')"
    res=db.insert(qry)
    return jsonify(status="ok")

@app.route('/and_send_feedback', methods=['POST'])
def and_send_feedback():
    db=Db()
    feedback=request.form['feedback']
    lid=request.form['lid']
    qry = "SELECT * FROM `feedback` WHERE `User_lid`='" + lid + "'"
    res = db.selectOne(qry)
    if res is None:

        qry="INSERT INTO feedback (`User_lid`,`Date`,`Feedback`)VALUES('"+lid+"',CURDATE(),'"+feedback+"')"
        res=db.insert(qry)
    else:
        qry="UPDATE `feedback` SET `Feedback`='"+feedback+"',`Date`=CURDATE() WHERE `User_lid` ='"+lid+"'"
        res=db.update(qry)
    return jsonify(status="ok")


@app.route('/and_send_complaint', methods=['POST'])
def and_send_complaint():
    db=Db()
    complaint=request.form['complaint']
    lid=request.form['lid']
    qry="INSERT INTO `complaint` (`User_lid`,`Date`,`Complaint`,`Status`,Reply) VALUES ('"+lid+"',curdate(),'"+complaint+"','pending','pending')"
    res=db.insert(qry)
    return jsonify(status="ok")


@app.route('/and_view_reply', methods=['POST'])
def and_view_reply():
    lid=request.form['lid']
    db=Db()
    qry="SELECT * FROM `complaint` WHERE `User_lid`='"+lid+"'"
    res=db.select(qry)
    return jsonify(status="ok",data=res)


@app.route('/and_view_feedback', methods=['POST'])
def and_view_feedback():
    lid=request.form['lid']
    db=Db()
    qry="SELECT * FROM `feedback` WHERE `User_lid`='"+lid+"'"
    res=db.select(qry)
    return jsonify(status="ok",data=res)

@app.route('/and_view_users', methods=['POST'])
def and_view_users():
    lid=request.form['lid']
    qry="SELECT * FROM `user` WHERE `User_lid` NOT IN (SELECT User_lid FROM `acces rights`) AND `User_lid`!='"+lid+"'  "
    db=Db()
    res=db.select(qry)
    return jsonify(status="ok",data=res)




@app.route('/and_view_users_search', methods=['POST'])
def and_view_users_search():
    lid=request.form['lid']
    search=request.form['search']
    print(search)
    qry="SELECT * FROM `user` WHERE `User_lid` NOT IN (SELECT User_lid FROM `acces rights`) and `user`.`Phone` LIKE '%"+str(search)+"%' AND `User_lid`!='"+lid+"'"
    db=Db()
    res=db.select(qry)
    return jsonify(status="ok",data=res)




@app.route('/and_giveaccess', methods=['POST'])
def and_giveaccess():
    did = request.form['did']
    selected = request.form['selected']
    choices = selected
    s= choices.split(",")
    for i in s:
        if str(i)!="":
            qry="INSERT INTO `acces rights` (`User_lid`,`Doc_lid`) VALUES('"+str(i)+"','"+did+"')"
            db=Db()
            db.insert(qry)
    return jsonify(status="ok")






@app.route('/authority_signup')
def authority_signup():
    return render_template('authority/SIGNUP.html')


@app.route('/authority_signup_post', methods = ['post'])
def authority_signup_post():
    name = request.form['textfield']
    phone = request.form['textfield2']
    city = request.form['textfield3']
    place = request.form['textfield4']
    post = request.form['textfield7']
    pin = request.form['textfield8']
    district = request.form['textfield5']
    state = request.form['textfield6']
    longitude = request.form['textfield9']
    latitude = request.form['textfield10']
    category = request.form['textfield11']
    description = request.form['textfield12']
    logo = request.files['textfield13']
    email = request.form['textfield14']
    Password = request.form['Password']
    db = Db()
    import datetime

    dd=datetime.datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
    logo.save("F:\\doc_backup\\web\\DOC_TAG\\static\\Logo\\"+dd)
    path="/static/Logo/"+dd

    import random
    pwd=Password
    qry2 = "INSERT INTO login(Username,PASSWORD,Login_type) VALUES('"+email+"','"+pwd+"','authority')"
    lid=str(db.insert(qry2))
    qry = "INSERT INTO authority(Authority_name,Place,Post,Pin,District,State,Latitude,Longitude,Authority_lid,Category,City,Phone,Email,Description,Logo) VALUES ('"+name+"','"+place+"','"+post+"','"+pin+"','"+district+"','"+state+"','"+latitude+"','"+longitude+"','"+lid+"','"+category+"','"+city+"','"+phone+"','"+email+"','"+description+"','"+path+"')"
    print(qry)
    res = db.insert(qry)
    return '''<script>alert('Signed Up');window.location='/'</script>'''










if __name__ == '__main__':
    app.run(debug=True, port=5000,host="0.0.0.0")

