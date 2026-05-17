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


class DataStream:
    def __init__(self) -> None:
        self._processors: List[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        if not isinstance(proc, DataProcessor):
            raise ValueError("Processor must be an instance of DataProcessor")
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            found = False
            for proc in self._processors:
                if proc.validate(item):
                    proc.ingest(item)
                    found = True
                    break
            if not found:
                print(f"Can't process element in stream: {item}")

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return

        for proc in self._processors:
            name = proc.__class__.__name__.replace("Processor", " Processor")
            total = proc._processed_count + len(proc._data_storage)
            remaining = len(proc._data_storage)
            print(f"{name}: total {total} items processed,"
                  f" remaining {remaining} on processor")


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")

    print("Initialize Data Stream...")
    stream_service = DataStream()
    stream_service.print_processors_stats()

    print("\nRegistering Numeric Processor...")
    num_proc = NumericProcessor()
    stream_service.register_processor(num_proc)

    raw_data = [
        'Hello world',
        [3.14, 1, 2.71],
        [{'log_level': 'WARNING', 'log_message': 'Telnet access!'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
    ]

    print("Send first batch of data on stream...")
    stream_service.process_stream(raw_data)
    stream_service.print_processors_stats()

    print("\nRegistering other data processors...")
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    stream_service.register_processor(text_proc)
    stream_service.register_processor(log_proc)

    print("Send the same batch again...")
    stream_service.process_stream(raw_data)
    stream_service.print_processors_stats()

    print("\nConsume some elements from the data "
          "processors: Numeric 3, Text 2, Log 1")
    for _ in range(2):
        num_proc.output()
    for _ in range(2):
        text_proc.output()
    log_proc.output()

    stream_service.print_processors_stats()
