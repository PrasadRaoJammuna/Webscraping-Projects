from flask import Flask,render_template,request,redirect
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    meaning=''
    no_mean=''
    word=''
    message=''
    try:
        if request.method == 'POST':
            word = request.form['word']
            if word =='':
                message = 'Enter a word'

            url = 'https://www.vocabulary.com/dictionary/'
            url = url+word
            link = requests.get(url).text
            soup = BeautifulSoup(link,'html')
            data = soup.find_all('p',class_='short')
            if data == []:
               no_mean= 'Sorry! word not found in this Dictionary'
            else:
             
                for mean in data:
                    meaning = mean.text
                print(meaning)
    except Exception as e:
            #print('Sorry!you are not connected to the interent')
            print(str(e))
            exit(-1)


    return render_template('index.html',meaning=meaning,no_mean=no_mean,word=word,message=message)
    






if __name__ == "__main__":
    app.run(debug=True)
