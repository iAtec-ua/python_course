# Constructor for Apartment class

# Import mongoengine to manage Mongo Database
import mongoengine
# Import reservations to link them to apartments
from Practice_13.models.reservations import Reservation


# Create class with structure of the MongoDB built-in document
# There are three fields: Name, Price, Description and Smoking allowance
class Apartment(mongoengine.Document):
    # Create first field of string type which is required and unique
    name = mongoengine.StringField(required=True, unique=True)
    # Create second field of float type which is required and has a minimal limit of 15
    price = mongoengine.FloatField(required=True, min_value=15)
    # Create third field of string type with no parameters
    description = mongoengine.StringField(max_length=100)
    # Create fourth field of boolean type which by default is False
    smoke_allowed = mongoengine.BooleanField(default=False)

    # Create linked field to show if apartment is reserved 
    reservations = mongoengine.EmbeddedDocumentListField(Reservation)

    # Create object with names of database and document
    meta = {
        'db_alias': 'hotel',
        'collection': 'apartments'
    }
