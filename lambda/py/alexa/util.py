# -*- coding: utf-8 -*-

import requests
from ask_sdk_model import IntentRequest
from typing import Union, Dict, List
from datetime import datetime, timedelta
from pytz import timezone

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
    todayUtc = datetime.now(timezone('UTC'))
    today = todayUtc.astimezone(timezone('US/Eastern'))
    return get_lunch(lunch_data, today)

def get_lunch_for_tomorrow(lunch_data):
    tomorrowUtc = (datetime.now(timezone('UTC')) + timedelta(days=1))
    tomorrow = tomorrowUtc.astimezone(timezone('US/Eastern'))
    return get_lunch(lunch_data, tomorrow)

def get_resolved_value(request, slot_name):
    """Resolve the slot name from the request."""
    # type: (IntentRequest, str) -> Union[str, None]
    try:
        return request.intent.slots[slot_name].value
    except (AttributeError, ValueError, KeyError, IndexError):
        return None
