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

## Endpoints

### GET /users/{username}

Retrieves information about a Hashnode user.

Example response:

~~~
{
  "username": "travistech",
  "name": "Travis Fischer",
  "tagline": "Software Engineer | DevOps Enthusiast",
  "photo": "https://cdn.hashnode.com/res/hashnode/image/upload/v1611804366165/8HABHpGZc.jpeg",
  "num_followers": 14,
  "num_following": 13,
  "num_posts": 3,
  "num_reactions": 70
}
~~~

### GET /users/{username}/articles

Retrieves a list of articles written by a Hashnode user.

Example response:

```
[
  {
    "title": "Building a Simple Blog with FastAPI and SQLite",
    "slug": "building-a-simple-blog-with-fastapi-and-sqlite",
    "cover_image": "https://cdn.hashnode.com/res/hashnode/image/upload/v1611877673504/LDvwVqrLn.png",
    "brief": "Learn how to build a simple blog with FastAPI and SQLite.",
    "date": "2021-01-28T20:00:00.000Z",
    "num_reactions": 25
  },
  {
    "title": "Deploying FastAPI Apps with Docker and Traefik",
    "slug": "deploying-fastapi-apps-with-docker-and-traefik",
    "cover_image": "https://cdn.hashnode.com/res/hashnode/image/upload/v1613234280390/hgGnDhJr2.png",
    "brief": "Learn how to deploy FastAPI apps with Docker and Traefik.",
    "date": "2021-02-13T20:00:00.000Z",
    "num_reactions": 18
  }
]
```

## License

This project is licensed under the terms of the MIT license. See LICENSE for more information.