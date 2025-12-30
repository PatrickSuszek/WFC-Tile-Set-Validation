import itertools
import math

from my_logger import Logger

def _common(logger: Logger, data: dict[int, set[int]]) -> tuple[bool, set[int]]:
    valid = True

    # check the existence of tile constraint pairs
    if len(data) == 0:
        logger.info("The given constraint set is empty")
        valid = False

    # check that no constraint is empty
    for t, c in data.items():
        if len(c) == 0:
            logger.info(f"The constraint of tile {t} is an empty set")
            valid = False

    # check only known tiles are used
    tiles_known = set(data.keys())
    tiles_used = set.union(*data.values())
    valid &= tiles_used.issubset(tiles_known)

    if not valid:
        logger.info(f"Constraints are using unknown tiles")

    return valid, tiles_known

def two_dim(logger: Logger, data: dict[int, set[int]]) -> bool:
    valid, _ = _common(logger, data)
    if not valid:
        return False

    # create helper variables
    found_pairs = []
    seen_pairs = set()
    max_pair_cnt = math.comb(len(data), 2)

    # find all possible pairs of tile ids
    for _, constraint in data.items():
        if len(found_pairs) == max_pair_cnt:
            break
        pairs = list(itertools.combinations(constraint, 2))
        for p in pairs:
            if p[0] != p[1]:
                fs = frozenset(p)
                if fs not in seen_pairs:
                    seen_pairs.add(fs)
                    found_pairs.append(p)

    # check all possible tile pairs
    for p in found_pairs:
        c_a = set(data[p[0]])
        c_b = set(data[p[1]])

        if len(c_a & c_b) == 0:
            logger.info(f"The intersection for the pair {p} is an empty set")
            valid = False

    return valid


def chunk(logger: Logger, data: dict[int, set[int]], neighbors: int = 4) -> bool:
    valid, _ = _common(logger, data)
    if not valid:
        return False

    # edge case handling, tile count less then neigbors
    neighbors = min(neighbors, len(data))

    # calculate all combinations of tiles
    tiles = set(data.keys())
    combinations = list(itertools.combinations(tiles, neighbors))

    for comb in combinations:
        constraints = []
        for c in comb:
            constraints.append(data[c])

        intersection = set.intersection(*constraints)

        if len(intersection) == 0:
            logger.info(f"The intersection for the combination {comb} is an empty set")
            valid = False

    return valid