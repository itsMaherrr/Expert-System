from chainages import TypesDeChainages
from base_de_connaissances import BC


class MoteurInference:
    def __init__(self, but=-1):
        self.but = but
        if self.but == -1:
            self.chainage = TypesDeChainages.AVANT
        else:
            self.chainage = TypesDeChainages.ARRIERE
        self.bc = BC()
        self.etat = []
        self.cycle = 1
        self.reglesInchanges = self.bc.baseDeRegles.baseDeRegles.copy()

    def verifier(self):
        match self.chainage:
            case TypesDeChainages.AVANT:  # verifier chainage avant
                self.verifierAvant()
            case TypesDeChainages.ARRIERE:  # verifier chainage arriere
                i=2

    def verifierAvant(self):
        self.reglesAppliques = []
        self.baseDesRegles = self.bc.baseDeRegles.baseDeRegles
        self.baseDeFaits = self.bc.baseDeFaits.baseDeFaits
        continuer = True
        while (continuer):
            print("Cycle :",self.cycle)
            continuer = self.inferenceAvant()
            print("Base de Faits : ", self.baseDeFaits,"\n")
            self.cycle += 1

    def inference(self):
        if self.but == -1 :
            self.inferenceAvant()
        else :
            self.pile = [self.but]
            #inference chainage arriere

    def inferenceArriere(self):
        reglesApplicables = self.filtrage(self.baseDesRegles, self.pile[-1:])
        if (not reglesApplicables) :
            return False
        else :
            regleIndex = self.selection(reglesApplicables)
            if (len(reglesApplicables)>1):
                self.saveState(reglesApplicables, reglesApplicables[regleIndex])
                # non complétée
                # faut implementer le choix du prochaine regle applicable au cas d'echec
                # idk

    def inferenceAvant(self):
        reglesApplicables = self.filtrage(self.baseDesRegles)
        print("Ensemble de Conflit :",reglesApplicables)
        if (not reglesApplicables):
            return False
        else:
            regleIndex = self.selection(reglesApplicables)
            numeroDeRegle = self.reglesInchanges.index(self.baseDesRegles[regleIndex])
            print("Choix : R"+str(numeroDeRegle+1))
            self.baseDeFaits.add(self.baseDesRegles[regleIndex].split("=")[0].strip())
            self.reglesAppliques.append(self.baseDesRegles.pop(regleIndex))
            return True

    def getPremisses(self, reglePremisses):
        premisses = []
        for reglePremisse in reglePremisses :
            premisse = reglePremisse.split("=")[1].strip()
            premisses.append(premisse)
        return premisses

    def getResults(self, reglePremisses):
        resultats = []
        for reglePremisse in reglePremisses :
            resultat = reglePremisse.split("=")[0].strip()
            resultats.append(resultat)
        return resultats

    def filtrage(self, regles, but=-1) :
        ensembleDeConflit = []
        if self.but == -1 :
            reglesPremisses = self.getPremisses(regles)
            for premisses in reglesPremisses :  # pour les premisses de chaque regle
                estCompatible = True
                for premisse in premisses.split(",") :  # pour chacune des premisses
                    estCompatible = estCompatible and (premisse.strip() in self.baseDeFaits)
                if estCompatible :
                    regleIndex = reglesPremisses.index(premisses)  #l'index de la regle
                    ensembleDeConflit.append(regleIndex)
        # Chainage Arriere
        else :
            reglesResultats = self.getResults(regles)
            for resultat in reglesResultats :
                if resultat == but :
                    ensembleDeConflit.append(reglesResultats.index(resultat))
        return ensembleDeConflit

    def selection(self, ensembleDeConflit):
        return min(ensembleDeConflit)

    #Chainage Arriere
    def saveState(self, conflit, regleApplique):
        pile = self.pile.copy()
        baseDeFaits = self.baseDeFaits
        ensembleDeConflit = conflit.copy().remove(regleApplique)
        etat = [pile, baseDeFaits, ensembleDeConflit]
        self.etat.append(etat)

