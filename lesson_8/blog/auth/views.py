from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import logout_user, login_user, login_required, current_user

from blog.forms.auth import AuthForm
from blog.models import User

auth = Blueprint('auth', __name__, static_folder='../static')


@auth.route('/login', methods=('GET',))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user.profile', pk=current_user.id))

    return render_template('auth/login.html', form=AuthForm(request.form))


@auth.route('/login', methods=('POST',))
def login_post():
    form = AuthForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if not user or not user.check_password(form.password.data):
            flash('Check your login details')
            return redirect(url_for('.login'))

        login_user(user)
        return redirect(url_for('user.profile', pk=user.id))

    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))
