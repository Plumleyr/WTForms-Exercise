from wtforms import ValidationError

def ValidateSpecies(form,field):
    if field.data.lower() not in ['cat','dog','porcupine']:
        raise ValidationError("Invalid Species")
