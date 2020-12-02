# -*- coding: utf-8 -*-

# City Guide: A sample Alexa Skill Lambda function
# This function shows how you can manage data in objects and arrays,
# choose a random recommendation,
# call an external API and speak the result,
# handle YES/NO intents with session attributes,
# and return text data on a card.

import logging
import random
import gettext

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.dispatch_components import (
    AbstractRequestHandler, AbstractExceptionHandler,
    AbstractRequestInterceptor)
from ask_sdk_core.utils import is_intent_name, is_request_type

from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard

from alexa import data, util

# Skill Builder object
sb = SkillBuilder()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# Request Handler classes
class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for skill launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In LaunchRequestHandler")
        logger.info(handler_input.attributes_manager.request_attributes)
        _ = handler_input.attributes_manager.request_attributes["_"]

        # logger.info(_("This is an untranslated message"))

        speech = _(data.WELCOME)
        speech += " " + _(data.HELP)
        handler_input.response_builder.speak(speech)
        handler_input.response_builder.ask(_(
            data.GENERIC_REPROMPT))
        return handler_input.response_builder.response


class AboutIntentHandler(AbstractRequestHandler):
    """Handler for about intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AboutIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In AboutIntentHandler")
        _ = handler_input.attributes_manager.request_attributes["_"]

        handler_input.response_builder.speak(_(data.ABOUT))
        return handler_input.response_builder.response
        
class LunchElementaryTodayIntentHandler(AbstractRequestHandler):
    """Handler for Lunch Elementary Today intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("LunchElementaryTodayIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In LunchElementaryTodayIntentHandler")

        attribute_manager = handler_input.attributes_manager
        session_attr = attribute_manager.session_attributes

        lunchItem = util.get_lunch_for_today(data.LUNCHMENU_DATA_ELEMENTARY)

        session_attr["lunchItem"] = lunchItem["item"]
        speech = ("Today's lunch in elementary is {}.").format(lunchItem["item"])

        handler_input.response_builder.speak(speech)
        return handler_input.response_builder.response


class LunchElementaryTomorrowIntentHandler(AbstractRequestHandler):
    """Handler for Lunch Elementary Tomorrow intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("LunchElementaryTomorrowIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In LunchElementaryTomorrowIntentHandler")

        attribute_manager = handler_input.attributes_manager
        session_attr = attribute_manager.session_attributes

        lunchItem = util.get_lunch_for_tomorrow(data.LUNCHMENU_DATA_ELEMENTARY)

        session_attr["lunchItem"] = lunchItem["item"]
        speech = ("Tomorrow's lunch in elementary is {}.").format(lunchItem["item"])

        handler_input.response_builder.speak(speech)
        return handler_input.response_builder.response

class LunchMiddleSchoolTodayIntentHandler(AbstractRequestHandler):
    """Handler for Lunch MiddleSchool Today intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("LunchMiddleSchoolTodayIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In LunchMiddleSchoolTodayIntentHandler")

        attribute_manager = handler_input.attributes_manager
        session_attr = attribute_manager.session_attributes

        lunchItem = util.get_lunch_for_today(data.LUNCHMENU_DATA_MIDDLESCHOOL)

        if(lunchItem["item"].find(":") == 1):
            items = lunchItem["item"].split(":")
            msg = "Today at Middle School is {article} {day} day, and today's lunch is {item}".format(article="an" if items[0] == "A" else "a", day=items[0], item=items[1])
        else:
            msg = "Today's lunch at Middle School is {}".format(lunchItem["item"])

        session_attr["lunchItem"] = msg
        speech = (msg)

        handler_input.response_builder.speak(speech)
        return handler_input.response_builder.response

class LunchMiddleSchoolTomorrowIntentHandler(AbstractRequestHandler):
    """Handler for Lunch MiddleSchool Tomorrow intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("LunchMiddleSchoolTomorrowIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In LunchMiddleSchoolTomorrowIntentHandler")

        attribute_manager = handler_input.attributes_manager
        session_attr = attribute_manager.session_attributes

        lunchItem = util.get_lunch_for_tomorrow(data.LUNCHMENU_DATA_MIDDLESCHOOL)

        if(lunchItem["item"].find(":") == 1):
            items = lunchItem["item"].split(":")
            msg = "Tomorrow at Middle School will be {article} {day} day, and lunch will be {item}".format(article="an" if items[0] == "A" else "a", day=items[0], item=items[1])
        else:
            msg = "Tomorrow's lunch at Middle School will be {}".format(lunchItem["item"])

        session_attr["lunchItem"] = msg
        speech = (msg)

        handler_input.response_builder.speak(speech)
        return handler_input.response_builder.response


class LunchTodayIntentHandler(AbstractRequestHandler):
    """Handler for Lunch Today intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("LunchTodayIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In LunchTodayIntentHandler")

        attribute_manager = handler_input.attributes_manager
        session_attr = attribute_manager.session_attributes

        lunchItemElementaryRaw = util.get_lunch_for_today(data.LUNCHMENU_DATA_ELEMENTARY)
        lunchItemMiddleSchoolRaw = util.get_lunch_for_today(data.LUNCHMENU_DATA_MIDDLESCHOOL)

        abDay = ""
        if(lunchItemMiddleSchoolRaw["item"].find(":") == 1):
            items = lunchItemMiddleSchoolRaw["item"].split(":")
            abDay = items[0]
            lunchItemMiddleSchool = items[1]
        else:
            lunchItemMiddleSchool = lunchItemMiddleSchoolRaw["item"]

        lunchItemElementary = lunchItemElementaryRaw["item"]

        if lunchItemElementary == lunchItemMiddleSchool:
            speech = ("Today's lunch at both schools are the same: {}.").format(lunchItemElementary)
        else:
            speech = ("Today's lunch in elementary is {}, and at Middle School it is {}.").format(lunchItemElementary, lunchItemMiddleSchool)

        if abDay:
            speech += " And today is {article} {day} day at Middle school.".format(article="an" if abDay == "A" else "a", day=abDay)

        session_attr["lunchItemElementary"] = lunchItemElementary
        session_attr["lunchItemMiddleSchool"] = lunchItemMiddleSchool

        handler_input.response_builder.speak(speech)
        return handler_input.response_builder.response


class LunchTomorrowIntentHandler(AbstractRequestHandler):
    """Handler for Lunch Tomorrow intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("LunchTomorrowIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In LunchTomorrowIntentHandler")

        attribute_manager = handler_input.attributes_manager
        session_attr = attribute_manager.session_attributes

        lunchItemElementaryRaw = util.get_lunch_for_tomorrow(data.LUNCHMENU_DATA_ELEMENTARY)
        lunchItemMiddleSchoolRaw = util.get_lunch_for_tomorrow(data.LUNCHMENU_DATA_MIDDLESCHOOL)

        abDay = ""
        if(lunchItemMiddleSchoolRaw["item"].find(":") == 1):
            items = lunchItemMiddleSchoolRaw["item"].split(":")
            abDay = items[0]
            lunchItemMiddleSchool = items[1]
        else:
            lunchItemMiddleSchool = lunchItemMiddleSchoolRaw["item"]

        lunchItemElementary = lunchItemElementaryRaw["item"]

        if lunchItemElementary == lunchItemMiddleSchool:
            speech = ("Tomorrow's lunch at both schools are the same: {}.").format(lunchItemElementary)
        else:
            speech = ("Tomorrow's lunch in elementary is {}, and at Middle School it is {}.").format(lunchItemElementary, lunchItemMiddleSchool)

        if abDay:
            speech += " And tomorrow will be {article} {day} day at Middle school.".format(article="an" if abDay == "A" else "a", day=abDay)

        session_attr["lunchItemElementary"] = lunchItemElementary
        session_attr["lunchItemMiddleSchool"] = lunchItemMiddleSchool

        handler_input.response_builder.speak(speech)
        return handler_input.response_builder.response


class NoMoreInfoIntentHandler(AbstractRequestHandler):
    """Handler for no to get no more info intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        session_attr = handler_input.attributes_manager.session_attributes
        return (is_intent_name("AMAZON.NoIntent")(handler_input) and
                "restaurant" in session_attr)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In NoMoreInfoIntentHandler")

        speech = ("Ok.  Enjoy your meal! "
                  "<say-as interpret-as='interjection'>bon appetit</say-as>")
        handler_input.response_builder.speak(speech).set_should_end_session(
            True)
        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for skill session end."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In SessionEndedRequestHandler")
        logger.info("Session ended with reason: {}".format(
            handler_input.request_envelope.request.reason))
        return handler_input.response_builder.response


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for help intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In HelpIntentHandler")
        _ = handler_input.attributes_manager.request_attributes["_"]

        handler_input.response_builder.speak(_(
            data.HELP)).ask(_(data.HELP))
        return handler_input.response_builder.response


class ExitIntentHandler(AbstractRequestHandler):
    """Single Handler for Cancel, Stop intents."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or
                is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In ExitIntentHandler")
        _ = handler_input.attributes_manager.request_attributes["_"]

        handler_input.response_builder.speak(_(
            data.STOP)).set_should_end_session(True)
        return handler_input.response_builder.response


# Exception Handler classes
class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Catch All Exception handler.

    This handler catches all kinds of exceptions and prints
    the stack trace on AWS Cloudwatch with the request envelope."""
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)
        logger.info("Original request was {}".format(
            handler_input.request_envelope.request))

        speech = "Sorry, there was some problem. Please try again!!"
        handler_input.response_builder.speak(speech).ask(speech)

        return handler_input.response_builder.response

class LocalizationInterceptor(AbstractRequestInterceptor):
    """Add function to request attributes, that can load locale specific data."""
    def process(self, handler_input):
        # type: (HandlerInput) -> None
        locale = handler_input.request_envelope.request.locale
        logger.info("Locale is {}".format(locale))
        i18n = gettext.translation(
            'base', localedir='locales', languages=[locale], fallback=True)
        handler_input.attributes_manager.request_attributes[
            "_"] = i18n.gettext

# Add all request handlers to the skill.
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(AboutIntentHandler())
sb.add_request_handler(LunchTodayIntentHandler())
sb.add_request_handler(LunchTomorrowIntentHandler())
sb.add_request_handler(LunchElementaryTodayIntentHandler())
sb.add_request_handler(LunchElementaryTomorrowIntentHandler())
sb.add_request_handler(LunchMiddleSchoolTodayIntentHandler())
sb.add_request_handler(LunchMiddleSchoolTomorrowIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(ExitIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())

# Add exception handler to the skill.
sb.add_exception_handler(CatchAllExceptionHandler())

# Add locale interceptor to the skill.
sb.add_global_request_interceptor(LocalizationInterceptor())

# Expose the lambda handler to register in AWS Lambda.
lambda_handler = sb.lambda_handler()
