from flask_sqlalchemy import SQLAlchemy

# Create the Flask SQLAlchemy extension
db = SQLAlchemy()

# Define a model class by inheriting from db.Model
class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Pet {self.id}, {self.name}, {self.species}>'

    def to_dict(self):
        """Converts the Pet object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'species': self.species
        }
