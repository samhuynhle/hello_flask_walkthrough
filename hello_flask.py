from flask import Flask, render_template                 #Import Flask to allow us to create our app
app = Flask(__name__)                   #Create a new instance of the Flask class called "app"
@app.route('/')                         #The "@" decorator associates this route with the function immediately following
def hello_world():
    # return 'Hello World of Flask!'      #Return the string when the function is called as a response
    # return the result of the render_template method
    return render_template('index.html', phrase='hello', times=5)
@app.route('/success')
def success():
    return 'Great jobs!'
@app.route('/hello/<name>/<id>')
def hello(name, id):
    return render_template('hello.html', given_name=name, given_id=int(id))

if __name__ == '__main__':              #Ensure this file is benig run directly and not from a different module
    app.run(debug=True)                 #Run the app in debug mode
