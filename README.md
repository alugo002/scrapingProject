# About my scraping project
## What I wanted to collect
My original plan was to collect all the information regarding bills from the link of all bills for all 990 bills. I wanted to collect each bill's number, title, original author and when the last action on the bill was.
I also wanted to collect all the information of senators from all 40 Florida senate districts, including their names, districts and parties.
The information was meant to be put neatly into two csv files, so that I could later use SQL to join both files and examine which parties and senators saw the most success with their bills.

## How I got the what I wanted
In my billAction.py file, I first made a for loop that would scrape all the information I wanted from the first page. Then I put that same for loop into a while loop, but changed its function to append instead of writing into the csv. I also set up the driver to scrape the href from the next button on the page so it could change the driver after clicking into the next page. That way, the driver knows to scrape the following information off the next page and not the first page. Finally, I closed it off with an except.

Meanwhile, in my senators.py file, I defined a function that would simply do what the billAction.py file did without scraping the links to the next pages because all the information I needed was in the first page. 

## Challenges I ran into
I had a hard time getting the driver to recognize that I wanted to scrape more than one page in my billAction.py file. I found it harder than expected to collect href's from each page after clicking into them. I also didn't weant to have to make the scraper go through all 20 pages twice just to get the urls then a second time for the information. The while loop which allowed me to change the url as it scraped, helped me overcome that challenge.

The second challenge I found was getting clean csv files. I tried adding the strip() finction to both files, but it didn't seem to work for some reason, so that challenge was never overcome this on time. 
