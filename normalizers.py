import numpy as np

class Normalizer(object):

    def __init__(self, values):
        self._set_stats(values)
        return

    def _set_stats(self, values):
        self.m = np.mean(values)
        self.std = np.std(values)

        return

    def apply(self, values):
        res = (values - self.m) / self.std
        return res


class RightAcensionNormalizer(Normalizer):

    def _find_jumps(self, values):
        delta_ra = values[1:] - values[:-1]
        jumps = delta_ra < - 1.5 * np.pi
        self.cumulated_jumps = np.insert(np.cumsum(jumps), 0, 0)
        return

    def _transform_ra(self, values):
        return values + self.cumulated_jumps * 2.0 * np.pi

    def _set_stats(self, values):
        """ Transform right ascension into a contious angle """

        self._find_jumps(values)
        values = self._transform_ra(values)
        super(RightAcensionNormalizer, self)._set_stats(values)
        return


class PositionNormalizer(object):
    def __init__(self, positions):
        self.rac_normalizer = RightAcensionNormalizer(positions['ra'])
        self.dec_normalizer = Normalizer(positions['dec'])
        return

    def apply(self, positions):
        res = {'ra': self.rac_normalizer.apply(positions['ra']),
               'dec': self.dec_normalizer.apply(positions['dec'])}

        return res
