# Final-Project-NLPH
This project try to use machine learning and hebrew rules to create a hebrew NLP models that can identify sentences with wrong name of numbers and fix wrong sentences to correct name of numbers in hebrew.

for demonstration please see the video attached in the root folder `Video Project NLPH.mov`.
to see the document behind it please see `NLP Hebrew Final Project - Roy - Noam.pdf`

## Final Document
(in hebrew) final_project_nlph.pdf

## Data Files
Generated data file - sentences with numbers in hebrew (data_synthetic.tsv).
Bag of hebrew words - (hebrew_names.txt)

## How to run
1. Clone repo
2. Open 3 tabs in terminal:
    Server Node js(First Tab):
    1. `$ cd Final-Project-NLPH/Web/Server`
    2. `$ npm install`
    3. `$ nodemon index.js`
    

    Client (Second Tab):
    1. `$ cd Final-Project-NLPH/Web/Client/my-app/src`
    2. `$ npm install`
    3. `$ npm start`

    Python ML Controller (Third Tab):
    1. install requirements.txt 
    2. `$ cd Final-Project-NLPH/Parser`
    3. `$ python3 nlph_http_request_handler.py                `

3. Browse to localhost:3002 and Plug and Play :)
