import copy


class Fuzzynum(object):
    qrung = None
    md = None
    nmd = None

    def __init__(self):
        pass

    def score(self):
        return self.md ** self.qrung - self.nmd ** self.qrung

    def isEmpty(self):
        if self.md is None and self.nmd is None:
            return True
        else:
            return False

    def isEmpty_half(self):
        if self.md is None or self.nmd is None:
            return True
        else:
            return False

    def complement(self):
        pass

    def algebraicPower(self, l):
        newFN = copy.copy(self)
        newFN.md = self.md ** l
        newFN.nmd = (1 - (1 - self.nmd ** self.qrung) ** l) ** (1 / self.qrung)
        return newFN

    def algebraicTimes(self, l):
        newFN = copy.copy(self)
        newFN.md = (1 - (1 - self.md ** self.qrung) ** l) ** (1 / self.qrung)
        newFN.nmd = self.nmd ** l
        return newFN

    def einsteinPower(self, l):
        newFn = copy.copy(self)
        newFn.md = ((2 * (self.md ** self.qrung) ** l) / (
                    (2 - self.md ** self.qrung) ** l + (self.md ** self.qrung) ** l)) ** (1 / self.qrung)
        newFn.nmd = (((1 + self.nmd ** self.qrung) ** l - (1 - self.nmd ** self.qrung) ** l) / (
                    (1 + self.nmd ** self.qrung) ** l + (1 - self.nmd ** self.qrung) ** l)) ** (1 / self.qrung)
        return newFn

    def einsteinTimes(self, l):
        newFn = copy.copy(self)
        newFn.md = (((1 + self.md ** self.qrung) ** l - (1 - self.md ** self.qrung) ** l) / (
                    (1 + self.md ** self.qrung) ** l + (1 - self.md ** self.qrung) ** l)) ** (1 / self.qrung)
        newFn.nmd = ((2 * (self.nmd ** self.qrung) ** l) / (
                    (2 - self.nmd ** self.qrung) ** l + (self.nmd ** self.qrung) ** l)) ** (1 / self.qrung)
        return newFn