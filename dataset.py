import numpy as np

import planetary_positions
from normalizers import Normalizer
from normalizers import PositionNormalizer


class PlanetData(object):

    def __init__(self):
        self.raw_positions = planetary_positions.generate()

        self.gen_normalizers()
        self.apply_normalizers()

        self.index_current = 0

        return

    def next_batch(self, batch_size):
        b = self.index_current
        e = self.index_current + batch_size

        times = self.positions['days'][b:e]

        return

    def gen_normalizers(self):
        self.normalizers = {
            'days': Normalizer(self.raw_positions['days'])}
        for planet in self.raw_positions.planets():
            print PositionNormalizer(self.raw_positions[planet])
            self.normalizers[planet] = PositionNormalizer(self.raw_positions[planet])

        return

    def apply_normalizers(self):

        print self.normalizers
        self.norm_positions = {
            'days': self.normalizers['days'].apply(self.raw_positions['days'])
        }
        for planet in self.raw_positions.planets():
            self.norm_positions[planet] = self.normalizers[planet].apply(
                self.raw_positions[planet])

        print self.norm_positions
        return
