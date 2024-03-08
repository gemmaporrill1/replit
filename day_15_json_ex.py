import json

# task 1
# posts_summary.json

with open("./blog_post.json", "r") as file:
    blog_data = json.load(file)
    print(blog_data, type(blog_data))

def extraction():
    for post in blog_data:
        



# with open("posts_summary.json", "w") as file:
#     json.dump(blog_posts, file, indent=3)