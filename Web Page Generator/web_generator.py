import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        # Label
        self.label = Label(self.master, text="Enter custom text or click the Default HTML page button", font=10)
        self.label.grid(padx=(5, 5), pady=(10, 5))

        #Entry
        self.entry = Entry(self.master, width=100)
        self.entry.grid(padx=(5, 10), pady=(10, 5), columnspan=2)

        # "Default HTML Page" button
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(pady=(10,10), row=2, column=0)

        #"Submit Custom Text" button
        self.btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customText)
        self.btn.grid(pady =(10,10), row=2, column=1)

    # creates an HTML document
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    # Creates HTML with user's input

    def customText(self):
        htmlText = self.entry.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")







if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()