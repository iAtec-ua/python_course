# Constructor for Reservation class

# Import mongoengine to manage Mongo Database
import mongoengine


# Create class with structure of the MongoDB built-in document
# There are four fields: Guest ID, Booking, Check-in and Check-out dates
class Reservation(mongoengine.EmbeddedDocument):
    # Create first field of object type with no parameters
    guest_id = mongoengine.ObjectIdField
    # Create second field of data time type with no parameters
    booked_date = mongoengine.DateTimeField(required=True)
    # Create third field of data time type which is required
    check_in_date = mongoengine.DateTimeField(required=True)
    # Create third field of data time type which is required
    check_out_date = mongoengine.DateTimeField(required=True)

    # Attribute and function automatically calculates duration of staying
    @property
    def duration(self):
        tmp = self.check_out_date - self.check_in_date
        # Returns duration only in days (no need for hours, minutes and seconds)
        return tmp.days
