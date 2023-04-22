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

## Edit the website
- Change the ``seminar_import.py``, especially the ``org``, ``org_url`` and ``org_email``. 
- install necessary packages of python
  ```
  pip install pandas
  ```
- run the python code with 
  ```
  python seminar_import.py <YEAR> <SEMESTER> <GOOGLE_SHARED_SHEET_URL>
  ```
