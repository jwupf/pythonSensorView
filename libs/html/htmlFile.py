
def getHtmlHeader(title = "&nspb"):
    head = "<head>"
    head += "<title>"
    head += title # title ought to be non empty
    head += "</title>"
    head += "</head>"
    return head

def getHtmlPage(title = "&nspb"):
    html = "<!DOCTYPE html>"
    html += "<html>"
    html += getHtmlHeader(title)
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
