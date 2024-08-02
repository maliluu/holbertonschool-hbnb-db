from src.models.base import Base
from src.persistence.repository import Repository


class DBRepository(Repository):

    def __init__(self) -> None:
        """ """

    def get_all(self, model_name: str) -> list:
        """ """
        return []

    def get(self, model_name: str, obj_id: str) -> Base | None:
        """ """

    def reload(self) -> None:
        """ """

    def save(self, obj: Base) -> None:
        """ """

    def update(self, obj: Base) -> Base | None:
        """ """

    def delete(self, obj: Base) -> bool:
        """ """
        return False
