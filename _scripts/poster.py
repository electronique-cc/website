import os
import time
from utils import opener, tagger

def recursive_block(content, block, source_dir, template_dir, extensions, language="en"):
    recursive_template = opener(f"{template_dir}/post_block.html")
    content2replace = ""
    posts = []
    for root, dirs, files in os.walk(source_dir):
        dirs[:] = [d for d in dirs if not d.startswith("_")]
        for file_name in files:
            if os.path.splitext(file_name)[1] in extensions:
                tags = tagger(opener(os.path.join(root, file_name)))
                if "static" not in tags or tags["static"] != "true" or "type" not in tags or tags["type"] != "post" or "lang" not in tags or tags["lang"] != language:
                    continue
                title = tags["title"] if "title" in tags else os.path.splitext(file_name)[0]
                unformatted_modified_date = tags["unformat-date"] if "unformat-date" in tags else time.strftime("%Y.%m.%d", time.gmtime(os.path.getmtime(os.path.join(root, file_name))))
                modified_date = time.strftime("%d %B %Y", time.gmtime(os.path.getmtime(os.path.join(root, file_name)))) if not "date" in tags else tags["date"]
                link = os.path.join(root, file_name).replace("\\", "/")[len(source_dir):]
                for ext in extensions:
                    if link.endswith(ext):
                        link = link.replace(ext, ".html")
                #post-categories are in the form of "category1, category2,category3" so we need to split them by "," and then remove the spaces and then convert them to a string with ", " as separator
                categories = ", ".join([category.strip() for category in tags["categories"].split(",")]) if "categories" in tags else ""
                categories = categories.upper()
                posts.append({"title": title, "unformatted_modified_date": unformatted_modified_date, "modified_date": modified_date, "link": link, "categories": categories, "author": tags["author"] if "author" in tags else "", "description": tags["description"] if "description" in tags else "", "image": tags["image"] if "image" in tags else ""})
    # Sort the posts by modified_date (most recent first)
    posts.sort(key=lambda post: post["unformatted_modified_date"], reverse=True)
    for post in posts:
        content2replace += recursive_template.replace("<!-- post-title -->", post["title"]).replace("<!-- post-date -->", post["modified_date"]).replace("<!-- post-url -->", post["link"]).replace("<!-- post-author -->", post["author"]).replace("<!-- post-description -->", post["description"]).replace("<!-- post-image -->", post["image"]).replace("<!-- read-more -->", "Read more" if language == "en" else "Lire la suite").replace("<!-- post-categories -->", post["categories"])
    block = f"<!-- FOR {block} -->"
    content = content.replace(block, content2replace)
    return content
