from flask import Flask, render_template, request, redirect

app = Flask(__name__)


notes = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)
    notes1=list(enumerate(notes))
    
    return render_template("home.html", notes=notes1)

@app.route('/delete/<int:index>', methods=['POST'])
def delete(index):
    if 0 <= index < len(notes):
        del notes[index]
    return redirect('/')

@app.route('/deleteall',methods=['POST'])
def dltall():
    notes.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)



