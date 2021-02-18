def asHtmlList(func):
    def innerFunc():
        htmlString = "<ul>"
        for item in func():
            htmlString += f"<li>{item}</li>"
        htmlString += "</ul>"
        return htmlString
    globals()[func.__name__ + "AsHtml"] = innerFunc
    return func

def log(func):
    def logger():
        print(f"Calling {func.__name__} -->")
        func()
        print(f"The function {func.__name__} is done.")
    return logger

@log
def doSomething():
    print("Doing something")
    
#> Calling doSomething -->
#> Doing something
#> The function doSomething is done.


@asHtmlList
def getList23():    
    return [2,3]

@asHtmlList
def getList1234():    
    return [1,2,3,4]


for item in getList23():
    print(item)
# prints:
#> 2
#> 3

for item in getList1234():
    print(item)
# prints:
#> 1
#> 2
#> 3
#> 4

print(getList23AsHtml())
# prints:
#> <ul><li>2</li><li>3</li></ul>

print(getList1234AsHtml())
# prints:
#> <ul><li>1</li><li>2</li><li>3</li><li>4</li></ul>

doSomething()
