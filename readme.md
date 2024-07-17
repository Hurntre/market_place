# pull the code

# install python if you don't have it installed

# open the market place app on your IDE

# create the virtual environment inside the application directory. This will house all the dependencies

python3 -m venv virtual_env

# activate the virtual environment

source virtual_env/bin/activate

# install the dependencies

python3 -m pip install flask

# set flask env variables

## if you are on macOS

export FLASK_APP=market
export FLASK_DEBUG=1

## if you are on windows

set FLASK_APP=market
export FLASK_DEBUG=1

the FLASK_DEBUG=1 ensures that the app restarts automatically anytime you make a change

## run the application

flask run
