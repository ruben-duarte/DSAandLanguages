import PyPDF2

#A relative path in Python is a path that describes the location of a directory relative to the entry point where you run the Python script.
with open('agenda.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    #print(len(reader.pages))
    page = reader.pages[0]
    page.rotate(90)
    writer = PyPDF2.PdfWriter()
    writer.add_page(page)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)



