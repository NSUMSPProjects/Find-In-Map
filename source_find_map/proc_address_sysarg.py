"""
    processes the address from command line args
"""

import sys
import logging


log_format = '%(asctime)s - %(levelname)s - %(message)s'
log_file = '../logs/log.txt'
logging.basicConfig(filename=log_file, level=logging.DEBUG, format=log_format)
logging.debug('Start')


def get_address():
    assert len(sys.argv) > 1, 'Too few arguments to work with!'
    address = ' '.join(sys.argv[1:])
    logging.debug('Got address from sys.argv')
    return address


def print_addr(address):
    logging.debug('Called print_addr')
    print('You are looking for : {}'.format(address))
    logging.debug('Done')
