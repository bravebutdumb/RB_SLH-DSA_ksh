class ADRS:
    def __init__(self):
        self.layer_adrs = bytearray(4)
        self.tree_adrs = bytearray(12)
        self.type = bytearray(4)

class WOTShash_ADRS(ADRS):
    def __init__(self):
        self.key_pair_adrs = bytearray(4)
        self.chain_adrs = bytearray(4)
        self.hash_adrs = bytearray(4)

class WOTSpkcomp_adrs(ADRS):
    def __init__(self):
        self.key_pair_adrs = bytearray(4)
        self.padding = bytearray(8)


class HashTree_adrs(ADRS):
    def __init__(self):
        self.padding = bytearray(4)
        self.tree_height = bytearray(4)
        self.tree_ind = bytearray(4)

class FORStree_adrs(ADRS):
    def __init__(self):
        self.key_pair_adrs = bytearray(4)
        self.tree_height = bytearray(4)
        self.tree_ind = bytearray(4)

class FORStrcomp_adrs(ADRS):
    def __init__(self):
        self.key_pair_adrs = bytearray(4)
        self.padding = bytearray(8)

class WOTSkeygen_adrs(ADRS):
    def __init__(self):
        self.key_pair_adrs = bytearray(4)
        self.chain_adrs = bytearray(4)
        self.hash_adrs = bytearray(4)

class FORSkeygen_adrs(ADRS):
    def __init__(self):
        self.key_pair_adrs = bytearray(4)
        self.tree_height = bytearray(4)
        self.tree_ind = bytearray(4)




