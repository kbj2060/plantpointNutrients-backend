from repository.repo import BaseRepo
from domain.entities.automation_history import AutomationHistory as eAutomationHistory
from repository import models
from controllers.app import session


class AutomationHistoryRepository(BaseRepo):
    def __init__(self) -> None:
        super().__init__()
        self.entity = eAutomationHistory
        self.model = models.AutomationHistory

    def read(self, filters):
        query = session.query(self.model)
        print(filters)
        if "subject__eq" in filters:
            result_models = query.filter(self.model.subject == filters["subject__eq"]).order_by(self.model.id.desc()).limit(1)
            return self._model2entity(models=result_models.first(), entity=self.entity)
            
    def create(self, subject, start, isCompledted) -> None:
        new_automation_history: models.AutomationHistory =self.model(subject=subject, start=start, isCompledted=isCompledted)
        session.add(new_automation_history)
        session.commit()

automationHistoryRepository = AutomationHistoryRepository()
