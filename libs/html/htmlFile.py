def getHtmlHeader(title="&nspb"):
    head = "<head>"
    head += "<title>"
    head += title  # title ought to be non empty
    head += "</title>"
    head += "</head>"
    return head


def getHtmlBody(document):
    body = "<body>"
    for chapter in document.Chapters:
        body += f"<h1>{chapter.Title}</h1>"
        for text in chapter.Text:
            body += text
    body += "</body>"
    return body


def getHtmlPage(document):
    html = "<!DOCTYPE html>"
    html += "<html>"
    html += getHtmlHeader(document.Title)
    html += getHtmlBody(document)
    html += "</html>"
    return html
