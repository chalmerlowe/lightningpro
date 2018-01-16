# Run the basic skeleton locally with django 1.11
* clone the repo
* recommend setting up a virtualenv and then run
```
python3 pip install -r requirements.txt
```
* make a local db by running
```
python3 manage.py migrate
```
* start the server with
```
python3 manage.py runserver
```
* go to http://localhost:8000/manager/
* test it

# lightningpro
Lightning Talk management tool

---

Lightning Pro is a tool designed to simplify the signup and management of [lightning talks](https://en.wikipedia.org/wiki/Lightning_talk)

Key features should include a website with the following capabilities:
* signup page 
    * input ~140 character title and description (single text input field)
    * input name (text input field)
    * input email address (text input field)
    * input scheduling preference via dropdown (such as the following):
        * I prefer to go early during the session
        * I prefer to go late in the session
        * I have no preference
    * ability to cancel
* admin page
    * mark talks as accepted, waitlisted, rejected
    * arrange/adjust the order of the talks
    * adjust the order of the talks
    * notify speakers via email
* login page
    * ability to signup
    * ability to login
* display page
    * show the order of the selected talks
    * available to viewers, logged in OR not
* timer page (reminiscent of [http://hackandtell.org/timer/](http://hackandtell.org/timer/)
    * display the time remaining
    * change the color of the timer from green (at 5:00) to red (at 0:00)
    * blink the timer at 10 seconds
* branding
    * LightningPro will need the capability to highlight two logos/brands
         * logo one: the logo of the organization using the tool
         * logo two: the LightningPro logo
    * Modifying the organization logo should be straightforward 
* user interface design
    * the user interface design should be straightforward, intuitive and easy to use without complicated instructions
