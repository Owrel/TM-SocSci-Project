import re

def getUserNameFromURL(url : str):
    """
        Description :
        -----------
        Get the username of a twitter user from the url

        Attribute :
        -----------
        url : str
            url of the twitter user

        Return :
        -----------
        str 
            url's username
    """
    x = re.split("^https?://(www\.)?twitter\.com/(#!/)?([^/]+)(/\w+)*$", url)
    return x[3]