from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)
books=[]
@app.route('/')
def index():
    return render_template('index.html',books=books)
@app.route('/addbook',methods=['GET','post'])
def addbook():
    if request.method=='POST':
        title=request.form['title']
        author=request.form['author']
        books.append({'title':title,'author':author})
        return redirect(url_for('index'))
    return render_template('addbook.html')
if __name__=='__main__':
    app.run(debug=True)

