from flask_wtf import Form
from wtforms import TextField,SubmitField,PasswordField,BooleanField
from wtforms.validators import DataRequired

class MyForm(Form):
    name   = TextField('name',validators=[DataRequired])
    submit = SubmitField('submit')

class LoginForm(Form):
    name = TextField('name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

    def validate_name(self, field):
        name = field.data.strip()
        if len(name) < 3 or len(name) > 20:
            raise ValidationError('name must be 3 letter at least')
        elif not re.search(r'^\w+$', name):
            raise ValidationError(
                'User names can contain only alphanumeric characters and underscores.')
        else:
            return name
