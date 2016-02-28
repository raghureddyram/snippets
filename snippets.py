import logging

logging.basicConfig(filename="snippets.log", level=logging.DEBUG)


def put(name, snipppet):
	"""
	Store a snippet with an associated name.

    Returns the name and the snippet.
    """
    logging.error("FIXME: Uninmplemented - put({!r}, {!r})".format(name, snippet))
    return name, snippet

def get(name, snippet):
	"""Retrieve the snippet with a given name.

    If there is no such snippet, return '404: Snippet Not Found'.

    Returns the snippet.
    """
    logging.error("FIXME: Unimplemented - get({!r})".format(name))
    return ""