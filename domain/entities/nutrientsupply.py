from domain.entities.watersupply import WaterSupply

class NutrientSupply(WaterSupply):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)