# SCOTUSBLOG GUI
# Written by: JoshTheEngineer
# Started: 08/11/17
# Updated: 08/11/17 - Started code
#                   - Works as intended so far
#          08/12/17 - Adding scroll bars
#                   - Adding counter for number of briefs
#                   - Adding links for appropriate values

import bs4 as bs                        # To parse the webpages
import urllib                           # To open the webpage
import urllib.request                   # To open the webpage
import webbrowser                       # To open up webpages

try:
    from tkinter import *               # Try to import Python 3.x
except ImportError:
    from Tkinter import *               # If it fails, import Python 2.x

class Application(Frame):

    # ==============================
    # ===== INITIALIZE THE GUI =====
    # ==============================
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()

        # :: Create the soup
        self.sauce = urllib.request.urlopen('http://www.scotusblog.com/case-files/terms/').read()                       # Get the webpage
        self.soup = bs.BeautifulSoup(self.sauce,'lxml')                                                                 # Create the soup for use in other methods

        # :: Create all the widgets
        self.create_widgets()                                                                                           # Create all the widgets in the GUI

    # ==============================
    # ===== CREATE THE WIDGETS =====
    # ==============================
    def create_widgets(self):

        self.titleTermCase = Label(self,text='SELECT TERM AND CASE',bg='black',fg='white')                              # Create the label widget for the term/case title
        self.titleTermCase.grid(row=0, column=0, columnspan=4, sticky=W + E)                                            # Place the widget in the GUI

        numRowsLists = 10                                                                                               # Number of rows in the Term and Case lists

        # ===== SELECT THE TERM =====
        self.scrollListTerms = Scrollbar(self,orient='vertical')                                                        # Create a scrollbar widget for the Terms list
        self.listTerms = Listbox(self,yscrollcommand=self.scrollListTerms.set)                                          # Create a listbox widget for the Terms list
        self.scrollListTerms.config(command=self.listTerms.yview)                                                       # Configure the scrollbar for y-scrolling(?)
        self.scrollListTerms.grid(row=1,column=1,rowspan=numRowsLists,sticky=N+S)                                       # Place the scrollbar next to the listbox
        self.listTerms.grid(row=1,column=0,rowspan=numRowsLists,sticky=N+S)                                             # Place the listbox to the left of the scrollbar
        self.populateTerms()                                                                                            # Call method to populate the Terms list

        self.pushSelect = Button(self,text='Select Term',command=self.pushSelectTerm_CB)                                # Button to select a term
        self.pushSelect.grid(row=numRowsLists+2,column=0,columnspan=2,sticky=W+E)                                       # Put the Button in the GUI

        # ===== CASES IN THE SELECTED TERM =====
        self.scrollListCases = Scrollbar(self,orient='vertical')
        self.listCases = Listbox(self,yscrollcommand=self.scrollListCases.set)
        self.scrollListCases.config(command=self.listCases.yview)
        self.scrollListCases.grid(row=1,column=3,rowspan=numRowsLists,sticky=N+S)
        self.listCases.grid(row=1,column=2,rowspan=numRowsLists,sticky=N+S)

        self.pushSelectCase = Button(self,text='Select Case',command=self.pushSelectCase_CB)
        self.pushSelectCase.grid(row=numRowsLists+2,column=2,columnspan=2,sticky=W+E)

        self.listCases.bind('<Double-Button-1>', self.openCasePage_CB)                          # ///////// BINDING //////////

        # ===== BLOG POSTS =====
        self.titleBlogs = Label(self, text='BLOG POSTS',bg='black',fg='white')                                          # Create Label width for title of Blogs section
        self.titleBlogs.grid(row=numRowsLists+3,column=0,columnspan=9,sticky=W+E)                                       # Place in the GUI

        self.scrollBlogs = Scrollbar(self,orient='vertical')
        self.listBlogs = Listbox(self,yscrollcommand=self.scrollBlogs.set)
        self.scrollBlogs.config(command=self.listBlogs.yview)
        self.scrollBlogs.grid(row=numRowsLists+4,column=8,sticky=N+S+W)
        self.listBlogs.grid(row=numRowsLists+4,column=0,columnspan=8,sticky=W+E)

        # ===== DOCKET INFO =====
        dateDocketTitleCol = 4
        dateDocketTextCol  = dateDocketTitleCol + 1

        self.titleDocket = Label(self, text='DOCKET INFO', bg='black', fg='white')                                      # Create Label widget for the docket information title
        self.titleDocket.grid(row=0,column=dateDocketTitleCol,columnspan=2,sticky=W+E,padx=5)                           # Place in the GUI

        self.titleDocketNo = Label(self,text='Docket No.').grid(row=1,column=dateDocketTitleCol)                        # Create Label widget for Docket No. name, and place in GUI
        self.titleOpBelow  = Label(self,text='Op. Below').grid(row=2,column=dateDocketTitleCol)                         # Create Label widget for Op. Below name, and place in GUI
        self.titleArgument = Label(self,text='Argument').grid(row=3,column=dateDocketTitleCol)                          # Create Label widget for Argument name, and place in GUI
        self.titleOpinion  = Label(self,text='Opinion').grid(row=4,column=dateDocketTitleCol)                           # Create Label widget for Opinion name, and place in GUI
        self.titleVote     = Label(self,text='Vote').grid(row=5,column=dateDocketTitleCol)                              # Create Label widget for Vote name, and place in GUI
        self.titleAuthor   = Label(self,text='Author').grid(row=6,column=dateDocketTitleCol)                            # Create Label widget for Author name, and place in GUI
        self.titleTerm     = Label(self,text='Term').grid(row=7,column=dateDocketTitleCol)                              # Create Label widget for Term name, and place in GUI

        self.textDocketNo = Label(self,text='\t\t',bg='white')                                                          # Create Label widget for Docket No. result
        self.textDocketNo.grid(row=1, column=dateDocketTextCol, sticky=W + E, padx=5)                                   # Place in the GUI
        self.textOpBelow  = Label(self,text='\t\t',bg='white')                                                          # Create Label widget for Op. Below result
        self.textOpBelow.grid(row=2, column=dateDocketTextCol, sticky=W + E, padx=5)                                    # Place in the GUI
        self.textArgument = Label(self,text='\t\t',bg='white')                                                          # Create Label widget for Argument result
        self.textArgument.grid(row=3, column=dateDocketTextCol, sticky=W + E, padx=5)                                   # Place in the GUI
        self.textOpinion  = Label(self,text='\t\t',bg='white')                                                          # Create Label widget for Opinion result
        self.textOpinion.grid(row=4, column=dateDocketTextCol, sticky=W + E, padx=5)                                    # Place in the GUI
        self.textVote     = Label(self,text='\t\t',bg='white')                                                          # Create Label widget for Vote result
        self.textVote.grid(row=5, column=dateDocketTextCol, sticky=W + E, padx=5)                                       # Place in the GUI
        self.textAuthor   = Label(self,text='\t\t',bg='white')                                                          # Create Label widget for Author result
        self.textAuthor.grid(row=6, column=dateDocketTextCol, sticky=W + E, padx=5)                                     # Place in the GUI
        self.textTerm     = Label(self,text='\t\t',bg='white')                                                          # Create Label widget for Term result
        self.textTerm.grid(row=7,column=dateDocketTextCol,sticky=W+E,padx=5)                                            # Place in the GUI

        # ===== BRIEFS =====
        briefCol = dateDocketTextCol + 1
        self.titleBrief      = Label(self,text='BRIEFS',bg='black',fg='white')
        self.titleBrief.grid(row=0,column=briefCol,columnspan=2,sticky=W+E,padx=5)

        self.textBriefWhite  = Label(self,text='White',bg='white').grid(row=1,column=briefCol,sticky=W+E,padx=5)
        self.textBriefOrange = Label(self,text='Orange',bg='dark orange').grid(row=2,column=briefCol,sticky=W+E,padx=5)
        self.textBriefTan    = Label(self,text='Tan',bg='tan').grid(row=3,column=briefCol,sticky=W+E,padx=5)
        self.textBriefLBlue  = Label(self,text='Light Blue',bg='cyan').grid(row=4,column=briefCol,sticky=W+E,padx=5)
        self.textBriefLRed   = Label(self,text='Light Red',bg='IndianRed1').grid(row=5,column=briefCol,sticky=W+E,padx=5)
        self.textBriefCream  = Label(self,text='Cream',bg='khaki1').grid(row=6,column=briefCol,sticky=W+E,padx=5)
        self.textBriefLGreen = Label(self,text='Light Green',bg='PaleGreen2').grid(row=7,column=briefCol,sticky=W+E,padx=5)
        self.textBriefDGreen = Label(self,text='Dark Green',bg='forest green').grid(row=8,column=briefCol,sticky=W+E,padx=5)
        self.textBriefGray   = Label(self,text='Gray',bg='gray').grid(row=9,column=briefCol,sticky=W+E,padx=5)

        self.numBriefWhite  = Label(self,text='\t\t',bg='white')
        self.numBriefWhite.grid(row=1,column=briefCol+1,sticky=W+E,padx=5)
        self.numBriefOrange = Label(self,text='\t\t',bg='white')
        self.numBriefOrange.grid(row=2,column=briefCol+1,sticky=W+E,padx=5)
        self.numBriefTan    = Label(self,text='\t\t',bg='white')
        self.numBriefTan.grid(row=3,column=briefCol+1,sticky=W+E,padx=5)
        self.numBriefLBlue  = Label(self,text='\t\t',bg='white')
        self.numBriefLBlue.grid(row=4,column=briefCol+1,sticky=W+E,padx=5)
        self.numBriefLRed   = Label(self,text='\t\t',bg='white')
        self.numBriefLRed.grid(row=5,column=briefCol+1,sticky=W+E,padx=5)
        self.numBriefCream  = Label(self,text='\t\t',bg='white')
        self.numBriefCream.grid(row=6,column=briefCol+1,sticky=W+E,padx=5)
        self.numBriefLGreen = Label(self,text='\t\t',bg='white')
        self.numBriefLGreen.grid(row=7,column=briefCol+1,sticky=W+E,padx=5)
        self.numBriefDGreen = Label(self,text='\t\t',bg='white')
        self.numBriefDGreen.grid(row=8,column=briefCol+1,sticky=W+E,padx=5)
        self.numBriefGray   = Label(self,text='\t\t',bg='white')
        self.numBriefGray.grid(row=9,column=briefCol+1,sticky=W+E,padx=5)

    # =======================================================
    # ===== METHOD: Populate the Listbox on GUI startup =====
    # =======================================================
    def populateTerms(self):
        listOfLists = []                                                                                                # Initialize a list
        for li in self.soup.select('div.post li'):                                                                      # For each list item
            listOfLists.append(li.text)                                                                                 # Append the term to the list

        self.listTerms.insert('end',*listOfLists)                                                                       # Populate the Listbox with our list
        self.listTerms.select_set(0)                                                                                    # Select the first entry by default

    # ===========================================================
    # ===== METHOD: Select the term and navigate to the new =====
    # ===========================================================
    def pushSelectTerm_CB(self):
        selectedTerm = self.listTerms.get(self.listTerms.curselection())

        # :: Get the href of the selected list item
        for link in self.soup.select('div.post li a'):
            if selectedTerm == link.text:
                termLink = link.get('href')
                print('==== SELECTED TERM ====')
                print(selectedTerm)
                print(termLink)

        self.sauceCases = urllib.request.urlopen(termLink).read()
        self.soupCases = bs.BeautifulSoup(self.sauceCases,'lxml')

        # :: Call the method to populate all the cases on the selected case files webpage
        self.populateCases()

    # ==================================================================================
    # ===== METHOD: Populate the cases Listbox with results from the selected term =====
    # ==================================================================================
    def populateCases(self):
        listCases = []
        self.linkCases = []
        for row in self.soupCases.select('table.caseindex tbody tr'):
            listCases.append(row.td.a.text)
            self.linkCases.append(row.td.a.get('href'))
        self.listCases.delete(0,'end')
        self.listCases.insert('end',*listCases)
        self.listCases.select_set(0)
        self.listCases.config(fg='blue')

    # ====================================================================
    # ===== METHOD: Select the case and display information about it =====
    # ====================================================================
    def pushSelectCase_CB(self):
        selectedCase = self.listCases.get(self.listCases.curselection())                                                # Get the text of the selected case
        print('\n==== SELECTED CASE ====')                                                                              # Print indicator header line
        print(selectedCase)                                                                                             # Print the name of the selected case

        # :: Get the href of the selected case
        for link in self.soupCases.select('table.caseindex tbody tr td a'):
            if selectedCase == link.text:
                caseLink = link.get('href')
                print(caseLink)

        # :: Get the soup for the selected case
        self.sauceSelCase = urllib.request.urlopen(caseLink).read()
        self.soupSelCase = bs.BeautifulSoup(self.sauceSelCase,'lxml')

        # :: Print the results from the case page
        listDateDocket = []                                                                                             # Initialize the list
        self.listDateDocketLinks = []                                                                                   # Initialize the list
        for col in self.soupSelCase.select('table#date-docket tbody tr td'):                                            # Loop through all the columns in the table
            listDateDocket.append(col.text.strip('\n').strip('\t'))                                                     # Get all the text from each column in the table
            if (col.a != None):                                                                                         # If there is an 'a' tag in the column
                self.listDateDocketLinks.append(col.a.get('href'))                                                      # Add the href to the list
            else:                                                                                                       # If there isn't an 'a' tag in the column
                self.listDateDocketLinks.append(None)                                                                   # Add a 'None' to the list

        # :: Populate the correct text boxes with the information
        self.textDocketNo.config(text=listDateDocket[0])                                                                # Populate the text of the Docket No. box
        self.textOpBelow.config(text=listDateDocket[1])                                                                 # Populate the text of the Op. Below box
        self.textArgument.config(text=listDateDocket[2])                                                                # Populate the text of the Argument box
        self.textOpinion.config(text=listDateDocket[3])                                                                 # Populate the text of the Opinion box
        self.textVote.config(text=listDateDocket[4])                                                                    # Populate the text of the Vote box
        self.textAuthor.config(text=listDateDocket[5])                                                                  # Populate the text of the Author box
        self.textTerm.config(text=listDateDocket[6])                                                                    # Populate the text of the Term box

        # :: Make the text blue if there is a link to be clicked
        # :: Bind the text with a double-click to call function to open link
        for i in range(len(self.listDateDocketLinks)):
            if (self.listDateDocketLinks[i] and i == 0):
                self.textDocketNo.config(fg='blue')
                self.textDocketNo.bind('<Double-Button-1>',lambda event, ind = i: self.openDateDocket_CB(event,ind))
            elif (self.listDateDocketLinks[i] and i == 1):
                self.textOpBelow.config(fg='blue')
                self.textOpBelow.bind('<Double-Button-1>',lambda event, ind = i: self.openDateDocket_CB(event,ind))
            elif (self.listDateDocketLinks[i] and i == 2):
                self.textArgument.config(fg='blue')
                self.textArgument.bind('<Double-Button-1>',lambda event, ind = i: self.openDateDocket_CB(event,ind))
            elif (self.listDateDocketLinks[i] and i == 3):
                self.textOpinion.config(fg='blue')
                self.textOpinion.bind('<Double-Button-1>',lambda event, ind = i: self.openDateDocket_CB(event,ind))
            elif (self.listDateDocketLinks[i] and i == 4):
                self.textVote.config(fg='blue')
                self.textVote.bind('<Double-Button-1>',lambda event, ind = i: self.openDateDocket_CB(event,ind))
            elif (self.listDateDocketLinks[i] and i == 5):
                self.textAuthor.config(fg='blue')
                self.textAuthor.bind('<Double-Button-1>',lambda event, ind = i: self.openDateDocket_CB(event,ind))
            elif (self.listDateDocketLinks[i] and i == 6):
                self.textTerm.config(fg='blue')
                self.textTerm.bind('<Double-Button-1>',lambda event, ind = i: self.openDateDocket_CB(event,ind))

        # :: Get the blog coverage
        blogNames      = []
        self.blogLists = []
        blogLinks = self.soupSelCase.select('h2#blog-coverage + ul li a')
        for i in blogLinks:
            blogNames.append(i.text)
            self.blogLists.append(i.get('href'))

        # Put the blogs into the list
        self.listBlogs.delete(0, 'end')
        self.listBlogs.insert('end', *blogNames)
        self.listBlogs.bind('<Double-Button-1>', self.openBlog_CB)
        self.listBlogs.config(fg='blue')

        # Get number of briefs and display numbers
        white, orange, cream, tan, Lblue, Lred, Lgreen, Dgreen, gray = 0,0,0,0,0,0,0,0,0
        briefRows = self.soupSelCase.select('table.dates_n_proceedings tr + tr')                   # Skip the header row (would have given None)
        for tr in briefRows:
            colorVal = tr.get('class')
            if (colorVal[0] == 'color0'):                   # Petition for a Write of Certiorari
                white = white + 1
            elif (colorVal[0] == 'color1'):                 # Brief in Opposition to a Writ of Certiorari
                orange = orange + 1
            elif (colorVal[0] == 'color2'):                 # Brief of Amicus Curiae at Petition Stage
                cream = cream + 1
            elif (colorVal[0] == 'color3'):                 # Reply Brief in Support of a Petition for a Writ of Certiorari
                tan = tan + 1
            elif (colorVal[0] == 'color4'):                 # Merits Brief of Petitioner or Appellant
                Lblue = Lblue + 1
            elif (colorVal[0] == 'color5'):                 # Merits Brief of Respondent or Appellee
                Lred = Lred + 1
            elif (colorVal[0] == 'color6'):                 # Brief of Amicus Curiae at Merits Stage in Support of Petitioner or Appellant
                Lgreen = Lgreen + 1
            elif (colorVal[0] == 'color7'):                 # Brief of Amicus Curiae at Merits Stage in Support of Respondent or Appellant
                Dgreen = Dgreen + 1
            elif (colorVal[0] == 'color9'):                 # Solicitor General
                gray = gray + 1

        self.numBriefWhite.config(text=white)
        self.numBriefOrange.config(text=orange)
        self.numBriefCream.config(text=cream)
        self.numBriefTan.config(text=tan)
        self.numBriefLBlue.config(text=Lblue)
        self.numBriefLRed.config(text=Lred)
        self.numBriefLGreen.config(text=Lgreen)
        self.numBriefDGreen.config(text=Dgreen)
        self.numBriefGray.config(text=gray)

    # ======================================================================
    # ===== METHOD: Open the double-clicked blog post from the Listbox =====
    # ======================================================================
    def openBlog_CB(self,event=None):
        selectedBlog = self.listBlogs.curselection()[0]
        webbrowser.open(self.blogLists[selectedBlog])

    # ======================================================================
    # ===== METHOD: Open the double-clicked blog post from the Listbox =====
    # ======================================================================
    def openDateDocket_CB(self,event,openInd):
        webbrowser.open(self.listDateDocketLinks[openInd])

    # =================================================================
    # ===== METHOD: Open the double-clicked case from the Listbox =====
    # =================================================================
    def openCasePage_CB(self,event=None):
        selectedCase = self.listCases.curselection()[0]
        webbrowser.open(self.linkCases[selectedCase])

# Create the actual GUI and display it
rootGUI = Tk()
rootGUI.title("ScotusBlog")
rootGUI.geometry("625x450")
app = Application(rootGUI)

rootGUI.mainloop()

