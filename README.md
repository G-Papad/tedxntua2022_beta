# tedxntua2022_beta

# Installation

- Clone the repository:<br>
``git clone git@github.com:G-Papad/tedxntua2022_beta.git``

- Create and Activate the virtual environment:<br>
``python -m venv env``<br>
``.\env\Scripts\activate (Windows)``<br>
``source env/bin/activate (Unix)``

- Install requirements:<br>
``python -m pip install -r requirements.txt``

- Make migrations:<br>
``python -m manage.py migrate``

- Run server:<br>
``python -m manage.py runserver``

# File Structure

- page/templates:<br>
  Contains the html code for each page.

- tedxntua2022/templates:<br>
  Contains the html code for base.html, the header and the footer.
 
- static/page/(img, css, js):<br>
  Contains each page's Javascript, CSS/SCSS code and static images needed.

- static/img:<br>
  Contains static images needed in more than one page.
