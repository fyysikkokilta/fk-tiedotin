from database import entriesFromCategory, week
from string import Template
from datetime import date, timedelta

with open("kilta-tiedottaa-template.html", 'r') as f:
    txt = f.read()
template = Template(txt)


first_paragraph = ""
table_of_contents = ""
contents = ""
first_paragraph_en = ""
table_of_contents_en = ""
contents_en = ""


# TODO
# - sort entries by date
# - english version
# - some smart way to make first paragraph
# - maybe categories could be defined only in one place instead of two


categories = ["Killan tapahtumat", "AYY ja Aalto", "Yleistä"]
# index for unique id:s to create links
idx = 1
for category in categories:
    entries = entriesFromCategory(category)
    if entries:
        table_of_contents += f"""<tr> 
            <td style="color: #201E1E; font-family: Calibri; font-size: 24px;">
            <b>{category}</b> 
            </td>
            </tr>\n"""

        table_of_contents += """<tr>
            <td style="padding: 10px 0px 15px 0px; font-family: Calibri; font-size: 16px;">
            <ul style=" margin: 0;">\n"""

        for entry in entries:
            table_of_contents += f"<li><a href='#id{idx}'>{entry['header']}</a></li>\n"
            # replace linebreaks with corresponding html code
            formattedContent = entry['content'].replace("\n", "<br/>")
            contents += f"""<tr>
                <td id='id{idx}' style="padding: 10px 0px 15px 0px; font-family: Calibri; font-size: 16px;">
                <b>{entry['header']}</b><br/>
                {formattedContent}
                </td>
                </tr>\n"""
            idx += 1

        table_of_contents += "</ul>\n</td>\n</tr>\n"


d = {
        'WEEK': week,
        'FIRST_PARAGRAPH': first_paragraph,
        'TABLE_OF_CONTENTS': table_of_contents,
        'CONTENTS': contents,
        'FIRST_PARAGRAPH_EN': first_paragraph_en,
        'TABLE_OF_CONTENTS_EN': table_of_contents_en,
        'CONTENTS_EN': contents_en
        }
newsLetter = template.substitute(d)


with open(f'mails/kilta-tiedottaa-viikko-{week}.html', 'w') as f:
    f.write(newsLetter)

print(newsLetter)
