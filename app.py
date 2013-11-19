# coding: utf-8

from flask import Flask, render_template, session, redirect, request, flash
app = Flask(__name__)
app.secret_key = 'RXj4Ojtv2OI4'

@app.route('/')
def index():
    if 'step' not in session:
        return render_template('index.html')
    else:
        return redirect('step/{}'.format(session['step']))

@app.route('/step/<int:step_id>', methods=['POST', 'GET'])
def step(step_id):
    if step_id == 1:
        session['step'] = 1
    if step_id == 2:
        if request.method == 'POST':
            if request.form['code'] != '2128506':
                flash('Oh...')
                return redirect('step/1')
            else:
                session['step'] = 2
        else:
            try:
                if session['step'] != 2:
                    redirect('step/1')
                else:
                    redirect('/')
            except KeyError:
                redirect('/')

    return render_template('step_{}.html'.format(step_id))

@app.route('/fin', methods=['POST'])
def fin():
    if request.form['code'] != '1983':
        flash('Oh...')
        return redirect('step/2')
    del session['step']
    return render_template('fin.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
