import numpy as np

import planetary_positions


class PlanetData(object):

    def __init__(self):
        self.positions = planetary_positions.generate()
        self.index_current = 0
        self.normalize()
        return

    def next_batch(self, batch_size):
        b = self.index_current
        e = self.index_current + batch_size

        times = self.positions['days'][b:e]

        return

    def normalize(self):
        self.normalizers = {}
        for planet in self.positions.planets():
            self.normalizers[planet] = Normalizer(self.positions[planet])

        return


class Normalizer(object):
    def __init__(self, positions):
        print positions
        self.ra_corrections = []

        self.transform_ra(positions['ra'])

        return

    def transform_ra(self, ra):
        delta_ra = ra[1:] - ra[:-1]

        print delta_ra
        print np.min(delta_ra)
        print np.max(delta_ra)
        jumps = delta_ra < - 1.5 * np.pi
        print jumps
        print np.sum(jumps)
        return
