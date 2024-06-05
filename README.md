# Backend Flask Server for Concussions

run the flask server on 127.0.0.1:8086 through 
python main.py
in the terminal.

main.py file sets up APIs and registers all URIs. This includes Titanic API (Titanic sinking survival simulation), Recovery API (suggestions for recovery), and Concussion API (concussion recovery time predictor).

all .py files in the /api folder handle setting up of API Blueprints and requests from user server (127.0.0.1:4000 if running Concussions Frontend locally)

algorithmic code and ML data cleaning/predictions are all found within /model folder. concussion.py, recovery.py, and titanic.py are the main features in this project and unique to the developers.
