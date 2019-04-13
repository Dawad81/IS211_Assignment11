#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring"""


from flask import Flask, render_template, request, redirect
import os
import pickle
import re

app = Flask(__name__)


@app.route('/')
def to_do():
    return render_template('index.html', to_do_list=to_do_list)


email_check = re.compile("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")


@app.route('/submit', methods=['POST'])
def submit():
    if request.form['task'] == '':
        return redirect('/')
    elif not re.match(email_check, request.form['email']):
        return redirect('/')
    elif request.form['priority'] not in ('Low', 'Medium', 'High'):
        return redirect('/')
    else:
        to_do_list.append({'ToDoItem': request.form['task'].title(),
                           'Email': request.form['email'],
                           'Priority': request.form['priority']})
        return redirect('/')


@app.route('/clear', methods=['POST'])
def clear():
    to_do_list[:] = []
    return redirect('/')


@app.route('/save', methods=['POST'])
def save():
    to_pickle_file = open('to_do_list.pkl', 'wb')
    pickle.dump(to_do_list, to_pickle_file)
    to_pickle_file.close()
    return redirect('/')


def get_to_do_list():
    from_pickle_file = 'to_do_list.pkl'
    if os.path.exists(from_pickle_file):
        to_do_list = pickle.load(open(from_pickle_file, 'rb'))
        return to_do_list
    else:
        to_do_list = []
        return to_do_list


if __name__ == '__main__':
    to_do_list = get_to_do_list()
    app.run(debug=1)
