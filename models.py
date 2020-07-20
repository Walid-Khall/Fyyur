from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    show = db.relationship("Show")
    
    def __repr__(self):
        return f'<Venue {self.id} {self.name} {self.city} {self.state}>'


class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    show = db.relationship("Show")
    
    
    def __repr__(self):
        return f'<Venue {self.id} {self.name} {self.city} {self.state}>'

    # TODO: implement any missing fields, as a database migration using Flask-Migrate



    
    # TODO: implement any missing fields, as a database migration using Flask-Migrate



class Show(db.Model):
    __tablename__ = 'shows'
    
    id = db.Column(db.Integer, primary_key=True)
    venue_name = db.Column(db.String(120))
    artist_name = db.Column(db.String(120))
    artist_image_link = db.Column(db.String(500))
    start_time = db.Column(db.String(120))
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), nullable=False)