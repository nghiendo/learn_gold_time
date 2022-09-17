class Categories():
    def __init__(self, id, name, root) -> None:
        id = id
        name = name
        root = root
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "root": self.root,
        }