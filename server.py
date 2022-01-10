# Os for running cmd commands
import os
# For colorful printing
from py_console import console
# Threading to perform multi-tasking
import threading
# Time to pause the execution for some seconds
import time
# For converting all css into inline. Only then emails will get styled
import css_inline

# Getting names of all templates
templateList = open("templates.txt").read().split(", ")[:-1]

counter = 0

for i in templateList:

    print(counter, ") ", i)
    counter += 1

templateSelected = templateList[int(input("\nKindly select the template: "))]

print("\n")

console.info("Starting the server for {}...".format(templateSelected))

# Function to start transpilation of Sass files to CSS
def processSassFiles():

    os.system(
        r"sass --watch templates\{0}\{0}.scss templates\{0}\{0}.css".format(templateSelected))

# Function to convert all html css to output mail.
def HTMLFileChangedFunction():

    print("Changing the output html file")

    htmlFileContent = open(
        "templates\{0}\{0}.html".format(templateSelected)).read()

    console.info("Making ", "./Emails/{}Output.html".format(templateSelected))
    outputFile = open("./Emails/{}Output.html".format(templateSelected), "w")
    console.info("Trying to write in the output file")

    # Exception may occur if the .css file did not generate. In that case let it sleep for just 2 sec, and the sass compiler would've generated the css file
    try:
        outputFile.write(css_inline.inline(htmlFileContent))
        outputFile.close()
    except Exception:
        time.sleep(2)
        outputFile.write(css_inline.inline(htmlFileContent))
        outputFile.close()

    console.info("Output file {}.html file updated".format(templateSelected))

    # Sleep for 2 seconds, and rerun the function to update the output
    time.sleep(2)
    HTMLFileChangedFunction()

# Making threads to perform multi-tasking

# Thread to process Sass files
sassFileThread = threading.Thread(target=processSassFiles)
sassFileThread.start()

# Thread to update output file
generateOutput = threading.Thread(target=HTMLFileChangedFunction)
generateOutput.start()
