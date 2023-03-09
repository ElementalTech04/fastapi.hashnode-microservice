# FastAPI Hashnode Microservice

This is a FastAPI microservice that interacts with the Hashnode API to retrieve information about Hashnode users and
their articles. It is designed to be deployed on [Railway](https://railway.app/) but can be run locally or on any other
hosting platform.

## Setup

1. Clone the repository:

~~~
git clone https://github.com/travistech04/fastapi.hashnode-microservice.git
~~~

2. Install the requirements:

~~~
pip install -r requirements.txt
~~~

3. Set your Hashnode API key as an environment variable:

~~~
export HASHNODE_API_KEY=your-api-key
~~~

Replace your-api-key with your actual API key.

## Usage

To start the server locally, run:

~~~
uvicorn app.main:app --reload
~~~

This will start the server at http://localhost:8000/.

To deploy the microservice to Railway, follow these steps:

1. Create a new Railway project and link it to your GitHub repository.

2. Set the HASHNODE_API_KEY environment variable in the Railway project settings.

3. Add a new service in Railway and select "Python + FastAPI".

4. Enter the following command in the "Start Command" field:

~~~
uvicorn app.main:app --host=0.0.0.0 --port=$PORT
~~~

5. Click "Create Service" and wait for the deployment to finish.

6. Open the URL provided by Railway to access the microservice.

## Documentation
To access the Swagger documentation in a FastAPI application, follow these steps:

1. Start your FastAPI application by running the command uvicorn main:app --reload in your terminal. Here, main refers to the name of your Python file and app refers to the name of your FastAPI application object.

2. Open a web browser and go to http://localhost:8000/docs. This will take you to the Swagger documentation page for your FastAPI application.

3. The Swagger documentation page will display all the endpoints available in your FastAPI application. You can explore each endpoint by clicking on it.

4. To try out an endpoint, click on the "Try it out" button on the right side of the endpoint. This will open a form where you can enter the input parameters and execute the endpoint.

5. Once you have entered the input parameters, click on the "Execute" button. This will send a request to the endpoint and display the response below the input form.

6. You can also view the API documentation in JSON format by going to http://localhost:8000/docs.json. This can be useful if you want to integrate your FastAPI application with other tools or services.

7. Overall, using the Swagger documentation in a FastAPI application can be very helpful in understanding the available endpoints and testing them out.

## License

This project is licensed under the terms of the MIT license. See LICENSE for more information.
