```
                 _____ _           _   _____ ______ _____ 
                /  __ \ |         | | |  __ \| ___ \_   _|
 _ __ ___  _   _| /  \/ |__   __ _| |_| |  \/| |_/ / | |  
| '_ ` _ \| | | | |   | '_ \ / _` | __| | __ |  __/  | |  
| | | | | | |_| | \__/\ | | | (_| | |_| |_\ \| |     | |  
|_| |_| |_|\__, |\____/_| |_|\__,_|\__|\____/\_|     \_/  
            __/ |                                         
           |___/                                         
```

A chatGPT generated chatGPT using OpenAI API, Python and Flask.

Disclaimer: The code is 90% written by the LLM therefore it is likely to contain bugs or injection vulnerabilities. Use at your own risk.

# Usage
Use with Docker using the Dockerfile or with docker-compose. A template is provided.

The app will create a session for the past messages therefore if you refresh it should reload all the old messages. This can be reset using the bin icon.

You can select either GPT3.5-turbo or GPT4 next to the trash. This will apply on the next sent messages

It is likely that a long conversation will use a lot of tokens so, if previous context is not required, start a new session.
