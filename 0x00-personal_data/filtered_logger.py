#!/usr/bin/env python3
"""
This python file contains function called filter_datum
that returns the log message obfuscated
"""
import re


def filter_datum(
        fields: list,
        redaction: str,
        message: str,
        seperator: str):
    """
    Obfuscated specified fields in a log message.
    """
    pattern = '|'.join([f"{field}=[^({seperator})]+" for field in fields])
    return re.sub(
            pattern,
            lambda m: m.group(0).split('=')[0] + f'={redaction}',
            message
            )
