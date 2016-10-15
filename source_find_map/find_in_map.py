import proc_address_clip
import proc_address_sysarg


import webbrowser

"""
    The program will show the address on google maps
    on a browser tab. Your default browser will be used
"""

base_url = 'https://www.google.com/maps/place/'
address1 = proc_address_clip.get_address()
address2 = proc_address_sysarg.get_address()


def show_in_map(address):
    webbrowser.open(base_url + address)


#show_in_map(address1)
show_in_map(address2)
