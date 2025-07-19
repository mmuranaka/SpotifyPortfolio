import os
from dotenv import load_dotenv
from flask import Blueprint, render_template, send_from_directory, current_app
from .models import Topic, Playlist, Song
from . import db

views = Blueprint('views', __name__)

load_dotenv()
img_src=os.getenv("SUPABASE_BUCKET_LINK")

@views.route('/')
def intro():
    return render_template('intro.html')

@views.route('/home')
def home():
    topics = Topic.query.all()
    playlists = Playlist.query.all()
    return render_template('home.html', img_src=img_src, topics=topics, playlists=playlists)

@views.route('/<playlist_name>')
def playlist(playlist_name):
    playlist = Playlist.query.filter(Playlist.name.ilike(playlist_name)).first()
    songs = Song.query.filter_by(playlist_id=playlist.id).order_by(Song.start_duration.desc())
    return render_template('playlist.html', img_src=img_src, playlist=playlist, songs=songs)

@views.route('/profile')
def profile():
    socials = Song.query.filter_by(playlist_id=6)
    return render_template('profile.html', img_src=img_src, socials=socials)

@views.route('/resume')
def resume():
    return send_from_directory(
        directory=os.path.join(current_app.root_path, 'static'),
        path='resume.pdf',
        as_attachment=False,
        download_name='matthew-muranaka-resume.pdf'
    )