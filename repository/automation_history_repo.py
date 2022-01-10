from repository.repo import BaseRepo
from domain.entities.automation_history import AutomationHistory as eAutomationHistory
from repository import models
from controllers.app import session


class AutomationHistoryRepository(BaseRepo):
    def __init__(self) -> None:
        super().__init__()
        self.entity = eAutomationHistory
        self.model = models.AutomationHistory

    def create(self, subject, start, success) -> None:
        new_automation_history: models.AutomationHistory =self.model(subject=subject, start=start, success=success)
        session.add(new_automation_history)
        session.commit()

automationHistoryRepository = AutomationHistoryRepository()
