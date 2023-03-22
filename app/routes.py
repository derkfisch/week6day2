from app import app
from flask import render_template
from app.forms import PhonebookForm


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/phonebook', methods = ["GET", "POST"])
def phonebook():
    form = PhonebookForm()
    if form.validate_on_submit():
        print('You have submmitted your phonebook')
        first_name = form.first_name.data
        last_name = form.last_name.data
        phone_number = form.phone_number.data
        address = form.address.data
        print(first_name, last_name, phone_number, address)
        flash(f"Thanks {first_name} for entering your phonebook info")
        return redirect(url_for('base'))
    return render_template('phonebook.html', form=form)