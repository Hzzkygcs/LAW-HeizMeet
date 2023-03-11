from schedule.core.Repository.DateRangeRepository import DateRangeRepository
from schedule.core.Repository.ScheduleRepository import ScheduleRepository
from schedule.models import Schedule


class ScheduleFactory:
    def __init__(self, dateRangeRepository: DateRangeRepository, scheduleRepository: ScheduleRepository):
        self.dateRangeRepository = dateRangeRepository
        self.scheduleRepository = scheduleRepository

    def create_schedule(self, event_id, start, end):
        date_range = self.dateRangeRepository.create()
        date_range.start_date_time = start
        date_range.end_date_time = end
        self.dateRangeRepository.save(date_range)

        date_range_id = date_range.ID
        schedule = Schedule.objects.create(datetime_range_id=date_range_id, event_id=event_id)
        return schedule
