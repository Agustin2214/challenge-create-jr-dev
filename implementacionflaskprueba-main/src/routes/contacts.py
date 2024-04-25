from flask import Blueprint, request, jsonify , abort
from models.contact import Contact , ContactSchema
from utils.db import db
contacts = Blueprint('contacts', __name__)

contact_schema = ContactSchema()
contact_schemas = ContactSchema(many=True)

@contacts.route('/new', methods=['POST'])
def post_contacts():
    fullname = request.json['fullname']
    email = request.json['email']
    phone = request.json['phone']


    contact = Contact(fullname, email, phone)
    db.session.add(contact)
    db.session.commit()

    return contact_schema.jsonify(contact)

@contacts.route('/', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    serialized_contacts = [{"fullname": contact.fullname, "phone": contact.phone, "email": contact.email} for contact in contacts]
    return jsonify(serialized_contacts)


@contacts.route("/update/<string:id>", methods=["PUT"])
def update(id):
    # get contact by Id
    print(id)
    contact = Contact.query.get(id)

    if contact:
        # Actualizar el contacto con los datos proporcionados en el cuerpo de la solicitud JSON
        data = request.get_json()
        contact.fullname = data.get('fullname', contact.fullname)
        contact.email = data.get('email', contact.email)
        contact.phone = data.get('phone', contact.phone)

        return jsonify({"message": "Contact updated successfully!"})
    else:
        return jsonify({"message": "Contact not found"}), 40


@contacts.route("/delete/<id>", methods=["DELETE"])
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)

    return jsonify({"message": "Contact deleted successfully!"})