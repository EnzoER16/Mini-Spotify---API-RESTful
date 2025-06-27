from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from models.musica import Musica
from models.db import db

cancion = Blueprint('musica', __name__, url_prefix='/api/spotify')

@cancion.route('/canciones')
def get_canciones_activas():
    canciones = Musica.query.filter_by(activo=True).all() # Filtra las canciones que estan activas
    return jsonify([cancion.serialize() for cancion in canciones])

@cancion.route('/canciones/<int:id>', methods=['DELETE'])
def modify_canciones(id):
    cancion = Musica.query.get(id)
    
    if not cancion: 
        return jsonify({'message':'Cancion no encontrada'}), 404 

    cancion.activo = False
    db.session.commit()

    return jsonify({'message': f'Canción con id {id} dada de baja'}), 200

