from abc import ABC, abstractmethod
from typing import Any, Union, List, Dict


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data_storage: List[str] = []
        self._processed_count = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data_storage:
            raise IndexError("Storage is empty")
        result = (self._processed_count, self._data_storage.pop(0))
        self._processed_count += 1
        return result


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if (isinstance(data, list) and
                all(isinstance(i, (int, float)) for i in data)):
            return True
        return False

    def ingest(self, x: Union[int, float, List[Union[int, float]]]) -> None:
        if not self.validate(x):
            raise ValueError("Invalid data type for NumericProcessor")
        if isinstance(x, list):
            for i in x:
                self._data_storage.append(str(i))
        else:
            self._data_storage.append(str(x))

    def get_data(self) -> List[str]:
        return self._data_storage


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and all(isinstance(x, str) for x in data):
            return True
        return False

    def ingest(self, data: Union[str, List[str]]) -> None:
        if not self.validate(data):
            raise ValueError("Invalid data type for TextProcessor")
        if isinstance(data, list):
            for item in data:
                self._data_storage.append(item)
        else:
            self._data_storage.append(data)

    def get_data(self) -> List[str]:
        return self._data_storage


class LogProcessor(DataProcessor):
    def check_dict(self, data: Any) -> bool:
        if not isinstance(data, dict):
            return False
        for key, value in data.items():
            if not isinstance(key, str) or not isinstance(value, str):
                return False
        return True

    def validate(self, data: Any) -> bool:
        if self.check_dict(data):
            return True
        if isinstance(data, List) and all(self.check_dict(i) for i in data):
            return True
        return False

    def ingest(self, d: Union[Dict[str, str], List[Dict[str, str]]]) -> None:
        if not self.validate(d):
            raise ValueError("Invalid data type for LogProcessor")
        items = d if isinstance(d, list) else [d]
        for item in items:
            formatted_log = ", ".join([f"{k}: {v}" for k, v in item.items()])
            self._data_storage.append(formatted_log)

    def get_data(self) -> List[str]:
        return self._data_storage


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    num_processor = NumericProcessor()
    text_processor = TextProcessor()
    log_processor = LogProcessor()

    print("\nTest NumericProcessor...")
    print(f"Trying to validate input '42': {num_processor.validate(42)}")
    print(f"Trying to validate input 'Hello':"
          f" {num_processor.validate("Hello")}")
    num_processor.ingest(42)
    num_processor.ingest([3.14, 2.718])
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_processor.ingest("foo")  # type: ignore
    except ValueError as e:
        print(f"Got exception: {e}")
    print(f"Processing data: {num_processor.get_data()}")
    try:
        print(num_processor.output())
        print(num_processor.output())
        print(num_processor.output())
        print(num_processor.output())
    except Exception as e:
        print(f"Got exception: {e}")
    print(f"Processing data: {num_processor.get_data()}")

    print("\nTest TextProcessor...")
    print(f"Trying to validate input '42': {text_processor.validate(42)}")
    print(f"Trying to validate input 'Hello':"
          f" {text_processor.validate('Hello')}")
    text_processor.ingest("Hello")
    text_processor.ingest(["World", "Test"])
    print("Test invalid ingestion of string '123' without prior validation:")
    try:
        text_processor.ingest("123")
    except ValueError as e:
        print(f"Got exception: {e}")
    print(f"Processing data: {text_processor.get_data()}")
    print(text_processor.output())
    print(f"Processing data: {text_processor.get_data()}")

    print("\nTest LogProcessor...")
    print(f"Trying to validate input '{{\"event\": \"login\"}}':"
          f"{log_processor.validate({'event': 'login'})}")
    print(f"Trying to validate input '42': {log_processor.validate(42)}")
    log_processor.ingest({"event": "login", "user": "admin"})
    log_processor.ingest([{"event": "login", "user1": "yahya"},
                          {"event": "login", "user3": "ahmet"}])
    print(f"\nProcessing data: {log_processor.get_data()}")
    print(log_processor.get_data())
    print(log_processor.output())
    print(log_processor.output())
    print(f"Processing data: {log_processor.get_data()}")
