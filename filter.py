import praw
import prawcore
import time
from datetime import datetime, timedelta


# Initialize the Reddit instance
reddit = praw.Reddit(
    client_id={CLIENT ID},
    client_secret={CLIENT SECRET},
    user_agent="{WHAT YOU'RE DOING} by /u/{USERNAME}",
)

# Insert your subreddits here
subreddits_list = ["Subreddit","Subreddit"]

active_subreddits = []

# Get the timestamp for 1 month ago
one_month_ago = datetime.utcnow() - timedelta(days=30)

for subreddit_name in subreddits_list:
    try:
        subreddit = reddit.subreddit(subreddit_name)

        # Get the top 100 posts from the last month
        recent_posts = list(subreddit.top(time_filter='month', limit=100))

        # If there are 20 or more posts from the last month, add to the active list
        if len(recent_posts) >= 20:
            active_subreddits.append(subreddit_name)

        # Optional: Add delay to avoid hitting rate limits
        time.sleep(1)
    except prawcore.exceptions.Forbidden:
        print(f"Access forbidden for subreddit: {subreddit_name}")


print(active_subreddits)
