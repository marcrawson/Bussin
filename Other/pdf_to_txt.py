import PyPDF2 # works with version 3.0.0+

input_pdf  = "schedule.pdf" # "26_UVIC_Weekday_Schedule.pdf"
output_txt = "schedule.txt" # "26_UVIC_Weekday_Schedule.txt"

def main():
    with open(input_pdf, "rb") as pdf_file:           # open pdf file in read-binary mode

        pdf_reader = PyPDF2.PdfReader(pdf_file)       # create pdf reader object

        num_pages = len(pdf_reader.pages)             # get number of pages in the pdf

        with open(output_txt, "w") as txt_file:       # open txt file for writing
            
            for page_num in range(num_pages):         # loop through all pages and extract text
                
                page_obj = pdf_reader.pages[page_num] # get current page object
                
                text = page_obj.extract_text()        # extract text from the page object
                
                txt_file.write(text)                  # write the text to the text file

if __name__ == "__main__":
    main()