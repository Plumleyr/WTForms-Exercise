from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, ValidationError
from wtforms.validators import InputRequired, Optional, NumberRange, URL, AnyOf
from functions import ValidateSpecies

class PetForm(FlaskForm):

    name = StringField("Pets Name",
                        validators = [InputRequired()])

    species = StringField("Species of Pet",
                            validators = [InputRequired(), ValidateSpecies])

    photo_url = StringField("Photo of Pet",
                            validators = [Optional(), URL()])

    age = IntegerField("Age of Pet",
                        validators = [Optional(), NumberRange(min = 0, max = 30, message = "Age must be between 0 and 30 years old")])

    notes = StringField("Additional Info of Pet",
                        validators = [Optional()])

    available = BooleanField("Is This Pet Available for Adoption",
                            default = True)