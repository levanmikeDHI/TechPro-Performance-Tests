Installation
============

You can install the required softwares in 2 ways

OPTION 1:

1. Install python 2.7.* (Not Python 3)

2. Install locust using PIP . Type in commandline

.. code-block:: bash

    $ pip install locustio

3. Install a python package manager. Anaconda is preferred. You can install Anaconda from here https://www.anaconda.com/download/#macos

4. Then run the following command in command line

.. code-block:: bash

    $ conda install bokeh

Option 2:

1. Install python 2.7.* (Not Python 3)

2. In terminal cd to the project root and Install the required libraries by executing the following command in terminal

.. code-block:: bash

    $ pip install -r requirements.txt


Running the Load tests
======================

To run the the load test first start the bokeh server through terminal using the following command

.. code-block:: bash

    $ bokeh serve

In terminal navigate to project root . Then run the file that has locust tests using the following command

.. code-block:: bash

    $ locust --host=localhost -f poctest.py

Then in a separate terminal window, run the plotter.py

.. code-block:: bash

    $ python  plotter.py


At this point a browser tab should open up automatically showing 2 empty line graphs

Open another browser tab and go to http://localhost:8089/ . Type in the number of users and hatch rate and Start Swarming
