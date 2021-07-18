import os

def check_path(root: str, query_path: str):
    """Check if it's safe or allowed to access a given path. Raise an exception 
    if not allowed

    Args:
        root: The route directory allowed for access. Any paths above this will
            throw an exception
        query_path: the path to check
    """
    root_realpath = os.path.realpath(root)
    query_realpath = os.path.realpath(query_path)

    if not query_realpath.startswith(root_realpath):
        raise ValueError(f"Access not allowed to path: {query_path}")