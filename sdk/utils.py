'''
 * @file utils.py
 * @author Krisna Pranav
 * @brief utils
 * @version 1.0
 * @date 2024-11-25
 *
 * @copyright Copyright (c) 2024 ThunderPayment Developers, Krisna Pranav
'''

import inspect
import json
import traceback

from collections.abc import Callable
from decimal import Decimal
from typing import Any

from .logger import logger

CONVERT_RATE = 100000000

def convert_amount_type(amount: str | Decimal) -> Decimal:
    if amount == "None":
        return Decimal("Nan")

    return Decimal(amount)

def satoshis(amount: str | Decimal) -> int:
    return int(convert_amount_type(amount) * CONVERT_RATE)
