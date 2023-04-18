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

Disclaimer: The code is 90% written by the LLM therefore it is likely to contail bugs or injection vulnerabilities. Use at your own risk.

# Features
- Git-like markdown rendering
- Text-to-Speech with compatible browser
- Model selection
- Retained session messages 
- Clear button to start a new session

# Usage
Use with Docker using the Dockerfile or with docker-compose. A template is provided.
- Rename `docker-compose-template.yml` to `docker-compose.yml`
- Add in your `OPENAI_API_KEY` into the `docker-compose.yml` and set the SSL requirements
- Run `docker-compose up --build` or `docker-compose up -d --build` if you want it to run as detached.

You can select either GPT3.5-turbo or GPT4 next to the trash. This will apply on the next sent messages

It is likely that a long conversation will use a lot of tokens so, if previous context is not required, start a new session.