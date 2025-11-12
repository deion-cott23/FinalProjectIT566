"""Entry point for the Students Language Application."""

import json
from argparse import ArgumentParser
from student_languages.persistence_layer.mysql_persistence_wrapper \
	import MySQLPersistenceWrapper
from student_languages.presentation_layer.user_interface import UserInterface



def main():
	"""Entry point."""
	args = configure_and_parse_commandline_arguments()

	if args.configfile:
		config = None
		with open(args.configfile, 'r') as f:
			config = json.loads(f.read())
			print(config)

		db = MySQLPersistenceWrapper(config)

	"ui = UserInterface(config)"
	"ui.start()"
			
		


def configure_and_parse_commandline_arguments():
	"""Configure and parse command-line arguments."""
	parser = ArgumentParser(
	prog='main.py',
	description='Start the Student Languages Application with a configuration file.',
	epilog='POC: Deion Cottingham | ddcottingham@gmail.com')

	parser.add_argument('-c','--configfile',
					help="Configuration file to load.",
					required=True)
	args = parser.parse_args()
	return args



if __name__ == "__main__":
	main()