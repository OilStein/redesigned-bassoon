class Project:
    def __init__(self, name, description, authors, lic, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.authors = authors
        self.lic = lic
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"
    
    def _stringify_to_bullet_list(self, items):
        return "\n".join(f"- {item}" for item in items) if len(items) > 0 else "-"


    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.lic or '-'}"
            f"\n"
            f"\nAuthors:\n{self._stringify_to_bullet_list(self.authors)}"
            f"\n"
            f"\nDependencies:\n{self._stringify_to_bullet_list(self.dependencies)}"
            f"\n"
            f"\nDevelopment dependencies:\n{self._stringify_to_bullet_list(self.dev_dependencies)}"
        )
