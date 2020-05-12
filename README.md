# Wizardify 
<!-- https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md#person-fantasy-->


## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [License](#license)

## About The Project

<!--pic here ?-->
<img src="logo.png">
A web service that uses Deep Learning AI to analyse pictures and categorize them. 
This machine-learning project was created to help answer the burning question:

What is my D&D -class?

Simple, but effective interface guides you on your journey. :compass:

The idea for the project was born from a need to learn about Machine Learning. After some thought, we landed on image analysis and a Dungeons & Dragons based concept. The basic idea was to create an AI model that could analyse a picture and categorize it based on the 12 classes of the game. This model would be deployed into a web app for easy access to all.

### Built With

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Bootstrap](https://getbootstrap.com)
* [TensorFlow](https://www.tensorflow.org/)
* [Keras](https://keras.io/)

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites
* Install Python 3.x
```sh
https://www.python.org/downloads/
```

### Installation
 
1. Clone the repo
```sh
git clone https://github.com/github_username/repo.git
```

2. Create virtual environment: 

```sh
python3 -m venv venv
OR
python -m venv venv
```

3. Activate virtual environment

 On macOS and Linux:

```sh
 source venv/bin/activate
```
 On Windows:

```
 venv\Scripts\activate
```

4. Install requirements to new environment

```sh
pip install -r requirements.txt
```


#### Optional

If you make changes and add new packages remember to update requirements.txt

```sh
pip freeze > requirements.txt
```

Show content of requirements.txt

```sh
cat requirements.txt
```

## License 
<!-- What license are we using?-->
Distributed under the MIT License. See `LICENSE` for more information.
