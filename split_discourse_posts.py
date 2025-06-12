import json
import os
from collections import defaultdict

INPUT_FILE = "discourse_posts.json"
OUTPUT_DIR = "downloaded_threads"

# Create the output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load the original JSON
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    all_posts = json.load(f)

# Group posts by topic_id
topics = defaultdict(list)
titles = {}

for post in all_posts:
    topic_id = post["topic_id"]
    topics[topic_id].append(post)
    titles[topic_id] = post.get("topic_title", "")

# Save each topic's posts into a separate JSON file
for topic_id, posts in topics.items():
    filename = os.path.join(OUTPUT_DIR, f"{topic_id}.json")
    data = {
        "id": topic_id,
        "title": titles[topic_id],
        "slug": titles[topic_id].lower().replace(" ", "-").replace("/", "-"),
        "post_stream": {
            "posts": posts
        }
    }
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
print(f"✅ Done! Saved {len(topics)} topic files in '{OUTPUT_DIR}'")
