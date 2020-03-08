from __future__ import absolute_import

from configparser import ConfigParser
import re, os, pathlib


def get_configuration():
    config_parser = ConfigParser()
    config_parser.read("config.ini")

    return config_parser


def get_qr_code():
    config = get_configuration()
    qr_code = config.get("login", "qr_code", fallback=None)
    qr_code = _check_qr_code(config, qr_code)

    return qr_code


def _check_qr_code(config, qr_code):
    if qr_code:
        qr_code_pattern = "^[A-Z0-9]{16}$"
        qr_code_is_valid = re.match(qr_code_pattern, qr_code)
        if qr_code_is_valid:
            qr_code = qr_code
        else:
            qr_code = None

    return qr_code
