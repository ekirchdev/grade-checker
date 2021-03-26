# grade-checker

This command line tool cyclically checks for a published grade in an university's grade management system.
It uses selenium to visit the website in a browser, but performs the check headless. The user
can specify the interval for checking.

The reference grade management system has an overview page with all exams
that the student has registered for; but whose results are not yet online.
As long as a module is still listed on this page, it can be assumed that
the grade has not been published. In the opposite case, the tool will open a pop-up window to inform
about the published grade.

## Requirements

* Python 3
* Chrome Driver: https://chromedriver.chromium.org/downloads (tested with Chrome on Windows)
* GeckoDriver: https://github.com/mozilla/geckodriver/releases (tested with Firefox on Ubuntu)

## Setup

```shell script
pip install -r requirements
```

- For Windows and Chrome, download the Chrome Driver and put the binary file on your PATH.
- For Firefox and Unix, download the Gecko Driver and put the binary file on your PATH. If you use a server-side unix without a GUI, you need to execute the following commands to run the script headless:
```shell script
sudo apt-get install xvfb
Xvfb :99 -ac &
export DISPLAY=:99
```
## Usage

To execute the check, run the script with these required command line arguments:
```shell script
python main.py -u "myusername" -p "mypassword" -m "Algorithms and Data Structures"
```

Too see more usage options, run:
```shell script
python main.py --help
```
