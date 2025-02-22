from models.iris_model import IrisTemplate


class InMemoryDatabase:
    def __init__(self):
        self.templates: dict[str, IrisTemplate] = {}

    def add_template(self, template: IrisTemplate):
        self.templates[template.user_id] = template

    def get_template(self, user_id: str) -> IrisTemplate | None:
        return self.templates.get(user_id)

    def get_all_templates(self) -> dict[str, IrisTemplate]:
        return self.templates
