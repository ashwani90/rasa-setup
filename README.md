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

### Train and run CRICKET template
### Not ready for use
#### Train the model
```
## Train the model
rasa train --domain chat-templates/cricket/domain.yml --data chat-templates/cricket/data/ --out chat-templates/cricket/models/
```
#### Run the model
```
rasa run -m chat-templates/cricket/models --enable-api --cors="*" --debug --endpoints endpoints.yml --credentials credentials.yml
```
#### Test the model
```
rasa shell -m chat-templates/cricket/models --enable-api --cors="*"  --endpoints endpoints.yml --credentials credentials.yml

```

### Train and run FINANCIAL template
### this is alsoo not ready as has extra configuration
#### Train the model
```
rasa train --domain chat-templates/financial/domain.yml --data chat-templates/financial/data/ --out chat-templates/financial/models/
```

#### Run the model
```
rasa run -m chat-templates/financial/models --enable-api --cors="*" --debug --endpoints endpoints.yml --credentials credentials.yml

```

#### Test the model
```
rasa shell -m chat-templates/financial/models --enable-api --cors="*"  --endpoints endpoints.yml --credentials credentials.yml

```

### Train and run HELPDESK template

#### Train the model
```
rasa train --domain chat-templates/helpdesk/domain.yml --data chat-templates/helpdesk/data/ --out chat-templates/helpdesk/models/

```
#### Run the model
```
rasa run -m chat-templates/helpdesk/models --enable-api --cors="*" --debug --endpoints endpoints.yml --credentials credentials.yml

```

#### Test the model
```
rasa shell -m chat-templates/helpdesk/models --enable-api --cors="*"  --endpoints endpoints.yml --credentials credentials.yml

```

### Train and run RETAIL template

#### Train the model
```
rasa train --domain chat-templates/retail/domain.yml --data chat-templates/retail/data/ --out chat-templates/retail/models/
```

#### Run the model
```
rasa run -m chat-templates/retail/models --enable-api --cors="*" --debug --endpoints endpoints.yml --credentials credentials.yml

```

#### Test the model
```
rasa shell -m chat-templates/retail/models --enable-api --cors="*"  --endpoints endpoints.yml --credentials credentials.yml

```

### Train and run RETAIL-STORE template

#### Train the model
```
rasa train --domain chat-templates/retail-store/domain.yml --data chat-templates/retail-store/data/ --out chat-templates/retail-store/models/

```

#### Run the model
```
rasa run -m chat-templates/retail-store/models --enable-api --cors="*" --debug --endpoints endpoints.yml --credentials credentials.yml

```

#### Test the model
```
rasa shell -m chat-templates/retail-store/models --enable-api --cors="*"  --endpoints endpoints.yml --credentials credentials.yml

```

### Train and run BREAKOUT template

#### Train the model
```
rasa train --domain chat-templates/breakoutbot/domain.yml --data chat-templates/breakoutbot/data/ --out chat-templates/breakoutbot/models/
```

#### Run the model
```
rasa run -m chat-templates/breakoutbot/models --enable-api --cors="*" --debug --endpoints endpoints.yml --credentials credentials.yml

```

#### Test the model
```
rasa shell -m chat-templates/breakoutbot/models --enable-api --cors="*"  --endpoints endpoints.yml --credentials credentials.yml

```

### Train and run CONCERTBOT template

#### Train the model
```
rasa train --domain chat-templates/concertbot/domain.yml --data chat-templates/concertbot/data/ --out chat-templates/concertbot/models/
```

#### Run the model
```
rasa run -m chat-templates/concertbot/models --enable-api --cors="*" --debug --endpoints endpoints.yml --credentials credentials.yml

```

#### Test the model
```
rasa shell -m chat-templates/concertbot/models --enable-api --cors="*"  --endpoints endpoints.yml --credentials credentials.yml

```

### Train and run E2EBOT template

#### Train the model
```
rasa train --domain chat-templates/e2ebot/domain.yml --data chat-templates/e2ebot/data/ --out chat-templates/e2ebot/models/

```

#### Run the model
```
rasa run -m chat-templates/e2ebot/models --enable-api --cors="*" --debug --endpoints endpoints.yml --credentials credentials.yml

```

#### Test the model
```
rasa shell -m chat-templates/e2ebot/models --enable-api --cors="*"  --endpoints endpoints.yml --credentials credentials.yml

```

### Train and run FORMBOT template

#### Train the model
```
rasa train --domain chat-templates/formbot/domain.yml --data chat-templates/formbot/data/ --out chat-templates/formbot/models/
```

#### Run the model
```
rasa run -m chat-templates/formbot/models --enable-api --cors="*" --debug --endpoints endpoints.yml --credentials credentials.yml

```

#### Test the model
```
rasa shell -m chat-templates/formbot/models --enable-api --cors="*"  --endpoints endpoints.yml --credentials credentials.yml

```

### Train and run KNOWLEDGEBASEBOT template

#### Train the model
```
rasa train --domain chat-templates/knowledgebasebot/domain.yml --data chat-templates/knowledgebasebot/data/ --out chat-templates/knowledgebasebot/models/
```

#### Run the model
```
rasa run -m chat-templates/knowledgebasebot/models --enable-api --cors="*" --debug --endpoints endpoints.yml --credentials credentials.yml

```

#### Test the model
```
rasa shell -m chat-templates/knowledgebasebot/models --enable-api --cors="*"  --endpoints endpoints.yml --credentials credentials.yml

```

### Train and run MOODBOT template

#### Train the model
```
rasa train --domain chat-templates/moodbot/domain.yml --data chat-templates/moodbot/data/ --out chat-templates/moodbot/models/
```

#### Run the model
```

rasa run -m chat-templates/moodbot/models --enable-api --cors="*" --debug --endpoints endpoints.yml --credentials credentials.yml

```

#### Test the model
```
rasa shell -m chat-templates/moodbot/models --enable-api --cors="*"  --endpoints endpoints.yml --credentials credentials.yml

```

### Train and run REMINDERBOT template

#### Train the model
```
rasa train --domain chat-templates/reminderbot/domain.yml --data chat-templates/reminderbot/data/ --out chat-templates/reminderbot/models/
```

#### Run the model
```
rasa run -m chat-templates/reminderbot/models --enable-api --cors="*" --debug --endpoints endpoints.yml --credentials credentials.yml

```

#### Test the model
```
rasa shell -m chat-templates/reminderbot/models --enable-api --cors="*"  --endpoints endpoints.yml --credentials credentials.yml

```

### Train and run RESPONSESELECTORBOT template

#### Train the model
```
rasa train --domain chat-templates/responseselectorbot/domain.yml --data chat-templates/responseselectorbot/data/ --out chat-templates/responseselectorbot/models/
```

#### Run the model
```
rasa run -m chat-templates/responseselectorbot/models --enable-api --cors="*" --debug --endpoints endpoints.yml --credentials credentials.yml

```

#### Test the model
```
rasa shell -m chat-templates/responseselectorbot/models --enable-api --cors="*"  --endpoints endpoints.yml --credentials credentials.yml

```

### Train and run ELEARNING template

#### Train the model
```
rasa train --domain chat-templates/e-learning/domain.yml --data chat-templates/e-learning/data/ --out chat-templates/e-learning/models/
```

#### Run the model
```
rasa run -m chat-templates/e-learning/models --enable-api --cors="*" --debug --endpoints endpoints.yml --credentials credentials.yml

```

#### Test the model
```
rasa shell -m chat-templates/e-learning/models --enable-api --cors="*"  --endpoints endpoints.yml --credentials credentials.yml

```

### Train and run HIRING-TEAM template
## In Working state
#### Train the model
```
rasa train --domain chat-templates/hiring-team/domain.yml --data chat-templates/hiring-team/data/ --out chat-templates/hiring-team/models/
```

#### Run the model
```
rasa run -m chat-templates/hiring-team/models --enable-api --cors="*" --debug --endpoints endpoints.yml --credentials credentials.yml

```

#### Test the model
```
rasa shell -m chat-templates/hiring-team/models --enable-api --cors="*"  --endpoints endpoints.yml --credentials credentials.yml

```

### Train and run ORDER-MANAGE template

#### Train the model
```
rasa train --domain chat-templates/order-manage/domain.yml --data chat-templates/order-manage/data/ --out chat-templates/order-manage/models/
```

#### Run the model
```
rasa run -m chat-templates/order-manage/models --enable-api --cors="*" --debug --endpoints endpoints.yml --credentials credentials.yml

```

#### Test the model
```
rasa shell -m chat-templates/order-manage/models --enable-api --cors="*"  --endpoints endpoints.yml --credentials credentials.yml

```

### Train and run RETAIL-STORE template

#### Train the model
```
rasa train --domain chat-templates/retail-store/domain.yml --data chat-templates/retail-store/data/ --out chat-templates/retail-store/models/
```

#### Run the model
```
rasa run -m chat-templates/retail-store/models --enable-api --cors="*" --debug --endpoints endpoints.yml --credentials credentials.yml

```

#### Test the model
```
rasa shell -m chat-templates/retail-store/models --enable-api --cors="*"  --endpoints endpoints.yml --credentials credentials.yml

```

### Train and run TECH-CLASSIFY template

#### Train the model
```
rasa train --domain chat-templates/tech-classify/domain.yml --data chat-templates/tech-classify/data/ --out chat-templates/tech-classify/models/
```

#### Run the model
```
rasa run -m chat-templates/tech-classify/models --enable-api --cors="*" --debug --endpoints endpoints.yml --credentials credentials.yml

```

#### Test the model
```
rasa shell -m chat-templates/tech-classify/models --enable-api --cors="*"  --endpoints endpoints.yml --credentials credentials.yml

```

### Train and run INSURANCE template

#### Train the model
```
rasa train --domain chat-templates/insurance/domain.yml --data chat-templates/insurance/data/ --out chat-templates/insurance/models/
```

#### Run the model
```
rasa run -m chat-templates/insurance/models --enable-api --cors="*" --debug --endpoints endpoints.yml --credentials credentials.yml

```

#### Test the model
```
rasa shell -m chat-templates/insurance/models --enable-api --cors="*"  --endpoints endpoints.yml --credentials credentials.yml

```

### Train and run FINANCIAL-SPACES template

#### Train the model
```
rasa train --domain chat-templates/financial-spaces/ --data chat-templates/financial-spaces/ --out chat-templates/financial-spaces/models/
```

#### Run the model
```
rasa run -m chat-templates/financial-spaces/models --enable-api --cors="*" --debug --endpoints endpoints.yml --credentials credentials.yml
```

#### Test the model
```
rasa shell -m chat-templates/financial-spaces/models --enable-api --cors="*"  --endpoints endpoints.yml --credentials credentials.yml

```
