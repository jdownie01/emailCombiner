import os
import subprocess

rootdir = '/home/jwd2488/GiveToBob/ProvideForGJ/stephen@idd-usa.com/Inbox_20210206-1658/messages'
extensions = '.pdf'
commands = []
attachment_directories = os.listdir("/home/jwd2488/Downloads/BZIP/BZIP/")


for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        ext = os.path.splitext(file)[-1].lower()
        if ext in extensions:
            base = os.path.basename(file)
            filename = os.path.splitext(base)[0]
            toAppend = []
            print(filename)
            try:
                command = ["pdfunite",
                           "/home/jwd2488/GiveToBob/ProvideForGJ/stephen@idd-usa.com/Inbox_20210206-1658/messages/" +
                           os.path.splitext(file)[0] + ".pdf"]
                for directory in attachment_directories:
                    if directory.split("-attachments")[0] == filename:
                        for files1 in os.walk("/home/jwd2488/Downloads/BZIP/BZIP/" + directory.replace(" ","\\ ")):
                            for file1 in files1:
                                if file1:
                                    if file1[0] != '/':
                                        for f in file1:
                                            command.append(
                                                "/home/jwd2488/Downloads/BZIP/BZIP/" + directory + "/" + (os.path.splitext(f)[0]) + ".pdf")

                if len(command) == 2:
                    raise Exception
                command.append(filename + ".pdf")
                commands.append(command)
            except Exception as e:
                print(e)
                print("not found")
                command = ["cp",
                           "/home/jwd2488/GiveToBob/ProvideForGJ/stephen@idd-usa.com/Inbox_20210206-1658/messages/" +
                           os.path.splitext(file)[0] + ".pdf", filename + ".pdf"]
                commands.append(command)




for command in commands:
    print(command)
    subprocess.run(command)

print(commands)