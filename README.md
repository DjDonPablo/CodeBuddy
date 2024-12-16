![CodeBuddy Logo](/assets/logo.png")

<div align="center"><h1>Use CodeBuddy to empower your coding experience with AI !</h1></div>

> [!WARNING]  
> To run this extension, you also need to run docker images to . If you want to run it on **GPU**, download this ..., else download that ... TODO

## Why CodeBuddy ?

CodeBuddy is the best **free** and **open-source** alternative to use AI in VSCode ! It also works **offline** !

With CodeBuddy, autocompletion is no longer a dream, moreover, you can also chat with a LLM and give it project files as context.

What's great is that you can choose which models you want to use ! By default, we chose **Qwen2.5-Coder-3b-base** for autocompletion and **Qwen2.5-Coder-3b-instruct** for the chat because of their great performances (both models run easily on a computer with 16go RAM at the same time). **Adapt** the model according to your **hardware** and your use case !

# INSERER UNE DEMO

## Extension settings

- `CodeBuddy: Server_port`: server's port to interact with models. Refer to the section [Extension configuration](#extension-configuration) if you want to change this value.
- `CodeBuddy: Autocomplete`: enable or disable the autocompletion. If you really don't want the autocomplete at anytime, you can set the environment variable `CODEBUDDY_DISABLE_AUTOCOMPLETE` to `true`.

## Extension configuration

### Change models

Models run in background with **Ollama**.

To change the models, ... TODO

For the autocomplete feature, the LLM handling the task needs to have a **fill in the middle** training, with 3 tokens. TODO

### Change server port

The server default port is **6969**. If you want to change it, just set the environment variable `CODEBUDDY_SERVER_PORT` with the value you want. For example :

```console
export CODEBUDDY_SERVER_PORT=8080
```

Then, you can reload the docker and change the `CodeBuddy: Server_port` setting in vscode with the same value you used in the previous command.

## CodeBuddy creation

This project was initially a group project for the **Advanced NLP** course at **EPITA** : https://github.com/Koweez/AdvancedNLP.

## Extend CodeBuddy

You can create **PR** to develop CodeBuddy.