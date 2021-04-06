from docxtpl import DocxTemplate

import json

doc = DocxTemplate("EuropassCV-Template.docx")

with open('assets/config.json', "r") as f:
    data = json.load(f)

doc.render(data)
doc.replace_pic('Image1', 'assets/pic.jpg')

doc.save("EuropassCV.docx")


def parse_placeholders(to_parse):
    for p_id in data:
        if f"%{p_id}%" in to_parse:
            if type(data[p_id]) == str:
                to_parse = to_parse.replace(f"%{p_id}%", data[p_id])
            elif type(data[p_id]) == list:
                to_parse = to_parse.replace(f"%{p_id}%", "\n".join(data[p_id]))
    return to_parse
