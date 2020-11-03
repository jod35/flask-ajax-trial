from flask import Flask,request,make_response,jsonify,render_template
from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+ app.root_path+ '/base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)


class Comment(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    body=db.Column(db.Text())

    def save(self):
        db.session.add(self)
        db.session.commit()

@app.route('/')
def hello():
    return make_response(jsonify({"message":"Hello"}))

@app.route('/ajax')
def ajax():
    return render_template('index.html')

@app.route('/comment')
def comment():
   
    return render_template('comment.html')

@app.route('/add_comment',methods=['POST'])
def add_comment(): 
    comment=request.form.get('comment')

    new_comment=Comment(body=comment)

    new_comment.save()

    return make_response(jsonify({"comment":comment}),201)
    


@app.shell_context_processor
def make_shell_context():
    return {
        'Comment':Comment,
        'db':db,
        'app':app
    }

if __name__ == "__main__":
    app.run(debug=True)