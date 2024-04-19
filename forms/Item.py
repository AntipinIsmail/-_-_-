from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileField



class AddItem(FlaskForm):

    item_name = StringField('Имя предмета', validators=[DataRequired()])
    price = StringField("Цена", validators=[DataRequired()])
    type = StringField("Тип", validators=[DataRequired()])
    about = StringField("Расскажите о предмете")
    photo = FileField('Картинка', validators=[DataRequired()])
    info = None
    submit = SubmitField('Create Item')
