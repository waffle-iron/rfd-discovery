from dominance.dominance_tools import RFDDiscovery
import utils.utils as ut

if __name__ == "__main__":
    nd = RFDDiscovery()
    with ut.timeit_context("Whole time"):
        print(nd.get_dominance("resources/dataset.csv", nd.naive_dominance, {"lhs": [1, 2, 3], "rhs": [0]}))
