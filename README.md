## Python Flask Skeleton for Google App Engine

A skeleton for building Python applications on Google App Engine with the
Runs using python 2.7 (std27 virtualenv)

1. Install dependencies:

% pip install -r requirements.txt -t lib

2. Run locally:

% dev_appserver.py .

3. To deploy the application:

% appcfg.py update -A <your-project-id> -V v1 .

(appcfg.py set_default_version -V v1 -A <your-project-id> )
