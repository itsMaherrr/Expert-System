from base_des_regles import BR
from base_des_faits import BF
class BC :
    def __init__(self, bf=-1, br=-1):
        if (bf == -1):
            self.baseDeFaits = BF()
        else :
            self.baseDeFaits = bf
        if (bf == -1):
            self.baseDeRegles = BR()
        else :
            self.baseDeRegles = br
