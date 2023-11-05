from flask import Flask, request, jsonify, render_template, url_for,redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/EnggMechanics')
def mechTXT():
    return redirect(url_for('MechChapter3'))

@app.route('/EnggMechanics', methods=['POST'])
def mechQS():
    n=request.form['prob']
    if n=="2":
        return redirect(url_for('EnggMechanicsP2_23'))
    elif n=="3":
        return redirect(url_for('MechChapter3'))
    else:
        return redirect(url_for('home'))


@app.route('/EnggMechanicsP3')
def MechChapter3():
    return render_template("Prob3.html")

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

@app.route('/EnggChemistry')
def chem():
    return render_template("PC404.html")

@app.route('/EnggMathematics')
def math():
    return render_template("PM404.html")

@app.route('/Electronics&PrincipleDevices')
def epd():
    return render_template("P404.html")



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