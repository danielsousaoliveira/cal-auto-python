# Automatic Calendar in Python

Automatically schedule tasks from github into google calendar, using Python

## Setup

1. Clone this repository and create a virtual environment

```bash
$ git clone
$ cd cal-auto-python
$ python3 -m venv venv
$ . venv/bin/activate
```

2. Install dependencies and packages

```bash
$ (venv) pip install -r requirements.txt
```

## Run

1. Add google credentials.json to auth/credentials.json

2. Add github token to auth/ghub.json

```bash
{
    "token": "xxxxxxxxxxx",
    "project_id": "PVT_xxxxxxxxxx"
}
```

3. Run the script

```bash
$ (venv) python3 src/main.py
```

## Roadmap

[x] ~~Retrieve project data from github~~ \
[x] ~~Add events and tasks to google calendar~~ \
[x] ~~Schedule based on priority~~ \
[ ] Optimize event distribution \
[ ] Fix duplicated events and tasks

## References

[Google Calendar API](https://developers.google.com/calendar/api/quickstart/python) \
[Github Projects API](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-api-to-manage-projects?tool=curl)
