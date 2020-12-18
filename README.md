# PITCH APP
## Author 
[Barnabas Kamau](https://github.com/Barnabas27)

## Live Link
[here:](https://warm-pitches.herokuapp.com/)
## Description
Pitch App is an application that is developed using flask, and it allows the user to make a pitch in the given categories and also the user can get to comment on the pitches they have liked or even disliked.

## Specifications

### Behaviour Driven Development

1. display a list of categories
   * This is already displayed and the user can get to choose from whatever category they would want to choose.
2. display the various pitches in each category
  - INPUT: 'button' clicked.
  - OUTPUT: A page displaying the different pitches in the clicked category.
3. adds a new pitch
    - INPUT: add 'create pitch' button pressed.
    - OUTPUT: User taken to log in for or sign up.
4. after sign up
   - INPUT: user's input in the category they are to pitch.
   - OUTPUT: The user's pitch in the preferred category.
5. register user to the website:
    - INPUT: "A form containing required info of user is submitted"
    - OUTPUT: "user's display of the profile"

6. Comment on a category:
    - INPUT: "press comment button"
    - OUTPUT: "user's text area to comment.
7. Log in user to the website:
    - INPUT:"User enter password and email address"
    - OUTPUT: "User logged in to the system"

## Technologies used
- Python 3.8
- Flask frameworks
- Html,CSS(bootstrap)
- PostgreSQL
- Pip

## Setup Installations Requirements
* To run the application, in your terminal:
    1. Clone or download the Repository
    2. Create a virtual environment
    3. Read the requirements file an dinstall all the requirements alternatively you  could run pip3 install -r requirements.txt to automatically install all the requirements.
    4. Prepare environment variables
    5. export your DATAVASE_URL and SECRET_KEY
    6. Run chmod a+x start.sh
    7. Run ./start.sh
    8. Acce the application throught the link or local server 'localhost:5000'

### Develpment

Want to contribute?
- Reach out on:
 * bkamau032@gmail.com

## Known bug 
If you find a bug, feel free to do so by openint an issue [here](bkamau032@.gmail.com)

### License 
*MIT*
Copyright (c) 2020 ** Barnabas Kamau**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
