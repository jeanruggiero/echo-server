"""
This module contains a function that returns the services provided
by a range of ports.
"""

import socket


def port_services(lower=20, upper=80):
    """
    Print the services provided by the given range of ports.
    Skip ports that are not found.
    """
    if lower < 0 or upper > 65535:
        raise ValueError('Provided port range out of bounds.' +
                         ' Must be within range of 0 to 65535.')

    for port in range(lower, upper+1):
        try:
            print('Port', port, ':', socket.getservbyport(port))
        except OSError:
            continue


if __name__ == '__main__':
    port_services()