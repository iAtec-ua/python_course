# Constructor for Guest class

# Import mongoengine to manage Mongo Database
import mongoengine


# Create class with structure of the MongoDB built-in document
# There are three fields: Name, Age and credit card existence
class Guest(mongoengine.Document):
    # Create first field of string type which is required
    name = mongoengine.StringField(required=True)
    # Create second field of integer type which is required and has a minimal limit of 16
    age = mongoengine.IntField(required=True, min_value=16)
    # Create fourth field of boolean type which by default is True
    is_card = mongoengine.BooleanField(default=True)

    # Create object with names of database and document
    meta = {
        'db_alias': 'hotel',
        'collection': 'guests'
    }
