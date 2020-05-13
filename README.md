# Wizardify


### Create virtual environment to local wizardify repository

1. Create virtual environment: 

```
 	python3 -m venv venv
	OR
	python -m venv venv
```

2. Activate virtual environment
 On macOS and Linux:

```
 	source venv/bin/activate
```
 On Windows:

```
 	venv\Scripts\activate
```

3. Install requirements to new environment

```
	pip install -r requirements.txt
```


Optional

Make a list of all required packages

```

	pip freeze > requirements.txt

```

Show content of requirements.txt

```

	cat requirements.txt

```