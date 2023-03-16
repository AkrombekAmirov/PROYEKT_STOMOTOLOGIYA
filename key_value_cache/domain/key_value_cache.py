import abc


class KeyValueCache(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key: str) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def set(self, key: str, value: str = None) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def expire(self, key: str) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def exists(self, key: str) -> bool:
        raise NotImplementedError
