"""
User account definition and convenience functions for Sleepy Follow.
"""
import base64
import hashlib


class UserAccount:
    """
    User account for Sleepy Follow.

    Attributes:
        username: A string representing the user's username.
        posts: A list of tuples representing the user's posts.
    """

    def __init__(self, username):
        """
        Create a new user account.

        Args:
            username: A string representing the new user's username.
        """
        self.username = username
        self.posts = []

    def get_post(self, post_id):
        """
        Find a user's post by the post ID.

        Args:
            post_id: A string representing the post ID.

        Returns:
            A tuple of two strings (the post ID and the post text) if the user
            has a post with the ID, and None otherwise.
        """
        for post in self.posts:
            if post[0] == post_id:
                return post
        return None

    def generate_new_post_id(self):
        """
        Generate a post ID for the user's next post.

        Returns:
            A string representing the user's next post ID.
        """
        hash_func = hashlib.sha256()
        hash_func.update(self.username.encode("utf-8"))
        hash_func.update(len(self.posts).to_bytes(4, byteorder="big"))
        encoded_hash = base64.urlsafe_b64encode(hash_func.digest())
        return encoded_hash[:-1].decode("utf-8")

    def post(self, text):
        """
        Add a new post to the user's history.

        Args:
            text: A string representing the post text.
        """
        post_id = self.generate_new_post_id()
        new_post = (post_id, text)
        self.posts.append(new_post)
