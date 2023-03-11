import json

from schedule.models import DateRange


class AvailableBooking:  # not for database
    def __init__(self, schedule_id, datetime_range: DateRange):
        self.schedule_id = schedule_id
        self.datetime_range = datetime_range

    def to_dict(self):
        return {
            'schedule_id': self.schedule_id,
            'datetime_range': self.datetime_range.to_dict(),
        }

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

