from datetime import datetime
from typing import Set
from enum import Enum
from dataclasses import dataclass


class Category(Enum):
    Backtesting = "backtesting"
    Library = "library"

class Feature(Enum):
    Backtesting = "backtesting"
    Live = "Live"

class Language(Enum):
    Python = "python"
    Rust = "rust"

@dataclass
class Repo:
    name: str
    url: str
    description: str
    last_update: datetime
    repo_stars: int

    def check(self):
        ...

@dataclass
class Record:
    name: str
    desciption: str
    repo: Repo
    category: Category
    features: Set[Feature]
    languages: Set[Language]
    tags: Set[str]

    

