from . import db

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    subname = db.Column(db.Text)                     # for the "Made for", maybe other things

    # Playlist relationship
    playlists = db.relationship('Playlist', backref='topic', lazy=True, cascade='all, delete-orphan')

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True)                        # playlist name
    description = db.Column(db.Text)
    playlist_type = db.Column(db.Text)               # Public Playlist, Album, etc.
    cover = db.Column(db.Text)
    creator = db.Column(db.Text)                     # made for --- recruiters, matthew muranaka
    creator_picture = db.Column(db.Text)                    # usually spotify logo (or my profile picture)
    col1 = db.Column(db.Text)                         # usually title
    col2 = db.Column(db.Text)                         # usually album
    col3 = db.Column(db.Text)                         # usually duration (will be description of the time icon)
    madeFor = db.Column(db.Boolean, default=False)
    other = db.Column(db.Text)                    # usually 50 songs, 2hr 53 min

    # Topic Foreign Key
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)

    # Songs relationship
    songs = db.relationship('Song', backref='playlist', lazy=True, cascade='all, delete-orphan')

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    artist = db.Column(db.Text)
    album = db.Column(db.Text)
    start_duration = db.Column(db.Date)
    end_duration = db.Column(db.Date)
    cover = db.Column(db.Text)
    explicit = db.Column(db.Boolean, default=False)          # explicit tag
    link = db.Column(db.Text)                               # used to link projects, etc.

    # Playlist foreign key
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'), nullable=False)


# format: https://<your-project-id>.supabase.co/storage/v1/object/public/<bucket-name>/<path>

# https://swpzmceclluxivxkgtex.supabase.co/storage/v1/object/public/playlist/technology.jpg