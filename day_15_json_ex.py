import json
from pprint import pprint

# task 1
# posts_summary.json

with open("./blog_post.json", "r") as file:
    blog_data = json.load(file)
    print(blog_data, type(blog_data))


def post_summary():
    blog_posts_summary = [
        {posts: post for posts, post in post.items() if posts != "comments"}
        for post in blog_data["posts"]
    ]
    return blog_posts_summary


with open("posts_summary.json", "w") as file:
    extracted_posts = post_summary()
    json.dump({"posts": extracted_posts}, file, indent=4)

pprint(post_summary())
