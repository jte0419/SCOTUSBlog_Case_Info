# SCOTUSBlog_Case_Info

I wanted to learn how to webscrape and code Python GUIs, so I decided to pick a site that has a very regular format: www.scotusblog.com.  I wrote this code while I was down in Virginia for the summer of 2017, and I haven't really looked at it since then.  For the webscraping, I use [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/).  For the Python GUI, I use [tkinter](https://wiki.python.org/moin/TkInter), mainly because there were good tutorials available.

## Running the Program

I'm no expert in Python, so if something I write sounds confusing, that's probably because it probably is.  Here's how I run the code.  I open up the .PY file in IDLE (version 3.5).  Then at the top, you click on the *Run* menu, and click on *Run Module*.  You can also just press *F5*.  The GUI will pop up, and will obviously need an internet connection because we are scraping the webpage for SCOTUSBlog to populate the GUI.

The only list that is populated at first is the *Term* list, so select a term, and press the *Select Term* button.  This will populate the *Case* list.  Note that all the entries in this list are now blue.  When text is blue, it means it's a link that you can open by double-clicking on it.  If you want to go to a case page, simply double-click on the case in the list.  

If you want more information about a specific case, select that case and press the *Select Case* button.  This will populate the rest of the GUI.  In the *Docket Info* section, there will be some info that you can also double-click on if it is in blue.  When a case has been decided and an opinion is issued, double-clicking on the *Opinion* entry will open a PDF of the opinion.

The briefs section shows the number of each type of brief.  Be aware that this only works for years going back to OT2012, because for the earlier years, the way the site lists the briefs in the HTML is different, and I didn't take the time to account for that.  In general, the more briefs are filed, the higher-profile a case it is.  Each color refers to a specific type of brief, and you can [click here](http://www.supremecourtpress.com/supreme_court_rules.html) for more information.

My favorite feature is the *Blog Posts* section, which lists all the blog posts for that particular case in order from most recent.  All of these should be highlighted in blue, and are thus links that can be double-clicked and will open in a web browser.

## Things I Want To Update

As mentioned, I haven't looked at this code since the summer, but here are some things I'd like to update in the future.

* Alphabetize the *Case* list
* Search feature for *Case* list
* Search feature for all cases in their database
* Update briefs counter for years before 2012
