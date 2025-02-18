#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import partial

from jinja2 import Environment, FileSystemLoader
from markupsafe import Markup

from utils import (
    grouper,
    category_sort,
    categories,
    categories_en,
    week,
    year,
    all_entries,
)


# Define template behaviour.
env = Environment(
    loader=FileSystemLoader("templates"),
    trim_blocks=True,
    lstrip_blocks=True,
)


def nl2br(s):
    """Change linebreaks to <br /> tags."""
    return s.replace("\n", Markup("<br/>\n"))


env.filters["nl2br"] = nl2br  # Add function to env's filters.


# Sort first by category to enable grouping.
entries = all_entries(isEnglish=False)
entries_en = all_entries(isEnglish=True)
entries = sorted(entries, key=partial(category_sort, cats=categories))
entries_en = sorted(entries_en, key=partial(category_sort, cats=categories_en))


# Group entries.
pairs = grouper(entries, categories)
pairs_en = grouper(entries_en, categories_en)


template = env.get_template("cells.html")
template_en = env.get_template("cells_en.html")
template_short = env.get_template("cells_short.html")
template_short_en = env.get_template("cells_short_en.html")
variables = {
    "title": "Fyysikkokillan viikkotiedote",
    "title_en": "Guild of Physics Weekly News",
    "short_title": f"Kilta tiedottaa {week}/{year}",
    "short_title_en": f"Guild News {week}/{year}",
    "header": week + "/2023\n" + "Kilta tiedottaa\nGuild News",
    "category_events": pairs,
    "category_events_en": pairs_en,
    "communications_officer": "Iris Kause",
    "telegram_nick": "viestintavastaava",
    "email": "viestintavastaava@fyysikkokilta.fi",
    "week": week,
}

tiedote = template.render(variables)
tiedote_en = template_en.render(variables)
tiedote_short = template_short.render(variables)
tiedote_short_en = template_short_en.render(variables)

with open("mails/kilta-tiedottaa-viikko-" + week + ".html", "w", encoding="utf-8") as f:
    f.write(tiedote)

with open(
    "mails/kilta-tiedottaa-viikko-" + week + "-en.html", "w", encoding="utf-8"
) as f:
    f.write(tiedote_en)

with open(
    "mails/kilta-tiedottaa-viikko-" + week + "-short.html", "w", encoding="utf-8"
) as f:
    f.write(tiedote_short)

with open(
    "mails/kilta-tiedottaa-viikko-" + week + "-short-en.html", "w", encoding="utf-8"
) as f:
    f.write(tiedote_short_en)

print("Bulletin made succesfully.")
