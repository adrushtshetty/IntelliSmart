from flask import Flask, request, jsonify, render_template, url_for,redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/EnggMechanics')
def mechTXT():
    return render_template("mechTXT.html")

@app.route('/EnggMechanics', methods=['POST'])
def mechQS():
    n=request.form['prob']
    if n=="2":
        return redirect(url_for('EnggMechanicsP2_23'))
    elif n=="3":
        return redirect(url_for('MechChapter3'))
    elif n=="A":
        return redirect(url_for('MechChapterA'))
    elif n=="6":
        return redirect(url_for('MechChapter6'))
    else:
        return redirect(url_for('notDone'))


@app.route('/EnggMechanicsP3')
def MechChapter3():
    return render_template("Prob3.html")

@app.route('/EnggMechanicsA')
def MechChapterA():
    return render_template("ChapterA.html")

@app.route('/EnggMechanics6')
def MechChapter6():
    return render_template("Chapter6.html")

@app.route('/EnggMechanics6', methods=['POST'])
def prpbSlc6():
    n=request.form['prob']
    if n=="3":
        return redirect(url_for('a_6'))
    else:
        return redirect(url_for('notDone'))

@app.route('/EnggMechanic6_3')
def a_6():
    return render_template("6-3.html")

@app.route('/EnggMechanicTXT6_3')
def txt6_3():
    return render_template("TxtBook6-3.html")

@app.route('/EnggMechanicsCust6-3')
def cs6_3():
    return render_template("Cust6-3.html")

@app.route('/EnggMechanicsCust6-3',methods=['POST'])
def inputcs6_3():
    import math
    m = float(request.form['mass'])
    P = float(request.form['P'])
    a=float(request.form['a'])
    t=float(request.form['t'])
    s=float(request.form['s'])
    k = float(request.form['k'])
    g=9.81
    cosa = math.cos(math.radians(a))
    sina = math.sin(math.radians(a))
    cost = math.cos(math.radians(t))
    sint = math.sin(math.radians(t))
    N=abs((m*g*cost)-(P*sina))
    Ff=N*s
    direc=""
    Ft=abs((m*g*sint)-(P*cosa))
    Pv = m * g * (((s * cost) + sint) / ((cosa) + (s * sina)))
    if Ft==0.0:
        check1="NoFriction"
    if Ff >=Ft:
        check1 = "Ff"
        if (m*g*sint) > (P*cosa):
            direc="UP"
            Ff1 = Ft
        elif (m*g*sint) < (P*cosa):
            direc="DOWN"
            Ff1=Ft
        else:
            check1="NoFriction"
        return render_template("CS6-3.html", St='{}'.format(t), Sa='{}'.format(a), Ss='{}'.format(s), Sk='{}'.format(k),
                               SP='{}'.format(P), SN='{}'.format(N), SFt='{}'.format(Ft), SFf='{}'.format(Ff),
                               SFf1='{}'.format(Ff1), Sdirec='{}'.format(direc), SPp='{}'.format(Pv),
                               check='{}'.format(check1))


    else:
        check1="Ft"
        if (m*g*sint) > (P*cosa):
            direc="UP"
            Ff1 = N * k
        else:
            direc="DOWN"
            Ff1 = N * k
        return render_template("CS6-3.html", St='{}'.format(t), Sa='{}'.format(a), Ss='{}'.format(s), Sk='{}'.format(k),
                               SP='{}'.format(P), SN='{}'.format(N), SFt='{}'.format(Ft), SFf='{}'.format(Ff),
                               SFf1='{}'.format(Ff1), Sdirec='{}'.format(direc), SPp='{}'.format(Pv),
                               check='{}'.format(check1))






    # if A==0.0:
    #     chk="zeroError"
    #     return render_template("CustA-3.html",error='{}'.format(chk))
    # else:
    #     Ix=(A*(kx**2))
    #     Iz=Ix+(Iy*1000)
    #     kz=(Iz/A)**0.5
    #     return render_template("CSA-3.html",SIy='{}'.format(Iy),SIx='{}'.format(Ix),SA='{}'.format(A),Skx='{}'.format(kx),SIz='{}'.format(Iz),Skz='{}'.format(kz))


@app.route('/EnggMechanicsA', methods=['POST'])
def prpbSlcA():
    n=request.form['prob']
    if n=="3":
        return redirect(url_for('a_3'))
    else:
        return redirect(url_for('notDone'))

@app.route('/EnggMechanicA_3')
def a_3():
    return render_template("A-3.html")


@app.route('/EnggMechanicsP3', methods=['POST'])
def prpbSlc3():
    n=request.form['prob']
    if n=="3":
        return redirect(url_for('p3_3'))
    else:
        return redirect(url_for('notDone'))

@app.route('/EnggMechanicP3_33')
def p3_3():
    return render_template("blog1.html")

@app.route('/EnggMechanicsCust3-3')
def cs3_3():
    return render_template("Cust3-3.html")

@app.route('/EnggMechanicsCustA-3')
def csa_3():
    return render_template("CustA-3.html")

@app.route('/EnggChemistry')
def chem():
    return render_template("PC404.html")

@app.route('/EnggMathematics')
def math():
    return render_template("PM404.html")

@app.route('/Electronics&PrincipleDevices')
def epd():
    return render_template("P404.html")

@app.route('/EnggMechanicsCustA-3',methods=['POST'])
def inputcsA_3():
    A = float(request.form['area'])
    Iy = float(request.form['Iy'])
    kx=float(request.form['kx'])
    if A==0.0:
        chk="zeroError"
        return render_template("CustA-3.html",error='{}'.format(chk))
    else:
        Ix=(A*(kx**2))
        Iz=Ix+(Iy*1000)
        kz=(Iz/A)**0.5
        return render_template("CSA-3.html",SIy='{}'.format(Iy),SIx='{}'.format(Ix),SA='{}'.format(A),Skx='{}'.format(kx),SIz='{}'.format(Iz),Skz='{}'.format(kz))


@app.route('/EnggMechanicsCust3-3',methods=['POST'])
def inputcs3_3():
    x = float(request.form['x'])
    y = float(request.form['y'])
    z = float(request.form['z'])
    m = float(request.form['m'])
    # f1=open("log.txt",'w')
    # f1.write(str([x,y,z,m]))
    # f1.close()
    Na=((m*9.81)*(x-((x+y+z)/2)+y))/y
    return render_template("CS3-3.html",rt_x='{}'.format(x),rt_y='{}'.format(y),rt_z='{}'.format(z),rt_m='{}'.format(m),rt_Na='{}'.format(Na))

@app.route('/EnggMechanicTXT3_3')
def txt3_3():
    return render_template("TxtBook3-3.html")

@app.route('/EnggMechanicTXTA_3')
def txtA_3():
    return render_template("TxtBookA-3.html")

@app.route('/EnggMechanicsP')
def EnggMechanicsP2_23():
    return render_template("Prob2.html")

@app.route('/EnggMechanicsP', methods=['POST'])
def prpbSlc():
    n=request.form['prob']
    if n=="23":
        return redirect(url_for('p2_23'))
    else:
        return redirect(url_for('notDone'))

@app.route("/EnggMechanicsP2-23")
def p2_23():
    return render_template("blog.html")

@app.route("/StillWorking")
def notDone():
    return render_template("P404.html")

@app.route('/EnggMechanics2-23')
def EnggMechP2_23():
    return render_template("Cust2-23.html")

@app.route('/EnggMechanicsT2-23')
def EnggMechPT2_23():
    return render_template("TxtBook2-23.html")

@app.route('/EnggMechanics2-23', methods=['POST'])
def EnggMechPCS2_23():
    import numpy as np
    import math
    a = int(request.form['alpha'])
    b = int(request.form['beta'])
    r = int(request.form['r'])
    f1=open("log.txt",'w')
    str1=str([a,b,r])
    f1.write(str1)
    f1.close()
    sina=(np.sin(math.radians(a)))
    sinb = (np.sin(math.radians(b)))
    sinx = (np.sin(math.radians(180-(a+b))))
    fa=r*sinb/sinx
    fb=r*sina/sinx
    pa=r*np.cos(math.radians(a))
    return render_template("CS2-23.html",rt_fa='{}'.format(fa),rt_fb='{}'.format(fb),rt_a='{}'.format(a),rt_b='{}'.format(b),rt_r='{}'.format(r),rt_x='{}'.format(180-(a+b)),rt_pa='{}'.format(pa))


@app.route('/', methods=['POST'])
def mail():
    from email.message import EmailMessage
    import ssl
    import smtplib

    name = request.form['name']
    subject = request.form['subject']
    message = request.form['message']
    mail = request.form['email']

    email_sender = "drdev.maill@gmail.com"
    email_password = "mmieeonadmnrylqz"
    email_receiver = ["adrushtshetty@gmail.com"]
    body = """
        Dear IntelliSmart Development Team,

        I hope this message finds you well. My name is {pName}, and I recently used the "Contact Us" form on your website. I wanted to follow up on my inquiry.

        Contact Information:

        Name: {pName}
        Email Address: {pMail}
        Inquiry:
        {pmessage}

        I appreciate your prompt attention to this matter and look forward to your response. Thank you for providing such a valuable platform for learning.

        Sincerely,

        {pName}

        """.format(pName=name, pMail=mail, pmessage=message)
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)