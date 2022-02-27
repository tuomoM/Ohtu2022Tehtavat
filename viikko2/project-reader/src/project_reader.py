from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)
        data = toml.loads(content)
        print(data)
        data = data['tool']
        data = data['poetry']
        print(data)
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(data['name'], data['description'], data['dependencies'], data['dev-dependencies'])
