import os
from py_console import console

console.info("\nProgram initialized...\n")

print("1) Build application\n2) Create a new template\n3) Generate output\n")


def buildApplication():

    # Making folders and files

    os.makedirs("Emails")
    os.makedirs("templates")
    templatesFile = open("templates.txt", "w").close()

    console.info(
        "Made Emails, templates, and templatesFile.txt. Application made")


while True:

    optionSelected = int(input("Kindly enter the option: "))

    if optionSelected == 1:

        buildApplication()

    elif optionSelected == 2:

        templateName = input("\nKindly enter the name of template: ")
        templateName = templateName.replace(" ", "-")

        print("\n")

        htmlBoilerPlate = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="templates\Document\Document.css">
</head>
<body>
    
</body>
</html>"""

        # Making file name appear in the boilerplate
        htmlBoilerPlate = htmlBoilerPlate.replace("Document", templateName)

        # Making directories and html, scss files

        os.makedirs('templates/{}'.format(templateName))
        console.info("Directory {} made.".format(templateName))
        file = open("templates/{0}/{0}.html".format(templateName), "w")
        file.write(htmlBoilerPlate)
        file.close()
        console.info("Made templates/{0}/{0}.html".format(templateName))
        file = open("templates/{0}/{0}.scss".format(templateName), "w").close()
        console.info("Made templates/{0}/{0}.scss".format(templateName))

        file = open("templates.txt", "a")
        file.write("{}, ".format(templateName))
        file.close()
        console.info("Registered this template\n")

        console.success("Successfully made the template\n")
