# amadeus-safeplace
Neighborhood Safety Map in Python with Amadeus and HERE Maps


### Create a venv inside the folder:

```
python3 -m venv venv
```

### Activate the venv

```
. venv/bin/activate
```


### Install dependencies:

```
pip3 install -r requirements.txt
```

### Replace the API Tokens:

Replace with Here maps API key:

https://github.com/milap-neupane/amadeus-safeplace/blob/4834fd0c093d47bce9dff796bfffd870b4de48cd/templates/safeplace.html#L24

Replace with Amadeus Client ID and Client Secret:

https://github.com/milap-neupane/amadeus-safeplace/blob/main/amadeus_service.py#L5

### Start the server 

```
python main.py
```

 This will start the server in 5000 port and can be accessed from the url http://127.0.0.1:5000/
