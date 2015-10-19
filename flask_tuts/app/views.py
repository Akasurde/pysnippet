from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname' : 'Abhijeet'}
    posts = [ 
        { 'author' : { 'nickname' : 'Abhijeet'},
            'body' : ' Sample Text in body 1',
        },
        {
            'author' : {'nickname': 'Aayush'},
            'body' : 'Sample text in body 2',
        }
    ]
        
    return render_template('index.html', title='Home', user=user, posts=posts)
