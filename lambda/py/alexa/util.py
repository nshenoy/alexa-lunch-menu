# -*- coding: utf-8 -*-

import requests
from ask_sdk_model import IntentRequest
from typing import Union, Dict, List
from datetime import datetime, timedelta

def get_lunch(lunch_data, menuDate):
    searchDate = menuDate.strftime("%Y-%m-%d")
    for lunchItem in lunch_data:
        if lunchItem["date"] == searchDate:
            return lunchItem

    if menuDate.weekday() < 5:
        return {"item": "NOTHING because it is a holiday!"}
    else:
        return {"item": "NOTHING because it is the weekend!"}        

def get_lunch_for_today(lunch_data):
    calcDate = datetime.today()
    return get_lunch(lunch_data, calcDate)

def get_lunch_for_tomorrow(lunch_data):
    calcDate = (datetime.today() + timedelta(days=1))
    return get_lunch(lunch_data, calcDate)

def get_resolved_value(request, slot_name):
    """Resolve the slot name from the request."""
    # type: (IntentRequest, str) -> Union[str, None]
    try:
        return request.intent.slots[slot_name].value
    except (AttributeError, ValueError, KeyError, IndexError):
        return None
