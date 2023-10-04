A Template for Seminar Website

## Run the code
- install hugo. see https://gohugo.io/installation/
- clone the project
- clone the hugo-story repository
  ```
  git clone https://github.com/caressofsteel/hugo-story.git
  ```
- hugo serve

## Generate the website
- run 
  ```
  hugo
  ```
- copy public to where your website is. 

## Update the website
- Change the ``seminar_import.py``, especially the ``org``, ``org_url`` and ``org_email``. 
- Change the ``data/banner.yml`` with updated link ``#schedule-YEAR-SEMESTER``, for instance ``#schedule-2023-Fall``.
- Change the ``layouts/index.html`` with updated ``{{ partial "items" ...}}`` and ``{{ partial "spotlights" ...}}``
- install necessary packages of python
  ```
  pip install pandas
  ```
- run the python code with 
  ```
  python seminar_import.py <YEAR> <SEMESTER> '<GOOGLE_SHARED_SHEET_URL>'
  ```
  **Note the url needs to be quoted.**
## FAQ
- What is the format of the google sheet?
- see https://docs.google.com/spreadsheets/d/1cFzxm3_-cEb2RLEbAkrJbO6QnqXs0OXK/edit?usp=sharing&ouid=113340153287953812217&rtpof=true&sd=true
- What if the abstract/title contains quotation marks?
- Please remove the quotation marks or replace with other symbols.
