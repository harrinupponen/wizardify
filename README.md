# Wizardify 


## Table of Contents

- [Wizardify](#wizardify)
  - [Table of Contents](#table-of-contents)
  - [About The Project](#about-the-project)
    - [Built With](#built-with)
  - [Implementation](#implementation)
  - [Tensorflow js](#tensorflow-js)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
      - [Optional](#optional)
  - [License](#license)

## About The Project

A web service that uses Deep Learning AI to analyse pictures and categorize them. 
This machine-learning project was created to help answer the burning question:

What is my D&D -class?

The idea for the project was born from a need to learn about Machine Learning. After some thought, we landed on image analysis and a Dungeons & Dragons based concept. The basic idea was to create an AI model that could analyse a picture and categorize it based on the 12 classes of the game. This model would be deployed into a web app for easy access to all.

### Built With

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Bootstrap](https://getbootstrap.com)
* [TensorFlow](https://www.tensorflow.org/)
* [Keras](https://keras.io/)

## Implementation

The program is Python based web application that is built upon a Flask framework. Our Tensorflow and Keras based AI program is separate from the web application, but the model that is built with it is critical to the app.

The readme for the Tensorflow part can be seen here: [TENSOR-README](https://github.com/harrinupponen/wizardify/blob/master/TENSOR-README.md)

Flask is used to work out the routing on the app. The front page of the web app can recieve images sent by the user, which are then routed to the model for comparison. After the results are in, the user is redirected to the results page. The visuals of the app use Flask Bootstrap.

## Tensorflow js

We also made a version using [Tensorflow.js](https://www.tensorflow.org/js), that can be found from [TFJS-folder](https://github.com/harrinupponen/wizardify/tree/master/TFJS). This version is tested to be working with [Heroku](https://www.heroku.com/) and it uses [Node.js](https://nodejs.org/en/) and [express.js](https://expressjs.com/) for routing. For further dependencies and information about the build, see [package.json](https://github.com/harrinupponen/wizardify/blob/master/TFJS/package.json) and [server.js](https://github.com/harrinupponen/wizardify/blob/master/TFJS/server.js).

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
git clone https://github.com/harrinupponen/wizardify.git
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
