from datetime import datetime, date


class DataConversion:
    @staticmethod
    def convert_openmrs_date(data):
        if type(data) == str:
            return date.fromisoformat(data)
        elif type(data) == int:
            return datetime.fromtimestamp(data / 1e3)
        else:
            return None
