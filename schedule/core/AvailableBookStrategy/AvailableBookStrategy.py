from schedule.models import DateRange


class AvailableBookStrategy:
    def get_available_slots(self) -> list[DateRange]:
        raise NotImplementedError()
