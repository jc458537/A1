__author__ ='Bhoomi'

# Initialize the constants

def main():
		print("Reading List 1.0 - by Bhoomi Raval")
		book_list = []
		load_book(book_list)
		display_menu()

		choice = input(">>>").upper()

		while choice != 'Q':
			if choice == 'R':
				list_required_books(book_list)
			elif choice == 'C':
				list_completed_books(book_list)
			elif choice == 'A':
				add_new_books(book_list)
			elif choice =='M':
				mark_book_completed(book_list)
			else:
			print('please enter R, C, A, M or Q(uit)')

		display_menu()
		choice = input('>>> ').upper()
		print('Have a nice day :)')

	# end of main()

def display_menu():
	print('Menu:')
	print("R - List required books")
	print("C - List completed books")
	print("A - Add new book")
	print("M - Mark a book as completed")
	print("Q - Quit")

def load_book(book_list):


	"""

	"""
	print("load books")

	#end of load_books()

def list_required_books(book_list):
	print('list_required_books')
def list_completed_books(book_list):
	print('list_completed_books')
def list_new_books(book_list):
	print('list_new_books')
def mark_book_completed(book_list):
	print('mark_book_completed')


def complete_a_book():
	"""

	"""
	print("complete a book")

# end of complete_a_book()

# Start the program
main()