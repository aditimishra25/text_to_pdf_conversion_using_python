
#Python program to create a pdf file
from fpdf import FPDF

#save FPDF() class into a variable pdf
pdf=FPDF()

#Add a page
pdf.add_page()

#set style and size of font that we want in pdf
pdf.set_font("Arial",size=18)

#create a cell
pdf.cell(200,10,txt="A file with the .pdf file extension is a Portable Document Format (PDF) file",ln=1,align='c')

#create another cell
pdf.cell(200,10,txt="PDFs are typically used to distribute read-only documents that preserve the layout of a page ",ln=2,align='c')

#create another cell
pdf.cell(200,10,txt="They’re commonly used for documents like user manuals, eBooks, application forms, and scanned documents," 
"to name just a few.",ln=2,align='c')

#create another cell
pdf.cell(200,10,txt="PDF was created by Adobe in the 1990s to achieve two things.",ln=2,align='c')

#create another cell
pdf.cell(200,10,txt="The first is that people should be able to open the documents on any hardware or operating system,"
"without needing to have the app used to create them—all you need is a PDF reader,"
                    "and these days most web browsers fit the bill",ln=2,align='c')

#create another cell
pdf.cell(200,10,txt="The second is that wherever you open a PDF, the layout of the document should look the same.",ln=2,align='c')

#create another cell
pdf.cell(200,10,txt="PDFs can contain text, images, embedded fonts, hyperlinks, video, interactive buttons, forms, and more. ",ln=2,align='c')

#save the pdf with name.pdf
pdf.output("mypdf2.pdf")