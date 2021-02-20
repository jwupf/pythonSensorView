def getHtmlPage():
    html = ""
    html += "<!DOCTYPE html>"
    html += "<html>"
    html += "<head>"
    html += "<title>"
    html += "&nspb" # title ought to be non empty
    html += "</title>"
    html += "</head>"
    html += "<body>"
    html += "</body>"
    html += "</html>"
    return html


def asHtmlList(func):
    def innerFunc():
        htmlString = "<ul>"
        for item in func():
            htmlString += f"<li>{item}</li>"
        htmlString += "</ul>"
        return htmlString
    globals()[func.__name__ + "AsHtml"] = innerFunc
    return func
