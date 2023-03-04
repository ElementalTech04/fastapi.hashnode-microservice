import json
from os import environ

from dotenv import load_dotenv
from fastapi import FastAPI
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from redis import Redis

load_dotenv()

app = FastAPI()
redis = Redis(host=environ.get("REDIS_CONN_HOST"), port=environ.get("REDIS_CONN_PORT"),
              password=environ.get("REDIS_CONN_PW"))

# GraphQL API endpoint
transport = RequestsHTTPTransport(
    url=environ.get("HASHNODE_API_URL"),
    headers={'Authorization': 'Bearer ' + environ.get("HASHNODE_API_KEY")},
    use_json=True
)
client = Client(transport=transport, fetch_schema_from_transport=True)


@app.get('/getPostsByTag/{tag}/{pageNum}')
def get_posts_by_tag(tag: str, pageNum: int):
    # Check Redis cache for tag
    cached_data = redis.get(tag)
    if cached_data:
        return json.loads(cached_data.decode("UTF-8"))

    # Query GraphQL API for user posts by page
    posts_by_user_query = gql('''
        query GetPosts($pageNum: Int!) { 
            user(username: "travistech04") { 
              publication { 
                posts(page: $pageNum) { 
                  title 
                  coverImage 
                  dateAdded 
                  totalReactions 
                  brief 
                  slug 
                } 
              } 
            } 
          }
    ''')
    posts_by_user_params = {'pageNum': pageNum}
    posts_by_user_result = client.execute(posts_by_user_query, variable_values=posts_by_user_params)
    print(posts_by_user_result['user']['publication']['posts'])
    posts_by_user_arr = posts_by_user_result['user']['publication']['posts']
    resulting_posts = []

    # Query GraphQL API for each post to see tags
    for post in posts_by_user_arr:
        single_post_query = gql('''
               query GetPosts($slug: String!) {
                  post(slug: $slug, hostname:"blog.travistheprogrammer.com"){
                    title,
                    slug,
                    cuid,
                    brief,
                    dateAdded,
                    totalReactions,
                    coverImage,
                    tags{
                      name
                    }
                  }
                }
            ''')
        single_post_params = {'slug': post['slug']}
        single_post_result = client.execute(single_post_query, variable_values=single_post_params)
        print(single_post_result)
        single_post_tags = single_post_result['post']['tags']
        for single_post_tag in single_post_tags:
            if tag in single_post_tag['name']:
                resulting_posts.append(single_post_result)
                break
        print(resulting_posts)

    # Cache result for future requests
    redis.set(tag, json.dumps(resulting_posts))

    return resulting_posts


@app.delete('/purge/{tag}')
def purge_cache_by_tag(tag: str):
    redis.delete(tag)
    return {'message': 'Cache purged successfully.'}
