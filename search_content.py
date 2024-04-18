import praw

# Initialize the Reddit instance
reddit = praw.Reddit(
    client_id={CLIENT ID},
    client_secret="{CLIENT SECRET},
    user_agent="{WHAT YOU'RE DOING} by /u/{USERNAME}",
)

# Drop in your list of keywords
keywords = [ "keyword", "keyword"
]

# Function to get top posts from a subreddit and assess relevance
def get_relevant_top_posts(subreddit_name, keywords, time_period='week', limit=10):
    subreddit = reddit.subreddit(subreddit_name)
    relevant_posts = []
    for post in subreddit.top(time_filter=time_period, limit=limit):
        # Check if any of the keywords are in the post title or selftext
        if any(keyword.lower() in (post.title + " " + post.selftext).lower() for keyword in keywords):
            relevant_posts.append((post.title, post.selftext, post.score))
    return relevant_posts

# Function to search subreddits and filter by relevance and activity
def search_and_filter_subreddits(keywords, time_period='month', post_limit=10, subreddit_limit=5, score_threshold=10):
    relevant_subreddits = set()
    for keyword in keywords:
        for submission in reddit.subreddit('all').search(keyword, time_filter=time_period, limit=post_limit):
            subreddit_name = submission.subreddit.display_name
            # Fetch top posts and assess relevance
            top_posts = get_relevant_top_posts(subreddit_name, keywords, time_period, limit=subreddit_limit)
            # If there are relevant posts and the top post has a score above the threshold, add to the list
            if top_posts and top_posts[0][2] > score_threshold:
                relevant_subreddits.add(subreddit_name)
    return relevant_subreddits

# Usage of the refined function
relevant_subreddits = search_and_filter_subreddits(keywords)

# Print the list of relevant subreddits formatted as r/subreddit
for subreddit in relevant_subreddits:
    print(f"r/{subreddit}")
