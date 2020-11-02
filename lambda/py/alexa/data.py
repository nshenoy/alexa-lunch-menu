# -*- coding: utf-8 -*-

# Resolving gettext as _ for module loading.
from gettext import gettext as _

SKILL_NAME = "Locust Valley Lunch Menu"

WELCOME = _("Welcome to the Locust Valley Lunch Menu.")
HELP = _("Say about, to hear more about the skill, or what's for lunch at Locust Valley Elementary Schools or Middle School today or tomorrow.")
ABOUT = _("I'll tell you what's for lunch today or tomorrow in Locust Valley Elementary Schools or Middle School. You can ask what's for lunch at AMP, Ann McArthur, LVI, Locust Valley Intermediate, Bayville Primary, Bayville Intermediate, Elementary, or Middle School.")
STOP = _("Okay, see you next time!")
FALLBACK = _("The {} can't help you with that.")
GENERIC_REPROMPT = _("What can I help you with?")
LUNCHMENU = "November2020"
LUNCHMENU_DATA_ELEMENTARY = [
    {
        "date": "2020-11-02",
        "item": "Grilled Cheese Sandwich"
    },
    {
        "date": "2020-11-06",
        "item": "Pizza Slice"
    },
    {
        "date": "2020-11-09",
        "item": "Maple Glazed French Toast Sticks"
    },
    {
        "date": "2020-11-10",
        "item": "Hamburger on a Bun"
    },
    {
        "date": "2020-11-12",
        "item": "Chicken Nuggets"
    },
    {
        "date": "2020-11-13",
        "item": "Pizza Cheese Crunchers"
    },
    {
        "date": "2020-11-16",
        "item": "Maple Glazed French Toast Sticks"
    },
    {
        "date": "2020-11-17",
        "item": "Mozzarella Sticks with Marinara Sauce"
    },
    {
        "date": "2020-11-19",
        "item": "Popcorn Chicken"
    },
    {
        "date": "2020-11-20",
        "item": "NO SCHOOL FOR ELEMENTARY STUDENTS"
    },
    {
        "date": "2020-11-23",
        "item": "Egg and Cheese Sandwich on a Bun"
    },
    {
        "date": "2020-11-24",
        "item": "Mozzarella Bites"
    },
    {
        "date": "2020-11-30",
        "item": "Grilled Cheese Sandwich"
    }
]
LUNCHMENU_DATA_MIDDLESCHOOL = [
    {
        "date": "2020-11-02",
        "item": "A:Grilled Cheese Sandwich"
    },
    {
        "date": "2020-11-04",
        "item": "B:Mozzarella Sticks with Marinara Sauce"
    },
    {
        "date": "2020-11-05",
        "item": "A:Chicken Teriyaki"
    },
    {
        "date": "2020-11-06",
        "item": "B:Pizza Sticks"
    },
    {
        "date": "2020-11-09",
        "item": "A:Maple Glazed French Toast Sticks"
    },
    {
        "date": "2020-11-10",
        "item": "B:Hamburger or Cheeseburger on a Bun"
    },
    {
        "date": "2020-11-12",
        "item": "A:Chicken Nuggets"
    },
    {
        "date": "2020-11-13",
        "item": "B:Pizza Cheese Crunchers"
    },
    {
        "date": "2020-11-16",
        "item": "A:Barbeque Rib Sandwich"
    },
    {
        "date": "2020-11-17",
        "item": "B:Turkey Nachos Grande"
    },
    {
        "date": "2020-11-18",
        "item": "A:Meatball Hero"
    },
    {
        "date": "2020-11-19",
        "item": "B:Popcorn Chicken"
    },
    {
        "date": "2020-11-20",
        "item": "A:Pizza Slice"
    },
    {
        "date": "2020-11-23",
        "item": "B:Chicken Patty on a Bun"
    },
    {
        "date": "2020-11-24",
        "item": "A:NO LUNCH SERVICE EARLY DISMISSAL"
    },
    {
        "date": "2020-11-30",
        "item": "B:Grilled Cheese Sandwich"
    }
]