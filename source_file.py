from abc import ABC, abstractmethod

class SourceFile(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def __str__(self):
        return f'SourceFile: {self.name}'

class SourceClass(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

class SourceMethod(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

class SourceField(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

class SourceParameter(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name