from flask import Flask, render_template, request, redirect
import os
import datetime
import csv
import webbrowser
fname = "error"
lname = "error"
varss=True
timeleft = datetime.datetime.now()
def openTab(x):
  if x ==True: #open a new tab
    webbrowser.open('http://127.0.0.1:5000/')
    print("tab open")

openTab(varss)
varss=False
app = Flask(__name__)
@app.route('/credits')
def default():
 return "hello World" #test page
@app.route('/back')
def back():
 global fname #imports the vars into the function
 global lname
 
 now = datetime.datetime.now().strftime("%H:%M:%S") #gets the time to allow the page to display the time left
 return render_template('back.html', variable=now, fnamew=fname, lnamew=lname) #sends the data to page
@app.route('/')
def home():
 global fname
 global lname
 global timeleft 
 
 date_today = datetime.datetime.now().strftime("%Y-%m-%d") 
 date = datetime.datetime.now().strftime("%H:%M:%S")
 now = datetime.datetime.now()
 timereturn = now-timeleft
 path = os.getcwd() #gets path to folder
 f = path+'//signoutsheets//'+date_today+'signoutlog'+'.csv'
 open(f, mode='a+')
 if fname != "error" or lname != "error":
  with open(f, mode='a+') as signout: #writes the lines to the spreadsheet
   signout_writer = csv.writer(signout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

   signout_writer.writerow([fname.upper(), lname.upper(), date,str("returned"), str("total time out: ") + str(timereturn)])

 return render_template('home.html' )
 
@app.route('/', methods=['POST'])#gets the data from the page
def my_form_post():
 global fname
 global lname 
 global timeleft
 fname = request.form['fname']
 lname = request.form['lname']
 lname_up = lname.upper()
 fname_up = fname.upper()
 date_today = datetime.datetime.now().strftime("%Y-%m-%d")
 date = datetime.datetime.now().strftime("%H:%M:%S")
 path = os.getcwd()
 f = path+'//signoutsheets//'+date_today+'signoutlog'+'.csv'
 timeleft = datetime.datetime.now()
 if fname != 'error' or lname != 'error':
  with open(f, mode='a+') as signout:
   signout_writer = csv.writer(signout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
   signout_writer.writerow([fname_up,lname_up,date,str("left")])

 return redirect('http://127.0.0.1:5000/back') #sends to next screen
 
 
if __name__ == '__main__':
 ip = '127.0.0.1'
 port = int(os.environ.get('PORT', 5000))
 app.run(host=ip, port=port, debug=False)
