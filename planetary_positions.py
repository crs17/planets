#!/usr/bin/python

'''
Calculates planetary positions.

Usage 

'''

import ephem
from datetime import datetime
from datetime import timedelta
import matplotlib.pylab as plt
import numpy as np


class Positions(dict):

    def __init__(self, planets):

        for p in planets:
            self[p] = {'ra':[], 'dec':[]}

        self['time'] = []
        self['days'] = []
        return

    def planets(self):
        keys = super(Positions, self).keys()
        keys.remove('time')
        keys.remove('days')
        return keys


def generate(planets=[ephem.Mercury()],
             begin=datetime(2014, 12, 1),
             end=datetime(2017, 12, 5),
             step=timedelta(days=1)):


    positions = Positions(planets)

    time = begin
    while time <= end:
        for planet in planets:
            planet.compute(time)
            positions[planet]['ra'].append(planet.ra)
            positions[planet]['dec'].append(planet.dec)
        positions['time'].append(time)
        positions['days'].append((time - begin).total_seconds() / (3600 * 24))

        time += step
    
    for planet in planets:
        positions[planet]['ra'] = np.array(positions[planet]['ra'])
        positions[planet]['dec'] = np.array(positions[planet]['dec'])

    return positions


def plot(positions, out='planets.png'):

    for planet in positions.planets():
        ra = positions[planet]['ra']
        dec = [d * 180. / np.pi for d in positions[planet]['dec']]
        plt.plot(ra, dec, '.', label=planet.name)

    plt.xlim([0, 2 * np.pi])
    #plt.ylim([-np.pi/2.0, np.pi/2.0])

    plt.xticks(
        (0.0, np.pi ,2 * np.pi),
        ('00:00', '12:00', '24:00'))

    plt.xlabel(r'$\alpha$')
    plt.ylabel(r'$\delta$')
    plt.legend()

    plt.savefig(out)

    return


if __name__ == '__main__':
    positions = generate()
    plot(positions)
