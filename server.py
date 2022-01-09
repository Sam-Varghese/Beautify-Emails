import os
from py_console import console
import threading
import time
import css_inline

templateList = open("templates.txt").read().split(", ")[:-1]

counter = 0

for i in templateList:

    print(counter, ") ", i)
    counter += 1

templateSelected = templateList[int(input("\nKindly select the template: "))]

print("\n")

console.info("Starting the server for {}...".format(templateSelected))


def processSassFiles():

    os.system(
        r"sass --watch templates\{0}\{0}.scss templates\{0}\{0}.css".format(templateSelected))


def HTMLFileChangedFunction():

    print("Changing the output html file")

    htmlFileContent = open(
        "templates\{0}\{0}.html".format(templateSelected)).read()

    console.info("Making ", "./Emails/{}Output.html".format(templateSelected))
    outputFile = open("./Emails/{}Output.html".format(templateSelected), "w")
    console.info("Trying to write in the output file")

    try:
        outputFile.write(css_inline.inline(htmlFileContent))
        outputFile.close()
    except Exception:
        time.sleep(2)
        outputFile.write(css_inline.inline(htmlFileContent))
        outputFile.close()

    console.info("Output file {}.html file updated".format(templateSelected))


def watchOverHTMLFile(initialContent=""):

    fileName = "templates\{0}\{0}.html".format(templateSelected)

    newContentFile = open("templates\{0}\{0}.html".format(templateSelected))
    newContent = newContentFile.read()
    newContentFile.close()

    HTMLFileChangedFunction()
    time.sleep(3)
    watchOverHTMLFile(initialContent=newContent)


sassFileThread = threading.Thread(target=processSassFiles)
sassFileThread.start()

generateOutput = threading.Thread(target=watchOverHTMLFile)
generateOutput.start()
