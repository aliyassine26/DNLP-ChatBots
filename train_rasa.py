
import os
import nest_asyncio
from rasa.cli.scaffold import create_initial_project
import rasa

nest_asyncio.apply()

os.chdir("/content/")
project = "my-chatbot"
create_initial_project(project)
os.chdir(project)

config = "config.yml"
training_files = "data/"
domain = "domain.yml"
output = "models/"

model_path = rasa.train(domain, config, [training_files], output).model
print("Model trained at:", model_path)
