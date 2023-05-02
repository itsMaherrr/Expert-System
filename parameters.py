from enum import Enum

class TypesDeChainages (Enum):
    AVANT = 1
    ARRIERE = 2

class Parcours (Enum):
    LARGEUR = 1
    PROFONDEUR = 2

class Regimes(Enum):
    irrevocable = 1
    parTentative = 2

class Monotonie (Enum):
    monotone = 1
    nonMonotone = 2