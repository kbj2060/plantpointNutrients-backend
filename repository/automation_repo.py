from repository.repo import BaseRepo
from domain.entities.automation import AutomationHistory as eAutomationHistory
from domain.entities.automation import AutomationLed as eAutomationLed
from domain.entities.automation import AutomationRoofFan as eAutomationRoofFan
from domain.entities.automation import AutomationFan as eAutomationFan
from domain.entities.automation import AutomationAC as eAutomationAC
from repository import models
from controllers.app import session


class AutomationHistoryRepository(BaseRepo):
    def __init__(self) -> None:
        super().__init__()
        self.entity = eAutomationHistory
        self.model = models.AutomationHistory

    def read(self, filters):
        query = session.query(self.model)
        if "subject__eq" in filters:
            result_models = query.filter(self.model.subject == filters["subject__eq"], self.model.isCompleted == filters["isCompleted"]).order_by(self.model.id.desc()).limit(1)
            return self._model2entity(models=result_models.first(), entity=self.entity)
            
    def create(self, subject, createdAt, isCompleted) -> None:
        new_automation_history: models.AutomationHistory =self.model(subject=subject, createdAt=createdAt, isCompleted=isCompleted)
        session.add(new_automation_history)
        session.commit()

class AutomationACRepository(BaseRepo):
    def __init__(self) -> None:
        super().__init__()
        self.entity = eAutomationAC
        self.model = models.AutomationAC

    def read(self):
        query = session.query(self.model)
        result_models = query.order_by(self.model.id.desc()).limit(1)
        return self._model2entity(models=result_models.first(), entity=self.entity)
            
    def create(self, start, end, active) -> None:
        new_automation: models.AutomationAC =self.model(end=end, start=start, active=active)
        session.add(new_automation)
        session.commit()

class AutomationFanRepository(BaseRepo):
    def __init__(self) -> None:
        super().__init__()
        self.entity = eAutomationFan
        self.model = models.AutomationFan

    def read(self):
        query = session.query(self.model)
        result_models = query.order_by(self.model.id.desc()).limit(1)
        return self._model2entity(models=result_models.first(), entity=self.entity)
            
    def create(self, term, active) -> None:
        new_automation: models.AutomationFan =self.model(term=term, active=active)
        session.add(new_automation)
        session.commit()

class AutomationRoofFanRepository(BaseRepo):
    def __init__(self) -> None:
        super().__init__()
        self.entity = eAutomationRoofFan
        self.model = models.AutomationRoofFan

    def read(self):
        query = session.query(self.model)
        result_models = query.order_by(self.model.id.desc()).limit(1)
        return self._model2entity(models=result_models.first(), entity=self.entity)
            
    def create(self, term, active) -> None:
        new_automation: models.AutomationRoofFan =self.model(term=term, active=active)
        session.add(new_automation)
        session.commit()

class AutomationLedRepository(BaseRepo):
    def __init__(self) -> None:
        super().__init__()
        self.entity = eAutomationLed
        self.model = models.AutomationLed

    def read(self):
        query = session.query(self.model)
        result_models = query.order_by(self.model.id.desc()).limit(1)
        return self._model2entity(models=result_models.first(), entity=self.entity)
            
    def create(self, start, end, active) -> None:
        new_automation: models.AutomationLed = self.model(end=end, start=start, active=active)
        session.add(new_automation)
        session.commit()

        
automationHistoryRepository = AutomationHistoryRepository()
automationACRepository = AutomationACRepository()
automationFanRepository = AutomationFanRepository()
automationRoofFanRepository = AutomationRoofFanRepository()
automationLedRepository = AutomationLedRepository()
