# LAB Class 17

## Project: Web Scraper

### Author: Dennis DeVries

### Setup

To run the application, first activate a virtual environment. Then run the following command in your terminal: `python web_scraper/scraper.py`

The output of the script will look something like the following:

```md
2
That same year, not coincidentally, Alaska repealed its state income tax.[citation needed]

One of the most prominent movies filmed in Alaska is MGM's Eskimo/Mala The Magnificent, starring Alaska Native Ray Mala. In 1932, an expedition set out from MGM's studios in Hollywood to Alaska to film what was then billed as "The Biggest Picture Ever Made". Upon arriving in Alaska, they set up "Camp Hollywood" in Northwest Alaska, where they lived during the duration of the filming. Louis B. Mayer spared no expense in spite of the remote location, going so far as to hire the chef from the Hotel Roosevelt in Hollywood to prepare meals.[citation needed]
```

The number is the number output by the get_citations_needed_count function. For my example, I used https://en.wikipedia.org/wiki/Alaska.

The text output is from the get_citations_needed_report function which prints the corresponding text related to the "citation needed" reference.