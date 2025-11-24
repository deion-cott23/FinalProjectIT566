"""Entry point for the Students Language Application."""

import json
from argparse import ArgumentParser
from student_languages.persistence_layer.mysql_persistence_wrapper \
	import MySQLPersistenceWrapper
from student_languages.service_layer.app_services import AppServices
from student_languages.presentation_layer.user_interface import UserInterface
from student_languages.presentation_layer.console_ui import ConsoleUI



def main():
	"""Entry point."""
	args = configure_and_parse_commandline_arguments()

	if args.configfile:
		config = None
		with open(args.configfile, 'r') as f:
			config = json.loads(f.read())
		
		ui = ConsoleUI(config)
		ui.start()
		
		service_layer = AppServices(config)
		students_list = service_layer.get_all_students_as_json()
		instructors_list = service_layer.get_all_instructors_as_json()
		print(students_list)
		print(instructors_list)
		


		""" db = MySQLPersistenceWrapper(config)
		students_list = db.select_all_students()
		for student in students_list:
			print(f'{student}')


		print('*' * 80)
		students_list = db.select_all_students_with_languages()
		for student in students_list:
			print(f'{student}')


		print('*' * 80)
		students_list = db.select_all_students()
		for student in students_list:
			print(f'{student[1]} {student[4]}')
			update_list = db.select_students_status_from_student_id(student[0])
			for student_update in update_list:
				update_string = f'\t{student_update[0]} {student_update[1]} {student_update[2]} '
				print(update_string)


	ui = UserInterface(config)
	ui.start() """
			
		


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