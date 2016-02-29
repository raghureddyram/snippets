import logging
import argparse
import psycopg2

logging.basicConfig(filename="snippets.log", level=logging.DEBUG)
logging.debug("Connecting to PostgreSQL")
connection = psycopg2.connect(database="snippets")
logging.debug("Database connection established.")

def put(name, snippet):
    """Store a snippet with an associated name."""
    logging.info("Storing snippet {!r}: {!r}".format(name, snippet))
    cursor = connection.cursor()
    command = 'INSERT into snippets values (%s, %s);'
    cursor.execute(command, (name, snippet))
    connection.commit()
    logging.debug("Snippet stored successfully.")
    return name, snippet

def get(name):
	"""Retrieve the snippet with a given name.

	If there is no such snippet, return '404: Snippet Not Found'.

	Returns the snippet.
	"""
	logging.error("FIXME: Unimplemented - get({!r})".format(name))
	return ""

def main():
    """Main function"""
    logging.info("Constructing parser")
    parser = argparse.ArgumentParser(description="Store and retrieve Snippets of text")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Subparser for the put command
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="Name of the snippet")
    put_parser.add_argument("snippet", help="Snippet text")
    get_parser = subparsers.add_parser("get", help="Retrieve a snippet")
    get_parser.add_argument("name", help="Name of the snippet")
    arguments = parser.parse_args()
    # Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments) ## how to use vars? vars() or vars()[].. seen both

    ## is vars(name="list", snippet="A sequence of things - created using []") syntactic sugar for a dictionary created from optional args?
    command = arguments.pop("command")

    if command == "put":
    	name, snippet = put(**arguments)
    	print("Stored {!r} as {!r}".format(snippet, name))
    elif command == "get":
    	snippet = get(**arguments) ## what's the diff between * vs **?
    	print("Retrieved snippet: {!r}".format(snippet))

if __name__ == "__main__":
	main()
