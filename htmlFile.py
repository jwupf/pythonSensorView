def getHtmlPage():
    return "<!DOCTYPE html>" + "<html>" + "</html>"


def asHtmlList(func):
    def innerFunc():
        htmlString = "<ul>"
        for item in func():
            htmlString += f"<li>{item}</li>"
        htmlString += "</ul>"
        return htmlString
    globals()[func.__name__ + "AsHtml"] = innerFunc
    return func


@asHtmlList
def getList():    
    return [2,3]

def getValue():
    return 3