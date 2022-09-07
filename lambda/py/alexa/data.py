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
LUNCHMENU = "September2022"
LUNCHMENU_DATA_ELEMENTARY = [
    {
        "date": "2022-09-01",
        "item": "Hamburger or Cheeseburger"
    },
    {
        "date": "2022-09-06",
        "item": "Cinnamon French Toast Sticks"
    },
    {
        "date": "2022-09-07",
        "item": "Pasta Day. Plain pasta with butter or meatballs and marinara sauce."
    },
    {
        "date": "2022-09-08",
        "item": "Turkey Nachos Grande"
    },
    {
        "date": "2022-09-09",
        "item": "Cheese or Pepperoni Pizza"
    },
    {
        "date": "2022-09-12",
        "item": "Breaded Chicken Tenders"
    },
    {
        "date": "2022-09-13",
        "item": "Pancakes with Syrup"
    },
    {
        "date": "2022-09-14",
        "item": "Hot Dog or Hamburger"
    },
    {
        "date": "2022-09-15",
        "item": "Macaroni and Cheese"
    },
    {
        "date": "2022-09-16",
        "item": "Cheese or Pepperoni Pizza"
    },
    {
        "date": "2022-09-19",
        "item": "Breaded Chicken Bites"
    },
    {
        "date": "2022-09-20",
        "item": "Cinnamon French Toast Sticks"
    },
    {
        "date": "2022-09-21",
        "item": "Cheesy Stuffed Breadsticks with Marinara Sauce"
    },
    {
        "date": "2022-09-22",
        "item": "Turkey Nachos Grande"
    },
    {
        "date": "2022-09-23",
        "item": "Cheese or Pepperoni Pizza"
    },
    {
        "date": "2022-09-28",
        "item": "Chicken Tenders and Waffles with Syrup"
    },
    {
        "date": "2022-09-29",
        "item": "Baked Mozarella Sticks"
    },
    {
        "date": "2022-09-30",
        "item": "Cheese or Pepperoni Pizza"
    }
]
LUNCHMENU_DATA_MIDDLESCHOOL = [
    {
        "date": "2022-09-01",
        "item": "Bacon Cheeseburger"
    },
    {
        "date": "2022-09-06",
        "item": "Cinnamon French Toast Sticks"
    },
    {
        "date": "2022-09-07",
        "item": "Pasta Day. Plain pasta with butter or meatballs and marinara sauce."
    },
    {
        "date": "2022-09-08",
        "item": "Turkey Nachos Grande"
    },
    {
        "date": "2022-09-09",
        "item": "Italian Sausage and Peppers Hero"
    },
    {
        "date": "2022-09-12",
        "item": "Breaded Chicken Tenders"
    },
    {
        "date": "2022-09-13",
        "item": "Chili or Buffalo Chicken"
    },
    {
        "date": "2022-09-14",
        "item": "Grilled Chicken Sandwich"
    },
    {
        "date": "2022-09-15",
        "item": "Beef or Bean Burrito"
    },
    {
        "date": "2022-09-16",
        "item": "Spinach Meatball and Cheese Stromboli or Calzone"
    },
    {
        "date": "2022-09-19",
        "item": "Baked Ziti with Meat Sauce"
    },
    {
        "date": "2022-09-20",
        "item": "Barbequeue Pulled Pork on a Bun"
    },
    {
        "date": "2022-09-21",
        "item": "Chicken Parmesan Sandwich"
    },
    {
        "date": "2022-09-22",
        "item": "Turkey Nachos Grande"
    },
    {
        "date": "2022-09-23",
        "item": "Cheesy Stuffed Breaksticks"
    },
    {
        "date": "2022-09-28",
        "item": "General Tso's Chicken"
    },
    {
        "date": "2022-09-29",
        "item": "Chicken Tenders and Waffles with Syrup"
    },
    {
        "date": "2022-09-30",
        "item": "Meatball Hero"
    }
]
