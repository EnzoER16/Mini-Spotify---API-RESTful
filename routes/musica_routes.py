from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from models.musica import Musica
from models.db import db

cancion = Blueprint('musica', __name__, url_prefix='/spotify')

@cancion.route('/canciones')
def get_canciones_activas():
    canciones = Musica.query.filter_by(activo=True).all()
    return jsonify([cancion.serialize() for cancion in canciones])