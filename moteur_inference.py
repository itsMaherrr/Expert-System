from chainages import TypesDeChainages
from base_de_connaissances import BC


class MoteurInference:
    def __init__(self, but=-1):
        if but == -1:
            self.chainage = TypesDeChainages.AVANT
        else:
            self.chainage = TypesDeChainages.ARRIERE
        self.bc = BC()

    def verifier(self):
        match self.chainage:
            case 1:  # verifier chainage avant
                i = 1
            case 2:  # verifier chainage arriere
                i=2

    def verifierAvant(self):
        reglesAppliques = []
        echec = False
        baseDesRegles = self.bc.baseDeRegles.baseDeRegles
        baseDeFaits = self.bc.baseDeFaits.baseDeFaits
        while ((baseDesRegles) and (not echec)):
            splited = baseDesRegles[0].split("=")
            conditions = splited[0].split(",")
            goal = splited[1]
            for condition in conditions :
                if condition in baseDeFaits :
                    condition = True
                else :
                    condition = False

