# django-chat
A chatting app with Rasa will a collection of ready to use templates


# Installation Process
To install this app please follow this below steps:

### Run Backend
```
1. Create a virtual environment `virtualenv venv`
2. And activate it `source venv/bin/activate`(for ubuntu) `venv\Scripts\activate`(for windows)
3. Then change the directory to server/ and install dependencies `pip install -r requirements.txt`
4. Migrate to database `python manage.py migrate`
5. Now run the server `python manage.py runserver`
```

# Run Rasa commands
### rasa init
```
This command is used to create the initial project structure of rasa.
```
### rasa train
```
This command is used to train the chatbot on the nlu data and stories.
```
### rasa shell
```
This command loads the trained model and lets us talk through the command line.
```
### rasa interactive
```
This command starts an interactive session and new training data can be created by chatting with the chatbot.
```
### rasa run
```
This is used to start a new server with the trained model.
```
### rasa run actions
```
This is used to run the action server.
```
### rasa visualize
```
It shows us a visual representation of the stories.
```
### rasa x
```
This command is used to start rasa x.
```
### rasa -h
```
It shows us all the available commands.
```
### rasa data split nlu
```
These commands split the training data in the ratio of 80/20.
```

### Rasa command run
```
rasa run -m models --enable-api --cors="*" --debug --endpoints endpoints.yml --credentials credentials.yml
```

### Rasa train command to train a specific template
```
rasa train --domain chat-templates/cricket/domain.yml --data chat-templates/cricket/data/ --out chat-templates/cricket/models/
```

## Rasa run a specific models

### Keep specific models needed for a bot
```
rasa run -m chat-templates/cricket/models --enable-api --cors="*" --debug --endpoints endpoints.yml --credentials credentials.yml
```

### For testing templates keep only one model inside the models folder
### For real world models keep all models for a bot inside the models the bot

