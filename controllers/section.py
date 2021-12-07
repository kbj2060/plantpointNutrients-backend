from controllers.app import app
from repository.section_repo import sectionRepository


@app.get("/section")
def read_sections():
    return sectionRepository.read()
