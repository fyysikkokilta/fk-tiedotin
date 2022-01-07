# FK-tiedotin 2020
Tool for making a structured weekly bulletin for the Guild of Physics. Forked from [summila](https://github.com/summis/fk-tiedotin). Information about events are fed to the GUI (information includes header, date, category of event and date) and they are saved to a database. Formatted HTML-file is created from database entries that can be used in emails and websites.

## Installation

First, clone the repository.

Use [Git Bash](https://gitforwindows.org/) on Windows. Any other shell on any other OS should be fine.

### Dependencies
FK-tiedotin is written in **Python 3** and uses following libraries: PyQt5, TinyDB, Jinja2.
These can be installed with

```bash
pip install -r requirements.txt
```

## Usage
Open GUI to add entries to database:

```bash
python gui.py
```

Create bulletin from database entries:

```bash
python bulletin.py
```

Entries are saved as JSON in the data-folder and finished emails are saved in the mails-folder. A new database and a new email are created for every week.

### Uploading `.json` for Fyysikkokilta website

To upload the correct weekly `.json` to the Fyysikkokilta website for the [corresponding Telegram bot](https://github.com/fyysikkokilta/fk-viikkotiedotebot) to work, set up permissions to `ssh` to `fk@otax.fi` and simply run
```bash
upload-to-otax.sh
```

**Windows users NB:** In order to support *special characters*, start the programs with the argument `python -X utf8` or set the environment variable `set PYTHONUTF8=1`.


## Screenshots
<p float="left">
  <img alt="GUI" src="https://i.imgur.com/l9mBWeR.png" width="auto"><img alt="Bulletin" src="https://i.imgur.com/anv5eMQ.png" width="375px">
</p>

## Remarks

* ``bulletin.py`` contains editable text variables for title and footer
* HTML used in the email must be written in a style that it looks similar in (almost) all email clients.


## To improve

* Add HTML bulletins to Guild website and maybe info about it with Kiltisbot
* Most URLs are followed by newline which is stored as \n and ``urlize`` treats it as part of the URL
* (maybe) Add support for _Opintovastaavan palsta_
