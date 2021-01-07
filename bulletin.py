#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import partial
from jinja2 import Environment, FileSystemLoader, Markup
from utils import grouper, category_sort, categories, categories_en, week, all_entries


# Define template behaviour.
env = Environment(
    loader=FileSystemLoader('templates'),
    trim_blocks=True,
    lstrip_blocks=True,
    )


def nl2br(s):
    """Change linebreaks to <br /> tags."""
    return s.replace('\n', Markup('<br/>\n'))

env.filters['nl2br'] = nl2br    # Add function to env's filters.


# Sort first by category to enable grouping.
entries = all_entries(isEnglish=False)
entries_en = all_entries(isEnglish=True)
entries = sorted(entries, key=partial(category_sort, cats=categories))
entries_en = sorted(entries_en, key=partial(category_sort, cats=categories_en))


# Group entries.
pairs = grouper(entries, categories)
pairs_en = grouper(entries_en, categories_en)


template = env.get_template('cells.html')
template_en = env.get_template('cells_en.html')
template_short = env.get_template('cells_short.html')
variables = {
    "title": "Fyysikkokillan viikkotiedote",
    "header": week+"/2020\n"+"Kilta tiedottaa\nGuild News",
    "category_events": pairs,
    "category_events_en": pairs_en,
    "communications_officer": "Niko Savola",
    "telegram_nick": "viestintavastaava",
    "email": "viestintavastaava@fyysikkokilta.fi",
    "week": week
    }

tiedote = template.render(variables)
tiedote_en = template_en.render(variables)
tiedote_short = template_short.render(variables)

with open('mails/kilta-tiedottaa-viikko-'+week+'.html', 'w', encoding='utf-8') as f:
    f.write(tiedote)

with open('mails/kilta-tiedottaa-viikko-'+week+'-en.html', 'w', encoding='utf-8') as f:
    f.write(tiedote_en)

with open('mails/kilta-tiedottaa-viikko-'+week+'-short.html', 'w', encoding='utf-8') as f:
    f.write(tiedote_short)

print("Bulletin made succesfully.")
