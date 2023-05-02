from parameters import TypesDeChainages, Parcours, Regimes, Monotonie

class MoteurInference:
    def __init__(self, bc, but=-1, chainage = TypesDeChainages.AVANT, parcours = Parcours.PROFONDEUR, regime = Regimes.irrevocable, monotonie = Monotonie.nonMonotone):
        self.br = bc.baseDeRegles.baseDeRegles
        self.bf = bc.baseDeFaits.baseDeFaits
        self.chainage = chainage
        self.parcours = parcours
        self.regime = regime
        self.monotonie = monotonie
        self.but = but
        self.atteint = False
        self.desactive = []
        self.cycle = 1
        self.file = open("trace.txt","w")

    def filtrerApplicables(self):
        ensembleDeConflit = []
        for regle in self.br :
            if regle not in self.desactive:
                premisses = self.getPremisses(regle)
                estCompatible = True
                for premisse in premisses :
                    estCompatible = estCompatible and (premisse in self.bf)
                if (estCompatible):
                    ensembleDeConflit.append(self.br.index(regle))
        return ensembleDeConflit

    def selectionnerRegle(self, ensembleDeConflit):
        return min(ensembleDeConflit)

    def appliquerRegle(self, index):
        action = self.br[index].split("=")[0].strip()
        self.bf.add(action)
        return action

    def desactiverRegle(self, index):
        self.desactive.append(self.br[index])

    def getPremisses(self, regle):
        premisses = []
        for premisse in regle.split("=")[1].strip().split(","):
            premisses.append(premisse.strip())
        return premisses

    def chainageAvant(self):
        ensembleDeConflit = self.filtrerApplicables()
        ensembleDeConflits = []
        for element in ensembleDeConflit :
            ensembleDeConflits.append("R"+str(element+1))
        self.file.write("Ensemble de Conflit : "+str(ensembleDeConflits)+"\n")
        if(ensembleDeConflit):
            match self.parcours:
                case Parcours.PROFONDEUR:
                    index = self.selectionnerRegle(ensembleDeConflit)
                    self.file.write("Choix : R"+str(index+1)+"\n")
                    result = self.appliquerRegle(index)
                    self.file.write("Base de faits : " + str(self.bf) + "\n")
                    self.desactiverRegle(index)
                    if self.but != -1 and result == self.but :
                        self.atteint = True
                case Parcours.LARGEUR:
                    for index in ensembleDeConflit :
                        result = self.appliquerRegle(index)
                        self.desactiverRegle(index)
                        if self.but != -1 and result == self.but:
                            self.atteint = True
                    self.file.write("Base de faits : " + str(self.bf) + "\n")
            return True
        else :
            return False

    def verifier(self, but):
        if self.but != -1 and (self.but in self.bf or but in self.bf) :
            self.file.write("Cycle : " + str(self.cycle) + "\n")
            self.cycle += 1
            if (self.chainage == TypesDeChainages.AVANT):
                self.file.write(str(self.but)+" est dans la base des faits")
                self.file.close()
            else :
                self.file.write("But : "+str(but)+"\n")
                self.file.write(str(but)+" est dans la base des faits\n")
            return True
        else :
            match self.chainage:
                case TypesDeChainages.AVANT:
                    self.file.write("Cycle : " + str(self.cycle) + "\n")
                    self.cycle += 1
                    while not self.atteint and self.chainageAvant():
                        self.file.write("Cycle : "+str(self.cycle)+"\n")
                        self.cycle += 1
                        pass
                    self.file.close()
                    if self.but != -1 and not self.atteint :
                        return False
                    else :
                        return True
                case TypesDeChainages.ARRIERE:
                    self.file.write("Cycle : " + str(self.cycle)+"\n")
                    self.cycle += 1
                    self.file.write("But : "+str(but)+"\n")
                    return self.chainageArriere(but)

    def chainageArriere(self, but):
        results = self.actionCompatibles(but)
        rules = []
        for num in results :
            rules.append("R"+str(num+1))
        self.file.write("Ensemble de Conflit : "+str(rules)+"\n")
        false = False
        if results :
            index = self.selectionnerRegle(results)
            self.file.write("On declanche R"+str(index+1)+"\n")
            cycleCopy = self.cycle - 1
            results.remove(index)
            reglesRestantes = results
            bfCopy = set(list(self.bf).copy())
            while (not self.prouver(index)):
                if (self.regime == Regimes.parTentative):
                    if (reglesRestantes) :
                        index = self.selectionnerRegle(reglesRestantes)
                        reglesRestantes.remove(index)
                        if (self.monotonie == Monotonie.nonMonotone) or (self.bf == bfCopy):
                            self.bf = bfCopy
                        self.file.write("echec\nbacktracking vers Cycle "+str(cycleCopy)+", on declanche R"+str(index+1)+"\n")
                    else :
                        false = True
                        break
                else :
                    return False
            if false:
                return False
        else :
            return False
        self.bf.add(but)
        return True

    def prouver(self, index):
        regle = self.br[index]
        ldp = regle.split("=")[1].strip().split(",")
        self.file.write("LDP : "+str(ldp)+"\n")
        for premisse in ldp:
            true = self.verifier(premisse.strip())
            if not true:
                return False
        return True

    def actionCompatibles(self, but):
        reglesCompatibles = []
        for regle in self.br :
            if regle.split("=")[0].strip() == but :
                reglesCompatibles.append(self.br.index(regle))
        return reglesCompatibles




