#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring"""


from flask import Flask, render_template, request, redirect
import re

app = Flask(__name__)

to_do_list = [{'ToDoItem': 'Get Milk', 'Email': 'Dennis.Awad@email.com', 'Priority': 'High'},
              {'ToDoItem': 'Get Pizza', 'Email': 'Nicole.Awad@email.com', 'Priority': 'Medium'},
              {'ToDoItem': 'Get Soap', 'Email': 'Awad@email.com', 'Priority': 'Low'}]


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


if __name__ == '__main__':
    app.run(debug=1)
