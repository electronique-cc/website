import os
import time
from utils import opener, tagger

def recursive_block(content, block, source_dir, template_dir, extensions, language="en"):
    recursive_template = opener(f"{template_dir}/post_block.html")
    content2replace = ""
    for root, dirs, files in os.walk(source_dir):
        dirs[:] = [d for d in dirs if not d.startswith("_")]
        for file_name in files:
            if os.path.splitext(file_name)[1] in extensions:
                tags = tagger(opener(os.path.join(root, file_name)))
                if "static" not in tags or tags["static"] != "true" or "type" not in tags or tags["type"] != "post" or "lang" not in tags or tags["lang"] != language:
                    continue
                title = tags["title"] if "title" in tags else os.path.splitext(file_name)[0]
                modified_date = tags["date"] if "date" in tags else time.strftime("%d %B %Y", time.gmtime(os.path.getmtime(os.path.join(root, file_name))))
                link = os.path.join(root, file_name).replace("\\", "/")[len(source_dir):]
                for ext in extensions:
                    if link.endswith(ext):
                        link = link.replace(ext, ".html")
                print(link)
                #post-categories are in the form of "category1, category2,category3" so we need to split them by "," and then remove the spaces and then convert them to a string with ", " as separator
                categories = ", ".join([category.strip() for category in tags["categories"].split(",")]) if "categories" in tags else ""
                categories = categories.upper()
                content2replace += recursive_template.replace("<!-- post-title -->", title).replace("<!-- post-date -->", modified_date).replace("<!-- post-url -->", link).replace("<!-- post-author -->", tags["author"] if "author" in tags else "").replace("<!-- post-description -->", tags["description"] if "description" in tags else "").replace("<!-- post-image -->", tags["image"] if "image" in tags else "").replace("<!-- read-more -->", "Read more" if language == "en" else "Lire la suite").replace("<!-- post-categories -->", categories)
    block = f"<!-- FOR {block} -->"
    content = content.replace(block, content2replace)
    return content