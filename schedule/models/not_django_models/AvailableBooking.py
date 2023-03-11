class AvailableBooking:  # not for database
    def __init__(self, schedule_id, datetime_range):
        self.schedule_id = schedule_id
        self.datetime_range = datetime_range
