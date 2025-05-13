# Fastapi-orders
Conditional offer on product based on count in bucket(user input)

### How to run the application

- Run the following command to create a VirtualEnv  

```
> python3 -m venv .venv
```

- Activate the env

```
> source .venv/bin/activate
```

- Install the dependencies

```
> pip install -r requirements.txt
```

- Run the application via uvicorn server
```
> uvicorn main:app --reload
```

### Steps to validate the functionality

- On any browse open the following url to open FastApi's swagger docs   
http://localhost:8000/docs

- In the basket section use the `Calculate basket price` API to test the functionality.

![image](./static/basket.png)

Click on `Try it out` on top right corner and pass the products strings as mentioned below as the request body.

![image](./static/Testcases.png)

### Result screen
![image](./static/Result.png)

