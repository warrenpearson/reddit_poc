import os

import praw


class RedditClient:
    def __init__(self):
        user_agent = "unix:otis:v0.1"
        client_id = os.environ['REDDIT_CLIENT_ID']
        client_secret = os.environ['REDDIT_CLIENT_SECRET']

        self._client = praw.Reddit(client_id=client_id,
                                   client_secret=client_secret,
                                   user_agent=user_agent
                                   )

    def quick_start(self):
        # self.get_hot("wallstreetbets")
        # self.get_details("wallstreetbets")
        self.get_submission("kmhp1p")

    def get_hot(self, subreddit, limit=5):
        for submission in self._client.subreddit(subreddit).hot(limit=limit):
            print(submission.title)

    def get_details(self, subreddit):
        subreddit = self._client.subreddit(subreddit)
        print(subreddit.description)

    def get_submission(self, sub_id):
        submission = self._client.submission(id=sub_id)
        for top_level_comment in submission.comments:
            print(top_level_comment.body)
            print("--------------")


if __name__ == "__main__":
    RedditClient().quick_start()
