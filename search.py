import praw

# Initialize the Reddit instance
reddit = praw.Reddit(
    client_id={CLIENT ID},
    client_secret={CLIENT SECRET}},
    user_agent="{WHAT YOU'RE DOING} by /u/{USERNAME}",
)

# Search for subreddits related to personal finance and spend tracking
topics = ["topic", "topic", "topic"]
subreddits = []

for topic in topics:
    # Searching for subreddits directly
    for subreddit in reddit.subreddits.search(topic, limit=100):
        subreddits.append(subreddit.display_name)

# Remove duplicates
subreddits = list(set(subreddits))

# Print the list of subreddits
for subreddit in subreddits:
    print(subreddit)
