

string = """<!DOCTYPE html><html lang="en">
    <head><meta charset="UTF-8"><title>Shira'Google</title></head>
    <body><a href=""" + value + """>""" + key + """<br /></a></body></html>"""
    with open("shira's_google.html", "a") as Html_file:
        Html_file.write(string)