# 0x15. API

## Description
Old-school system administrators usually only know Bash and that is what they use to build their scripts. While Bash is perfectly fine for a lot of things, it can quickly get messy and not efficient compared to other programming languages. The new generation of system administrators, usually called SREs, are pretty much regular software engineers but instead of building products, they are managing systems. And one of the big differences with their predecessors is that they know more than just Bash scripting.<br>One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them – access and modify their data. In this project, you will access employee data via an API to organize and export them to different data structures.<br>This is a perfect example of a task that is not suited for Bash scripting, so let’s build Python scripts.

## Tasks
| Files | Description |
|----- | -----------|
| [0-gather_data_from_an_API.py](./0-gather_data_from_an_API.py) | Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress |
| [1-export_to_CSV.py](./1-export_to_CSV.py) | Python script to export data in the CSV format, extending from 0-gather_data_from_an_API.py |
| [2-export_to_JSON.py](./2-export_to_JSON.py) | Python script to export data in the JSON format, extending from 0-gather_data_from_an_API.py |
| [3-dictionary_of_list_of_dictionaries.py](./3-dictionary_of_list_of_dictionaries.py) | Python script to export data in the JSON format, extending from 0-gather_data_from_an_API.py and 2-export_to_JSON.py |
