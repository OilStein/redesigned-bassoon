import toml
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)

        parse_toml = toml.loads(content)
        #print(parse_toml)

        name = parse_toml["tool"]["poetry"]["name"]
        #print(name)
        desc = parse_toml["tool"]["poetry"]["description"]
        #print(desc)
        dependencies = parse_toml["tool"]["poetry"]["dependencies"]
        #print(dependencies)
        dev = parse_toml["tool"]["poetry"]["group"]["dev"]["dependencies"]
       #print(dev)

        lic = parse_toml["tool"]["poetry"]["license"]

        authors = parse_toml["tool"]["poetry"]["authors"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, authors , lic, dependencies, dev)
