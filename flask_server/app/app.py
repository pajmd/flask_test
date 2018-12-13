from flask import Flask, render_template, request
from werkzeug.utils import secure_filename


# https://www.youtube.com/watch?v=uqr-e-dkkNI
# https://www.youtube.com/watch?v=AOboS0RESt4

app = Flask(__name__)

planes = [
     {
         'name': 'marie',
         'plane':'boeing',
         'when': '10am'
     },
    {
        'name': 'pierre',
        'plane': 'piper',
        'when': '10am'
    },
    {
        'name': 'jean',
        'plane': 'boeing',
        'when': '14am'
    },
]

@app.route('/')
@app.route('/<user>')
def index(user=None):
    return render_template("user.html", user=user)


@app.route("/profile/<name>")
def profile(name):
    return render_template("profile.html", name=name)


@app.route("/shopping")
def shopping():
    food = ['croissant', 'pain aux rasins', 'flans']
    return render_template("shopping.html", food=food)


@app.route("/register")
def register():
    return render_template('registration.html')


@app.route("/single_page_register", methods=['GET', 'POST'])
def single_page_register():
    if request.method == 'POST':
        name = request.form.get('name')
        new_plane = request.form.get('plane')
        when = request.form.get('when')
        if new_plane and new_plane and when:
            planes.append(
                {
                    'name': name,
                    'plane': new_plane,
                    'when': when
                }
            )
    return render_template('single_page_registration.html', planes=planes)


@app.route("/registration2", methods=['POST'])
def reply():
    plane = request.form.get('plane')
    if plane:
        return render_template('registration2.html', plane=plane)
    else:
        return render_template('registration2.html', error="YOU NEED TO SPECIFY A PLANE")

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['picture']
    f.save(secure_filename())

# an alternative way to $ flask run --host=192.168.1.4 is app.run()
# but it is not recommended
if __name__ == "__main__":
    app.debug = True
    app.run(host="192.168.1.4",)