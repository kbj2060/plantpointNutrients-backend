from domain.entities.temperature import Temperature

class Humidity(Temperature):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

