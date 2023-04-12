## Python Flask Skeleton for Google App Engine

Make sure gcloud init has been called to set up google credentials.
Also points to project: artistannamir

### Using pyenv 3.10.5..
% pyenv install 3.10.5
% pyenv local 3.10.5
% python -m venv env
% source env/bin/activate
% pip install -r requirements.txt

2. Run locally:

% main.py

3. To deploy the application:

% gcloud app deploy

You can stream logs from the command line by running:
  $ gcloud app logs tail -s default

To view your application in the web browser run:
  $ gcloud app browse

  