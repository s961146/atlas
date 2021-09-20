#!/usr/bin/env python3

'''
CPSC 415 -- Homework #2 template
Stephen Davies, University of Mary Washington, fall 2021
'''
import math

from atlas import Atlas
import numpy as np
import logging
import sys


def find_best_path(atlas):
    '''Finds the best path from src to dest, based on costs from atlas.
    Returns a tuple of two elements. The first is a list of city numbers,
    starting with 0 and ending with atlas.num_cities-1, that gives the
    optimal path between those two cities. The second is the total cost
    of that path.'''

    # THIS IS WHERE YOUR AMAZING CODE GOES

    # Here's a (bogus) example return value:

    def find_nonzero_indexes(x):
        dict = []
        for i in range(0, atlas.get_num_cities()):
            t = atlas.get_road_dist(x, i)
            if t != 0 and t != math.inf:
                dict.append(i)
        return dict

    apath = [0]

    distance = 0.
    num_city = atlas.get_num_cities()

    d = find_nonzero_indexes(0)

    currrnt_city = 0
    while True:

        if currrnt_city == num_city - 1:
            break

        for i in apath:
            if i in d:
                d.remove(i)

        min_tuple = ()

        for key in d:
            temp = atlas.get_road_dist(currrnt_city, key) + atlas.get_crow_flies_dist(key, num_city - 1)
            if min_tuple:
                if min_tuple[1] > temp:
                    min_tuple = (key, temp)
            else:
                min_tuple = (key, temp)

        if min_tuple:
            distance = distance + atlas.get_road_dist(currrnt_city, min_tuple[0])
            currrnt_city = min_tuple[0]

        apath.append(currrnt_city)
        d = find_nonzero_indexes(currrnt_city)
    print('path: {0}, dist {1} '.format(apath, distance))

    return (apath, distance)


if __name__ == '__main__':

    if len(sys.argv) not in [2, 3]:
        print("Usage: gps.py numCities|atlasFile [debugLevel].")
        sys.exit(1)

    if len(sys.argv) > 2:
        if sys.argv[2] not in ['DEBUG', 'INFO', 'WARNING', 'ERROR']:
            print('Debug level must be one of: DEBUG, INFO, WARNING, ERROR.')
            sys.exit(2)
        logging.getLogger().setLevel(sys.argv[2])
    else:
        logging.getLogger().setLevel('INFO')

    try:
        num_cities = int(sys.argv[1])
        logging.info('Building random atlas with {} cities...'.format(
            num_cities))
        usa = Atlas(num_cities)
        logging.info('...built.')
    except:
        logging.info('Loading atlas from file {}...'.format(sys.argv[1]))
        usa = Atlas.from_filename(sys.argv[1])
        logging.info('...loaded.')

    path, cost = find_best_path(usa)
    print('Best path from {} to {} costs {}: {}.'.format(0,
                                                         usa.get_num_cities() - 1, cost, path))
    print('You expanded {} nodes: {}'.format(len(usa._nodes_expanded),
                                             usa._nodes_expanded))
