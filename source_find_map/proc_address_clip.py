"""
    processes the address from system clip board
"""

import pyperclip
import logging


log_format = '%(asctime)s - %(levelname)s - %(message)s'
log_file = '../logs/log.txt'
logging.basicConfig(filename=log_file, level=logging.DEBUG, format=log_format)
logging.debug('Start')


def get_address():
    logging.debug('Fetching address from clipboard')
    address = pyperclip.paste()
    logging.debug('Done fetching')
    assert address != '', 'Address can not be empty!'
    return address


def print_addr(address):
    logging.debug('Called print_addr')
    print('You are looking for : {}'.format(address))
    logging.debug('Done')
