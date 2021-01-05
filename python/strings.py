def dedup_spaces(the_string: str) -> str:
    """Return a string with any duplicate whitespaces compressed to a
    single one, and leading and trailing whitespace removed
    
    Args:
        the_string: string to deduplicate

    Returns:
        the deduplicated string
    """
    return ' '.join(the_string.split())