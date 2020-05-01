# Import mongoengine to manage Mongo Database
import mongoengine


# Create function for initializing connection to MongoDB
def global_init():
    mongoengine.register_connection('hotel', name='hotel_one')
