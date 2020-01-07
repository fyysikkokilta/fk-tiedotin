# FK-tiedotin 2020
Tool for making a structured weekly bulletin for the Guild of Physics. Forked from [summila](https://github.com/summis/fk-tiedotin). Information about events are fed to the GUI (information includes header, date, category of event and date) and they are saved to a database. Formatted HTML-file is created from database entries that can be used in emails and websites.

Tool is still under construction.

## Installation
Clone the repository.

### Dependecies
FK-tiedotin is written in **Python 3** and uses following libraries: PyQt5, TinyDB, Jinja2.
These can be installed with

`pip3 install pyqt5 tinydb Jinja2`

## Usage
Open GUI to add entries to database:

`python gui.py`

Create bulletin from database entries:

`python bulletin.py`

Entries are saved with JSON in data-folder and ready emails are saved in mails-folder. For every week new database and a new mail are created.


## Screenshots
<p float="left">
  <img alt="GUI" src="https://i.imgur.com/l9mBWeR.png" width="auto"><img alt="Bulletin" src="https://i.imgur.com/anv5eMQ.png" width="375px">
</p>


## Remarks

* ``bulletin.py`` contains editable text variables for title and footer
* HTML used in the email must be written in a style that it looks similar in (almost) all email clients.
