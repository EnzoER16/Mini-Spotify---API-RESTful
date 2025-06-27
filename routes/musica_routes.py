from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from models.musica import Musica
from models.db import db

cancion = Blueprint('musica', __name__, url_prefix='/spotify')