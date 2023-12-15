from abc import ABC, abstractmethod


class Invoice(ABC):
    @abstractmethod
    def process_data(self, page_data: str, page_no: int):
        pass
