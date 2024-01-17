from flask import Flask, render_template, flash, redirect, Blueprint
from forms import PetForm
from models import db, Pet

routes_bp = Blueprint('routes', __name__)

@routes_bp.route("/")
def homepage():

    pets = Pet.query.all()
    return render_template('homepage.html', pets = pets)

@routes_bp.route("/add", methods = ["GET", "POST"])
def add_pet_form():

    form = PetForm()

    if form.validate_on_submit():

        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        new_pet = Pet(name = name, species = species, photo_url = photo_url, age = age, notes = notes, available = available)

        db.session.add(new_pet)
        db.session.commit()

        flash(f"added {name} to Pets")
        return redirect("/add")
    else:
        return render_template("Add_Pet_Form.html", form = form)

@routes_bp.route("/<pet_id>")
def show_pet_details(pet_id):

    pet = Pet.query.get_or_404(pet_id)

    return render_template("Pet_Details.html", pet = pet)

@routes_bp.route("/<pet_id>/edit", methods=["GET", "POST"])
def edit_pet(pet_id):

    pet = Pet.query.get_or_404(pet_id)

    form = PetForm(obj=pet)

    if form.validate_on_submit():
        
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.add(pet)
        db.session.commit()
        
        return redirect("/")
    else:
        return render_template("Edit_Pet_Form.html", form = form, pet_name=pet.name, pet_species=pet.species)

@routes_bp.route("/<pet_id>/delete", methods = ["POST"])
def delete_pet(pet_id):

    pet = Pet.query.get_or_404(pet_id)

    db.session.delete(pet)
    db.session.commit()

    return redirect("/")
