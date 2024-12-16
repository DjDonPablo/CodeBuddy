def get_prompt(prompt, files):
    if len(files) == 0:
        return prompt
    elif len(files) == 1:
        return one_context_file_prompt(
            prompt, list(zip(files.keys(), files.values()))[0]
        )
    else:
        return multiple_context_file_prompt(
            prompt, list(zip(files.keys(), files.values()))
        )


def one_context_file_prompt(prompt, file):
    return (
        "Here is the content of my file " + file[0] + ":\n"
        "```\n" + file[1] + "```\n"
        "I want you to answer to the following prompt: " + prompt + ".\n"
        "Using the file content to answer the prompt is NOT necessary, only use it if relevant."
    )


def multiple_context_file_prompt(prompt, files):
    file_contents = "".join(
        "File " + file[0] + ":\n```\n" + file[1] + "```\n" for file in files
    )
    return (
        "Here is the content of my files:\n"
        + file_contents
        + "I want you to answer to the following prompt: "
        + prompt
        + ".\n"
        "Using the files content to answer the prompt is NOT necessary, only use it if relevant."
    )
