# -*- coding: utf-8 -*-

"""
Linux (Ubuntu) Installation Instructions:
Linux comes preinstalled with Python, so just execute the command below:

sudo apt install -y xclip libncurses5-dev python-pip && pip install --upgrade pip && pip install readline pynput convertdate clipboard backports.shutil_get_terminal_size

python '/home/user/path/to/multi_tool.py'

---------------------------------------------------

Windows Installation Instructions:
Download and install Python: https://www.python.org/downloads/release/python-2717/

Go to "Edit the system environment variables" in Windows and then click "Environment Variables..."

Select "Path" from System variables and click "Edit..."

Make sure there is a semi-colon on the end of the "Variable value" field, then add "C:\Python27;C:\Python27\Scripts" to it (without quotes). If your folder is not named Python27, change it to what your folder is named.

RESTART your system. You will now be able to call Python from the Command Prompt.

pip install pynput convertdate clipboard backports.shutil_get_terminal_size

python "C:\Path\to\multi_tool.py"
"""

#-----------------
# General Imports

try:
	import readline
except ImportError:
	pass

from pynput.keyboard import Key, Controller, Listener
from threading import Thread
import sys

#-----------------
# Imports for date tool

from convertdate import hebrew, mayan, coptic
import datetime as dt

#-----------------
# Imports for number tool

from bisect import bisect_left
import math
import itertools

#-----------------
# Imports for Library

import textwrap
from backports.shutil_get_terminal_size import get_terminal_size

#-----------------
# Imports for gematria tool

import clipboard
import unicodedata

#-----------------------------------------------------------------------
# Introduction

print('\nWelcome to the Date/Number/Gematria Analyzer Research Tool!')

print('        ___  ___  ___  ___ ')
print('       (__ )(__ )(__ )| __)')
print('By      (_ \\ (_ \\ / / |__ \\')
print('       (___/(___/(_/  (___/\n')

print('https://theprophetictimeline.com/\n')

print('How to use:\n')

print('Dates:')
print('     Enter a date in the format "month day year" using spaces like so: 10 28 2017')
print('     Calculate the number of days between two dates like this:         10 28 2017 -> 1 29 2021')
print('     Subtract a certain amount of days from a date:                    7 20 2019 - 25999')
print('     Add a certain amount of days to a date:                           12 21 2012 + 2442\n')

print('     When the +, -, or -> function is used, the date on the left side of the screen is assigned')
print('     to a variable called "a", and the date on the right side becomes "b" ... The letter a or b')
print('     can be substituted for a date:\n')

print('     a -> b ....... b - 25999 ....... 11 12 1997 -> a\n')

print('Numbers:')
print('     Input a lone integer to analyze its properties:          42')
print('     After analyzing a number, hit the Right-Shift key to view its next occurrence in Pi')
print('     If info is available for your inputted number, view it like this: ..42\n')

print('     Input an expression to do simple calculations:           1.375 * 1.375')
print('     Add a decimal point to your numbers when doing division: 24576 / 2457.0\n')

print('Fast Pi Search:')
print('     Input a number like so to view its various occurrences in Pi: //2424')
print('     Type anything and press Enter to end search\n')

print('Gematria:')
print('     Input a text message to view the values of the letters, words, and message total')
print('     Hit the Right-Ctrl key to view the Gematria of the text in the Clipboard. This is useful for multi-line messages')
print('     The ciphers used are English Ordinal, Full Reduction, Reverse Ordinal, Reverse Full Reduction')
print('     The fifth gematria value is the sum of all four previous values')
print('     The Gematria and Isopsephy of Hebrew and Greek text can also be viewed\n')

print('Constants:')
print('     To change the Constant you would like to use, type one of the following codes (example: em):  Pi (pi), Phi (phi), e (e), Euler-Mascheroni Constant (em), 2Pi (2pi), Glaisher-Kinkelin Constant (A), Catalan Constant (cat), Khinchin-Levy Constant (kl), Square root of 2 (rt)')

#-----------------------------------------------------------------------
# Number tool

print('\n---------------------------------------------------\n')

the_constant = ''
constant_choice = 'Pi'
constant_sample_len = 55		# How many sample digits to get before and after our number

pi = ''
phi = ''
e = ''
em = ''
pi2 = ''
GK = ''
cat = ''
KL = ''
sqrt2 = ''

def choose_number(choice):
	global the_constant, constant_choice

	if choice == 'Pi':
		the_constant = pi
		constant_choice = 'Pi'
	if choice == 'Phi':
		the_constant = phi
		constant_choice = 'Phi'
	if choice == 'e':
		the_constant = e
		constant_choice = 'e'
	if choice == 'em':
		the_constant = em
		constant_choice = 'em'
	if choice == '2Pi':
		the_constant = pi2
		constant_choice = '2Pi'
	if choice == 'A':
		the_constant = GK
		constant_choice = 'A'
	if choice == 'cat':
		the_constant = cat
		constant_choice = 'cat'
	if choice == 'KL':
		the_constant = KL
		constant_choice = 'KL'
	if choice == 'rt':
		the_constant = sqrt2
		constant_choice = 'Sqrt 2'

def find_nth_occurrence_in_pi(num, n):
	position = the_constant.find(num)
	if position == -1:
		return -1
	while position >= 0 and n > 1:
		position = the_constant.find(num, position + len(num))
		if position == -1:
			return -1
		n -= 1
	return position

def search_in_pi(num, occurrence_count):
	int_num = int(num)
	num = str(num)
	num_no_leading_zeros = num.lstrip('0')
	pos = find_nth_occurrence_in_pi(num, occurrence_count)
	max_number_digits = len(the_constant) 

	info_string = ''

	if pos != -1:
		front_var = 0
		back_var = 0

		if pos >= constant_sample_len:
			front_var = pos - constant_sample_len

		if pos > max_number_digits - constant_sample_len:
			back_var = max_number_digits
		else:
			back_var = pos + constant_sample_len + len(num)

		sample = the_constant[front_var:back_var]
		endof = pos + len(num)

		front_amount = endof - front_var - len(num)		# Usually equals constant_sample_len
		sample_front = sample[:front_amount]
		end_amount = len(sample) - len(sample_front) - len(num)
		sample_end = sample[-end_amount:]

		if endof == max_number_digits:
			sample_end = ''

		sample_string = sample_front + ' ' + num + ' ' + sample_end
		sample_string = sample_string.strip()

		occurrence_string = ' occurrence #' + str(occurrence_count)

		if occurrence_count == 1:
			occurrence_string = ' first'

		info_string = num + occurrence_string + ' appears in ' + constant_choice + ' at the end of ' + str(endof) + ' digits (Position ' + str(endof + 1) + ') :\n' + sample_string + '\n'
	else:
		info_string = 'This number does not occur within the first ' + str(max_number_digits) + ' digits of ' + constant_choice + '.\n'

	if int_num <= max_number_digits and int_num != 0:
		selection = the_constant[:int_num]

		if len(selection) > constant_sample_len:
			selection = selection[-constant_sample_len:]		# Only get last n digits of string

		selection2 = selection + ' ' + the_constant[int_num : int_num + constant_sample_len]

		info_string2 = '\nWhat occurs at the end of ' + num_no_leading_zeros + ' digits of ' + constant_choice + ' : \n' + selection2
		info_string2 += '\n' + (' ' * (selection2.find(' '))) + '^'

		info_string += info_string2

	if info_string.endswith('\n') and not (int_num == 0 and occurrence_count > 1):
		info_string = info_string[:-1]

	return info_string

def find_multiple_pi(num):
	pi_info = search_in_pi(num, 1)

	if num == '0': pi_info += '\n'
	print('\n\n' + pi_info)

	pi_search_input = ''
	occurrence_count = 2

	pi_search_input = raw_input('')

	while pi_search_input == '':

		pi_info = search_in_pi(num, occurrence_count)

		if 'does not occur' in pi_info:
			return

		print(pi_info)

		pi_search_input = raw_input('')
		occurrence_count += 1

def digit_sum_pi(num):
	count = 0
	digit_sum = 0
	found = False
	zeros = 0

	for digit in the_constant:
		if found:
			if digit == '0':
				zeros += 1
				continue
			else:
				break

		digit = int(digit)
		digit_sum += digit
		count += 1

		if digit_sum == num:
			found = True
			continue
		if digit_sum > num:
			count = 0
			break

		if count == len(the_constant) and digit_sum != num:
			count = 0

	count2 = 0
	sum2 = 0

	for digit in the_constant:
		digit = int(digit)
		sum2 += digit
		count2 += 1

		if count2 == num:
			break

		if count2 == len(the_constant) and count2 != num:
			count2 = 0

	result_string = ''

	if count != 0:
		result_string += str(count)
		if zeros != 0:
			result_string += ' (up to ' + str(count + zeros) + ')'

		result_string += ' digits of ' + constant_choice + ' sum to ' + str(digit_sum) + ' ... '

	if count2 != 0:
		result_string += str(num) + ' digits of ' + constant_choice + ' sum to ' + str(sum2)

	return result_string

def is_perfect_cube(num):
	num = abs(num)
	cube_root = int(round(num ** (1. / 3)))
	if cube_root ** 3 == num:
		return cube_root
	return False

def isPerfect(num, divisors):
	divisors = divisors[:-1]				# All divisors except the number itself
	if sum(divisors) == num:
		return True
	return False

def isRegular(num, factorization):
	if num == 1:
		return True
	for i in factorization:
		if i != 2 and i != 3 and i != 5:	# The factorization of regular numbers only contain 2s, 3s, 5s
			return False
	return True

def isFactorial(num):
	i = f = 1
	while f < num:
		i += 1
		f *= i
	return f == num

def isPerfectSquare(num):
	s = int(math.sqrt(num))
	return s * s == num

def isFibonacci(num):
	return isPerfectSquare(5 * num * num + 4) or isPerfectSquare(5 * num * num - 4)

def divisorGenerator(n):
	large_divisors = []
	for i in xrange(1, int(math.sqrt(n) + 1)):
		if n % i == 0:
			yield i
			if i * i != n:
				large_divisors.append(n / i)
	for divisor in reversed(large_divisors):
		yield divisor

def prime_factors(n):
	i = 2
	factors = []
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
			factors.append(i)
	if n > 1:
		factors.append(n)
	return factors

def prime_list(n):
	sieve = [True] * n
	for i in xrange(3, int(n ** 0.5) + 1, 2):
		if sieve[i]:
			sieve[i * i::2 * i]=[False]*((n - i * i - 1) / (2 * i) + 1)
	return [2] + [i for i in xrange(3, n, 2) if sieve[i]]

def base10toN(num, base):
	converted_string, modstring = '', ''
	currentnum = num
	if not 1 < base < 37:
		raise ValueError('Base must be between 2 and 36')
	if not num:
		return '0'
	while currentnum:
		mod = currentnum % base
		currentnum = currentnum // base
		converted_string = chr(48 + mod + 7 * (mod > 10)) + converted_string
	return converted_string

def format(line1, line2):
	length = 45
	return line1 + ((length - len(line1)) * ' ') + line2

print('Generating 9,999,999 prime numbers... (Takes about 10 seconds)\n')

biggest_prime = 179424691 # The 10,000,001st prime
second_to_biggest_prime = 179424673
list_of_primes = prime_list(biggest_prime)

print('---------------------------------------------------\n')
print('Program loaded. To exit, type the word exit and hit enter.\n')
print('---------------------------------------------------')

def take_closest(the_list, num):
	pos = bisect_left(the_list, num)

	if pos == 0:
		return the_list[0]
	if pos == len(the_list):
		return the_list[-1]

	before = the_list[pos - 1]
	after = the_list[pos]

	if after - num < num - before:
		return after
	else:
		return before

def prime_info(num):
	if num == 1:
		return 0, 2, 'None', 2		# 2 is the first prime, No previous prime, next prime is 2
	if num == 2:
		return 1, 3, 'None', 3

	number_of_prime = 0
	nth_prime_number = 0
	previous_prime = 0
	next_prime = 0

	if num > 9999999:
		nth_prime_number = 'Unavailable'
	else:
		nth_prime_number = list_of_primes[num - 1]

	if num < second_to_biggest_prime:	# The last prime before the biggest_prime

		if num in list_of_primes:
			number_of_prime = list_of_primes.index(num) + 1
			previous_prime = list_of_primes[number_of_prime - 2]
			next_prime = list_of_primes[number_of_prime]
		else:
			prime = take_closest(list_of_primes, num)

			if num > prime:
				previous_prime = prime
				index = list_of_primes.index(previous_prime) + 1
				next_prime = list_of_primes[index]
			else:
				next_prime = prime # Because the prime is greater than num
				index = list_of_primes.index(next_prime) - 1
				previous_prime = list_of_primes[index]
	else:
		previous_prime = 'Unavailable'
		next_prime = 'Unavailable'

	return number_of_prime, nth_prime_number, previous_prime, next_prime

#-----------------------------------------------------------------------
# Date tool

def get_jd(year, month, day, type = 'julian'):
	if month <= 2:
		year = year - 1
		month = month + 12

	a = int(year / 100)

	if type == 'gregorian':
		b = 2 - a + int(a / 4)
	else:
		b = 0

	jd = int(365.25 * (year + 4716)) + int(30.6001 * (month + 1)) + day + b -1524.5

	return jd

def split_up_date(date):
	month = int(date.split(' ', 1)[0])
	day = int(date.split(' ', 1)[1].split(' ', 1)[0])
	year = int(date.split(' ', 1)[1].split(' ', 1)[1])

	return year, month, day

def get_coptic_date_information(year, month, day):
	coptic_date = coptic.from_gregorian(year, month, day)

	coptic_year = coptic_date[0]
	coptic_month = coptic_date[1]
	coptic_day = coptic_date[2]

	first_day = coptic.to_gregorian(coptic_year, 1, 1)
	first_day_year = first_day[0]
	first_day_month = first_day[1]
	first_day_day = first_day[2]

	first_date = dt.date(first_day_year, first_day_month, first_day_day)
	second_date = dt.date(year, month, day)
	difference = (first_date - second_date).days

	if difference < 0:
		difference = difference * -1

	day_of_coptic_year = difference + 1

	return str(coptic_month) + '/' + str(coptic_day).replace('.0', '') + '/' + str(coptic_year), day_of_coptic_year

def get_hebrew_date_formatted(year, month, day):
	hebrew_date = hebrew.from_gregorian(year, month, day)

	hebrew_year = hebrew_date[0]
	hebrew_month = hebrew_date[1]
	hebrew_day = hebrew_date[2]

	return str(hebrew_month) + '/' + str(hebrew_day) + '/' + str(hebrew_year)

def get_day_of_hebrew_year(year, month, day):
	hebrew_date = hebrew.from_gregorian(year, month, day)
	hebrew_year = hebrew_date[0]
	hebrew_month = hebrew_date[1]

	first_day = hebrew.to_gregorian(hebrew_year, 7, 1)	# Returns first day of that Hebrew civil year
	first_day_year = first_day[0]
	first_day_month = first_day[1]
	first_day_day = first_day[2]

	first_date = dt.date(first_day_year, first_day_month, first_day_day)
	second_date = dt.date(year, month, day)
	difference = (first_date - second_date).days

	if difference < 0: difference = difference * -1
	day_of_civil_year = difference + 1

	# -----

	# Find out what day of the Hebrew Ecclesiastical year it is

	if hebrew_month > 6: hebrew_year = hebrew_year - 1

	first_day_e = hebrew.to_gregorian(hebrew_year, 1, 1)  # Returns 1st day of Hebrew Ecclesiastical year
	first_day_year_e = first_day_e[0]
	first_day_month_e = first_day_e[1]
	first_day_day_e = first_day_e[2]

	first_date_e = dt.date(first_day_year_e, first_day_month_e, first_day_day_e)
	second_date_e = dt.date(year, month, day)
	difference_e = (first_date_e - second_date_e).days

	if difference_e < 0: difference_e = difference_e * -1
	day_of_ecclesiastical_year = difference_e + 1

	return day_of_ecclesiastical_year, day_of_civil_year

def get_longcount(a):
	return str(a[0]) + '.' + str(a[1]) + '.' + str(a[2]) + '.' + str(a[3]) + '.' + str(a[4])

def get_tzolkin(julian_day):
	tzolkin = mayan.to_tzolkin(julian_day)											# Converts jd to tzolkin: (7, 'Chuwen')
	tzolkin_day_num = mayan._tzolkin_count(tzolkin[0], tzolkin[1])	# Converts (7, 'Chuwen') to day num: 111

	return tzolkin, tzolkin_day_num

def get_date_information(year, month, day):
	jd = get_jd(year, month, day)

	if jd >= 2299171.5:
		jd = get_jd(year, month, day, 'gregorian')

	a = mayan.from_jd(jd)
	julian_day = mayan.to_jd(a[0], a[1], a[2], a[3], a[4])		# Converts Mayan long count to "julian day"

	tzolkin, tzolkin_day_num = get_tzolkin(julian_day)
	long_count = get_longcount(a)

	gregorian_day_of_year = (dt.date(year, month, day) - dt.date(year, 1, 1)).days + 1

	hebrew_date_formatted = get_hebrew_date_formatted(year, month, day)
	day_of_ecclesiastical_year, day_of_civil_year = get_day_of_hebrew_year(year, month, day)

	coptic_date_formatted, day_of_coptic_year = get_coptic_date_information(year, month, day)

	return month, day, year, gregorian_day_of_year, long_count, tzolkin_day_num, tzolkin, hebrew_date_formatted, day_of_civil_year, day_of_ecclesiastical_year, coptic_date_formatted, day_of_coptic_year

def print_date_information(year, month, day, year2, month2, day2):
	month, day, year, gregorian_day_of_year, long_count, tzolkin_day_num, tzolkin, hebrew_date_formatted, day_of_civil_year, day_of_ecclesiastical_year, coptic_date_formatted, day_of_coptic_year = get_date_information(year, month, day)
	nice_date1 = str(month) + '/' + str(day) + '/' + str(year)

	line1 = 'Date:            ' + nice_date1 + ' (Day ' + str(gregorian_day_of_year) + ')'
	line2 = 'Long count:      ' + long_count
	line3 = "Tzolk'in day:    " + str(tzolkin_day_num) + ' ' + str(tzolkin).replace('"', '')
	line4 = 'Hebrew date:     ' + hebrew_date_formatted + ' (Day ' + str(day_of_civil_year) + ' C, ' + str(day_of_ecclesiastical_year) + ' E)'
	line5 = 'Coptic date:     ' + coptic_date_formatted + ' (Day ' + str(day_of_coptic_year) + ')'

	if year2 == None:
		print('\n')
		print(line1)
		print(line2)
		print(line3)
		print(line4)
		print(line5)

	else:
		month, day, year, gregorian_day_of_year, long_count, tzolkin_day_num, tzolkin, hebrew_date_formatted, day_of_civil_year, day_of_ecclesiastical_year, coptic_date_formatted, day_of_coptic_year = get_date_information(year2, month2, day2)
		nice_date2 = str(month) + '/' + str(day) + '/' + str(year)

		line1_2 = 'Date:            ' + nice_date2 + ' (Day ' + str(gregorian_day_of_year) + ')'
		line2_2 = 'Long count:      ' + long_count
		line3_2 = "Tzolk'in day:    " + str(tzolkin_day_num) + ' ' + str(tzolkin).replace('"', '')
		line4_2 = 'Hebrew date:     ' + hebrew_date_formatted + ' (Day ' + str(day_of_civil_year) + ' C, ' + str(day_of_ecclesiastical_year) + ' E)'
		line5_2 = 'Coptic date:     ' + coptic_date_formatted + ' (Day ' + str(day_of_coptic_year) + ')'

		n = 51

		print('\n')
		print(line1 + (n - len(line1)) * ' ' + '|       ' + line1_2)
		print(line2 + (n - len(line2)) * ' ' + '|       ' + line2_2)
		print(line3 + (n - len(line3) - 2) * ' ' + '[A|B]     ' + line3_2)
		print(line4 + (n - len(line4)) * ' ' + '|       ' + line4_2)
		print(line5 + (n - len(line5)) * ' ' + '|       ' + line5_2)

#-----------------------------------------------------------------------
# Gematria tool

def Gematria_print(wordnum, letternum, infostring, totalEO, totalFR, totalRO, totalRFR, all_total, EOletters, wordvals, letters, totalsimple, totalshort, totalreverse, totalkaye, totalHebrew, totalGreek):
	complete_letters = ''
	complete_numbers = ''

	for EOletters_word, letter_word, wordval in itertools.izip(EOletters, letters, wordvals):
		for EOletter, letter in zip(EOletters_word, letter_word):

			complete_letters += letter + ' '
			complete_numbers += str(EOletter) + ' '

			if len(EOletter) > 1:
				complete_letters += ' ' * (len(EOletter) - 1)

		the_wordval = '(' + str(wordval) + ')  '
		the_spaces = ' ' * len(the_wordval)

		complete_letters += ' ' + the_wordval
		complete_numbers += ' ' + the_spaces

	complete = '```\n' + complete_letters + '\n' + complete_numbers + '\n\n'

	if totalHebrew != None:
		complete += '(' + str(totalHebrew) + ')\n\n' + infostring + '\n```'
		return complete

	if totalGreek != None:
		complete += '(' + str(totalGreek) + ')\n\n' + infostring + '\n```'
		return complete

	all_totals = totalEO + totalFR + totalRO + totalRFR

	complete += '(' + str(totalEO) + ')     ' + '(' + str(totalFR) + ')     ' + '(' + str(totalRO) + ')     ' + '(' + str(totalRFR) + ')     |     (' + str(all_totals) + ')\n\n'
	complete += 'simple (' + str(totalsimple) + ')     ' + 'short (' + str(totalshort) + ')     ' + 'reverse (' + str(totalreverse) + ')     ' + 'kaye (' + str(totalkaye) + ')\n\n'

	complete += infostring + '\n'
	complete += '```'

	return complete

def Gematria(text):
	if type(text) == str: text = unicode(text, 'utf-8')

	iotas = u'ᾀᾁᾂᾃᾄᾅᾆᾇᾈᾉᾊᾋᾌᾍᾎᾏᾐᾑᾒᾓᾔᾕᾖᾗᾘᾙᾚᾛᾜᾝᾞᾟᾠᾡᾢᾣᾤᾥᾦᾧᾨᾩᾪᾫᾬᾭᾮᾯᾲᾳᾴᾷᾼῂῃῄῇῌῲῳῴῷῼ'
	for iota in iotas: text = text.replace(iota, iota + u'ι')
	text = text.strip().replace("'", '').replace(u'ʹ', '').replace(u'ʹ', '').replace(u'ſ', 's')
	text = ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn') # Remove accents

	if not any(c.isalpha() or c.isdigit() for c in text): return None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None

	s = ''

	for letter in text:
		if letter.isalpha() or letter.isdigit():
			s += letter
		else:
			if len(s) > 0:
				if s[-1] != ' ':
					s += ' '

	if s[-1] == ' ': s = s[:-1]

	words = s.split(' ')
	wordnum = len(words)
	letternum = sum(c.isalpha() for c in s)

	#-----------------

	valuesH = {u'א' : 1, u'ב' : 2, u'ג' : 3, u'ד' : 4, u'ה' : 5, u'ו' : 6, u'ז' : 7, u'ח' : 8, u'ט' : 9, u'י' : 10, u'כ' : 20, u'ך' : 20, u'ל' : 30, u'מ' : 40, u'ם' : 40, u'נ' : 50, u'ן' : 50, u'ס' : 60, u'ע' : 70, u'פ' : 80, u'ף' : 80, u'צ' : 90, u'ץ' : 90, u'ק' : 100, u'ר' : 200, u'ש' : 300, u'ת' : 400}
	valuesG = {u'Α' : 1, u'α' : 1, u'Β' : 2, u'β' : 2, u'Γ' : 3, u'γ' : 3, u'Δ' : 4, u'δ' : 4, u'Ε' : 5, u'ε' : 5, u'Ϛ' : 6, u'ϛ' : 6, u'Ζ' : 7, u'ζ' : 7, u'Η' : 8, u'η' : 8, u'Θ' : 9, u'θ' : 9, u'Ι' : 10, u'ι' : 10, u'Κ' : 20, u'κ' : 20, u'Λ' : 30, u'λ' : 30, u'Μ' : 40, u'μ' : 40, u'Ν' : 50, u'ν' : 50, u'Ξ' : 60, u'ξ' : 60, u'Ο' : 70, u'ο' : 70, u'Π' : 80, u'π' : 80, u'Ϙ' : 90, u'ϙ' : 90, u'Ρ' : 100, u'ρ' : 100, u'Σ' : 200, u'σ' : 200, u'ς' : 200, u'Τ' : 300, u'τ' : 300, u'Υ' : 400, u'υ' : 400, u'Φ' : 500, u'φ' : 500, u'Χ' : 600, u'χ' : 600, u'Ψ' : 700, u'ψ' : 700, u'Ω' : 800, u'ω' : 800, u'Ϡ' : 900, u'ϡ' : 900}

	allHebrew = True
	allGreek = True

	for letter in s.replace(' ', ''):
		if letter not in valuesH:
			allHebrew = False
			break

	for letter in s.replace(' ', ''):
		if letter not in valuesG:
			allGreek = False
			break

	#-----------------

	if allHebrew or allGreek:
		totalChoice = 0

		letters = []
		EOletters = []
		wordvals = []

		for word in words:
			wordval = 0
			EOletters_words = []
			letters_words = []

			if allHebrew:
				for letter in word:
					wordval += valuesH[letter]
					EOletters_words.append(str(valuesH[letter]))
					letters_words.append(letter)
					totalChoice+= valuesH[letter]
			else:
				for letter in word:
					wordval += valuesG[letter]
					EOletters_words.append(str(valuesG[letter]))
					letters_words.append(letter)
					totalChoice+= valuesG[letter]

			wordvals.append(wordval)
			letters.append(letters_words)
			EOletters.append(EOletters_words)

		infostring = '(' + str(letternum) + ' letters, ' + str(wordnum) + ' words)'

		if allHebrew:
			return wordnum, letternum, infostring, None, None, None, None, None, EOletters, wordvals, letters, None, None, None, None, totalChoice, None
		else:
			return wordnum, letternum, infostring, None, None, None, None, None, EOletters, wordvals, letters, None, None, None, None, None, totalChoice

	#-----------------

	valuesEO = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8, 'i' : 9, 'j' : 10, 'k' : 11, 'l' : 12, 'm' : 13, 'n' : 14, 'o' : 15, 'p' : 16, 'q' : 17, 'r' : 18, 's' : 19, 't' : 20, 'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24, 'y' : 25, 'z' : 26, '1' : 1,  '2' : 2,  '3' : 3,  '4' : 4,  '5' : 5,  '6' : 6,  '7' : 7,  '8' : 8,  '9' : 9,  '0' : 0}
	valuesFR = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8, 'i' : 9, 'j' : 1, 'k' : 2, 'l' : 3, 'm' : 4, 'n' : 5, 'o' : 6, 'p' : 7, 'q' : 8, 'r' : 9, 's' : 1, 't' : 2, 'u' : 3, 'v' : 4, 'w' : 5, 'x' : 6, 'y' : 7, 'z' : 8, '1' : 1,  '2' : 2,  '3' : 3,  '4' : 4,  '5' : 5,  '6' : 6,  '7' : 7,  '8' : 8,  '9' : 9,  '0' : 0}
	valuesRO = {'a' : 26, 'b' : 25, 'c' : 24, 'd' : 23, 'e' : 22, 'f' : 21, 'g' : 20, 'h' : 19, 'i' : 18, 'j' : 17, 'k' : 16, 'l' : 15, 'm' : 14, 'n' : 13, 'o' : 12, 'p' : 11, 'q' : 10, 'r' : 9, 's' : 8, 't' : 7, 'u' : 6, 'v' : 5, 'w' : 4, 'x' : 3, 'y' : 2, 'z' : 1, '1' : 1,  '2' : 2,  '3' : 3,  '4' : 4,  '5' : 5,  '6' : 6,  '7' : 7,  '8' : 8,  '9' : 9,  '0' : 0}
	valuesRFR = {'a' : 8, 'b' : 7, 'c' : 6, 'd' : 5, 'e' : 4, 'f' : 3, 'g' : 2, 'h' : 1, 'i' : 9, 'j' : 8, 'k' : 7, 'l' : 6, 'm' : 5, 'n' : 4, 'o' : 3, 'p' : 2, 'q' : 1, 'r' : 9, 's' : 8, 't' : 7, 'u' : 6, 'v' : 5, 'w' : 4, 'x' : 3, 'y' : 2, 'z' : 1, '1' : 1,  '2' : 2,  '3' : 3,  '4' : 4,  '5' : 5,  '6' : 6,  '7' : 7,  '8' : 8,  '9' : 9,  '0' : 0}

	#-----------------

	totalEO = 0
	totalFR = 0
	totalRO = 0
	totalRFR = 0

	#-----------------

	valuessimple = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8, 'i' : 9, 'j' : 9, 'k' : 10, 'l' : 11, 'm' : 12, 'n' : 13, 'o' : 14, 'p' : 15, 'q' : 16, 'r' : 17, 's' : 18, 't' : 19, 'u' : 20, 'v' : 20, 'w' : 21, 'x' : 22, 'y' : 23, 'z' : 24}
	valuesshort = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8, 'i' : 9, 'j' : 9, 'k' : 1, 'l' : 2, 'm' : 3, 'n' : 4, 'o' : 5, 'p' : 6, 'q' : 7, 'r' : 8, 's' : 9, 't' : 1, 'u' : 2, 'v' : 2, 'w' : 3, 'x' : 4, 'y' : 5, 'z' : 6}
	valuesreverse = {'a' : 24, 'b' : 23, 'c' : 22, 'd' : 21, 'e' : 20, 'f' : 19, 'g' : 18, 'h' : 17, 'i' : 16, 'j' : 16, 'k' : 15, 'l' : 14, 'm' : 13, 'n' : 12, 'o' : 11, 'p' : 10, 'q' : 9, 'r' : 8, 's' : 7, 't' : 6, 'u' : 5, 'v' : 5, 'w' : 4, 'x' : 3, 'y' : 2, 'z' : 1}
	valueskaye = {'a' : 27, 'b' : 28, 'c' : 29, 'd' : 30, 'e' : 31, 'f' : 32, 'g' : 33, 'h' : 34, 'i' : 35, 'j' : 35, 'k' : 10, 'l' : 11, 'm' : 12, 'n' : 13, 'o' : 14, 'p' : 15, 'q' : 16, 'r' : 17, 's' : 18, 't' : 19, 'u' : 20, 'v' : 20, 'w' : 21, 'x' : 22, 'y' : 23, 'z' : 24}

	#-----------------

	totalsimple = 0
	totalshort = 0
	totalreverse = 0
	totalkaye = 0

	#-----------------

	new = ''

	for letter in s:
		if letter == ' ' or letter.lower() in valuesEO: new += letter

	while '  ' in new: new = new.replace('  ', ' ')

	s = new.strip()
	words = s.split(' ')
	wordnum = len(words)
	letternum = sum(c.isalpha() for c in s)

	letters = []
	EOletters = []
	wordvals = []

	for word in words:
		wordval = 0
		EOletters_words = []
		letters_words = []

		for letter in word:
			letters_words.append(letter)

			letter = letter.lower()

			wordval += valuesEO[letter]
			EOletters_words.append(str(valuesEO[letter]))

			totalEO += valuesEO[letter]
			totalFR += valuesFR[letter]
			totalRO += valuesRO[letter]
			totalRFR += valuesRFR[letter]

			if letter.isalpha():
				totalsimple += valuessimple[letter]
				totalshort += valuesshort[letter]
				totalreverse += valuesreverse[letter]
				totalkaye += valueskaye[letter]

		wordvals.append(wordval)
		letters.append(letters_words)
		EOletters.append(EOletters_words)

	all_total = totalEO + totalFR + totalRO + totalRFR

	infostring = '(' + str(letternum) + ' letters, ' + str(wordnum) + ' words)'

	return wordnum, letternum, infostring, totalEO, totalFR, totalRO, totalRFR, all_total, EOletters, wordvals, letters, totalsimple, totalshort, totalreverse, totalkaye, None, None

#-----------------------------------------------------------------------
# Library

number_library = {
'3' : 'The number 3 is a fundamental number of the world. The Trinity is made up of three beings. The number 3 is important in the Bible, as Jesus was said to have rose again in 3 days.~Matthew 27:40: And saying, Thou that destroyest the temple, and buildest it in three days, save thyself. If thou be the Son of God, come down from the cross.',
'7' : 'Seven is highly fundamental, it is the number of days in a week. 42 is divisible by 7. The number 7 is highly related to 33, as 33 and 7 = 40.~Genesis 2:2 (Verse #33): And on the seventh day God ended his work which he had made; and he rested on the seventh day from all his work which he had made.',
'9' : '9, the product of 3 * 3. Every circle (360 degrees: 3 + 6) equals nine, also the reduction of the sum of the interior angles of any polygon will always equal 9. 9 is important to base-10.',
'17' : 'The 7th prime, and a number which is sometimes used to represent a divine being. Francis Bacon\'s name equals 34 (17 + 17) and 17. The symbol Q, either representing the mischievous character in Star Trek, or the online anonymous internet postings, use this as it is the 17th letter of the alphabet.',
'33' : '33, one of the most important numbers of Freemasonry, we are shown 3 and also 9, by 3 times 3. The middle chapter of the Bible contains 33 English words.',
'40' : 'A number used frequently in the Bible, it is the number of years the Israelites wandered in the desert. It is also the only number in a certain range of Pi to display a circular property of its location in its first occurrence. This is 2 less than 42.',
'42' : '42 represents the ultimate number, it is 6 * 7 or even 33 + 9. 42\'s location in Pi, at the end of 93 digits is important to note, as Revelation 13:5 is the last use of forty two in the Bible, with 135 being 42 + 93.'
}

#-----------------------------------------------------------------------
# Take input from user and decide whether they are entering a date, a number, or a text message

exit_flag = False
extra_search = False
extra_search_count = 2
last_command = 'math'		# (Current available commands) = measure_date, add_date, subtract_date, lone_date_group, number, math, library_search, pi_search, gematria, extra_search, paste_gematria
last_num = '2424'

a = []
b = []

def mainLoop():

	global exit_flag, extra_search, last_command, last_num

	while True:

		try:

			newlines = '\n\n'

			if extra_search:
				extra_search = False
				newlines = '\n'

			user_input = raw_input(newlines + 'Input: ').strip()			# No trailing or leading spaces

			if user_input == 'exit':		# Exit program
				exit_flag = True
				exit()

			if user_input == 'pi':
				choose_number('Pi')
				continue
			if user_input == 'phi':
				choose_number('Phi')
				continue
			if user_input == 'e':
				choose_number('e')
				continue
			if user_input == 'em':
				choose_number('em')
				continue
			if user_input == '2pi':
				choose_number('2Pi')
				continue
			if user_input == 'A':
				choose_number('A')
				continue
			if user_input == 'cat':
				choose_number('cat')
				continue
			if user_input.lower() == 'kl':
				choose_number('KL')
				continue
			if user_input.lower() == 'rt':
				choose_number('rt')
				continue

			num_with_leading_zeros = user_input	# String

			try_eval = True
			eval_result = ''
			eval_user_input = ''

			if user_input != 'pi2' and user_input != 'GK' and user_input != 'sqrt2':
				try:
					eval_user_input = user_input.replace('"', '').replace("'", '')	# Remove double and single quotes
					eval_result = eval(eval_user_input)
				except:
					try_eval = False
			else:
				continue

			pi_search = True

			try:
				int_test = int(user_input.split('//', 1)[1])
				num_with_leading_zeros = user_input.split('//', 1)[1]
			except:
				pi_search = False

			if user_input != '':
				if user_input == len(user_input) * '0':
					last_command = 'number'
					last_num = user_input
					pi_info = search_in_pi(num_with_leading_zeros, 1)
					print('\n\n' + pi_info)
					continue

			library_search = 1

			try:
				library_search = user_input.split('..', 1)[1]

				if not library_search in number_library:
					library_search = 0
			except:
				library_search = 0

			contains_arrow = False
			contains_plus = False
			contains_minus = False
			date_group = False
			lone_date_group = False
			lone_number = False
			separator = ''

			if len(user_input.split(' ')) == 3 and user_input.replace(' ', '').isdigit():
				lone_date_group = True

			if user_input.isdigit():
				lone_number = True

			if '+' in user_input:
				contains_plus = True
				separator = '+'
			if '-' in user_input and not '->' in user_input:
				contains_minus = True
				separator = '-'
			if '->' in user_input:
				contains_arrow = True
				separator = '->'

			if contains_plus or contains_minus:
				left_side = user_input.split(separator, 1)[0].strip()
				right_side = user_input.split(separator, 1)[1].strip()

				if len(left_side.split(' ')) == 3 and left_side.replace(' ', '').isdigit() and right_side.isdigit():
					# There are three groups of numbers on left side, and the right side contains just a number
					date_group = True
				if left_side.lower() == 'a' or left_side.lower() == 'b' and right_side.isdigit():
					date_group = True

			if contains_arrow:
				left_side = user_input.split(separator, 1)[0].strip()
				right_side = user_input.split(separator, 1)[1].strip()

				left_group = False
				right_group = False

				if len(left_side.split(' ')) == 3 and left_side.replace(' ', '').isdigit():		# There are three groups of numbers on left side
					left_group = True
				if len(right_side.split(' ')) == 3 and right_side.replace(' ', '').isdigit():	# There are three groups of numbers on right side
					right_group = True

				if left_side.lower() == 'a' or left_side.lower() == 'b':
					left_group = True
				if right_side.lower() == 'a' or right_side.lower() == 'b':
					right_group = True

				if left_group and right_group:
					date_group = True

			if contains_arrow and date_group:			# We are measuring the distance between two dates
				last_command = 'measure_date'
				first_date = user_input.split('->', 1)[0].strip().lower()
				second_date = user_input.split('->', 1)[1].strip().lower()

				start_year, start_month, start_day = None, None, None
				end_year, end_month, end_day = None, None, None

				if first_date == 'a':
					start_year, start_month, start_day = a[0], a[1], a[2]
				elif first_date == 'b':
					start_year, start_month, start_day = b[0], b[1], b[2]
				else:
					start_year, start_month, start_day = split_up_date(first_date)

				if second_date == 'b':
					end_year, end_month, end_day = b[0], b[1], b[2]
				elif second_date == 'a':
					end_year, end_month, end_day = a[0], a[1], a[2]
				else:
					end_year, end_month, end_day = split_up_date(second_date)

				a = [start_year, start_month, start_day]
				b = [end_year, end_month, end_day]

				start = dt.datetime(start_year, start_month, start_day, 0, 0, 0)
				end = dt.datetime(end_year, end_month, end_day, 0, 0, 0)
				delta = end - start

				result = str(delta.days)

				if delta.days < 0:
					result = str(-delta.days)

				start_date_nice = str(start_month) + '/' + str(start_day) + '/' + str(start_year)
				end_date_nice = str(end_month) + '/' + str(end_day) + '/' + str(end_year)

				print_date_information(start_year, start_month, start_day, end_year, end_month, end_day)

				result_string = '\n\n' + start_date_nice + ' -> ' + end_date_nice + ' = ' + str(result) + ' days'

				print(result_string)

			elif contains_plus and date_group:			# We are adding a certain number of days to a date
				last_command = 'add_date'
				first_date = user_input.split('+', 1)[0].strip().lower()
				the_days = int(user_input.split('+', 1)[1].strip())

				start_year, start_month, start_day = None, None, None

				if first_date == 'a':
					start_year, start_month, start_day = a[0], a[1], a[2]
				elif first_date == 'b':
					start_year, start_month, start_day = b[0], b[1], b[2]
				else:
					start_year, start_month, start_day = split_up_date(first_date)

				start = dt.datetime(start_year, start_month, start_day, 0, 0, 0)

				r_date = start + dt.timedelta(the_days)
				end_year = r_date.year
				end_month = r_date.month
				end_day = r_date.day

				a = [start_year, start_month, start_day]
				b = [end_year, end_month, end_day]

				start_date_nice = str(start_month) + '/' + str(start_day) + '/' + str(start_year)
				end_date_nice = str(end_month) + '/' + str(end_day) + '/' + str(end_year)
				result_string = '\n\n' + start_date_nice + ' + ' + str(the_days) + ' days = ' + end_date_nice

				print_date_information(start_year, start_month, start_day, end_year, end_month, end_day)

				print(result_string)

			elif contains_minus and date_group:			# We are subtracting a certain number of days from a date
				last_command = 'subtract_date'
				first_date = user_input.split('-', 1)[0].strip().lower()
				the_days = int(user_input.split('-', 1)[1].strip())

				start_year, start_month, start_day = None, None, None

				if first_date == 'a':
					start_year, start_month, start_day = a[0], a[1], a[2]
				elif first_date == 'b':
					start_year, start_month, start_day = b[0], b[1], b[2]
				else:
					start_year, start_month, start_day = split_up_date(first_date)

				start = dt.datetime(start_year, start_month, start_day, 0, 0, 0)

				r_date = start - dt.timedelta(the_days)
				end_year = r_date.year
				end_month = r_date.month
				end_day = r_date.day

				a = [start_year, start_month, start_day]
				b = [end_year, end_month, end_day]

				start_date_nice = str(start_month) + '/' + str(start_day) + '/' + str(start_year)
				end_date_nice = str(end_month) + '/' + str(end_day) + '/' + str(end_year)
				result_string = '\n\n' + start_date_nice + ' - ' + str(the_days) + ' days = ' + end_date_nice

				print_date_information(start_year, start_month, start_day, end_year, end_month, end_day)

				print(result_string)

			elif lone_date_group:			# The user_input is simply a date group, so we will display its information
				last_command = 'lone_date_group'
				year, month, day = split_up_date(user_input)

				print_date_information(year, month, day, None, None, None)

			#-----------------------------------------------------------------------
			# Analyze number

			elif lone_number:				# The user_input is an integer for us to display its properties
				last_command = 'number'
				num = int(user_input)
				last_num = user_input

				factorization = prime_factors(num)
				divisors = list(divisorGenerator(num))
				sum_of_divisors = sum(divisors)
				prime_num, nth_prime, previous_prime, next_prime = prime_info(num)
				prev_int = str(num - 1)
				next_int = str(num + 1)
				binary = bin(num)[2:]
				octal = oct(num).lstrip('0')
				hexadecimal = hex(num)[2:]
				duodecimal = base10toN(num, 12).replace(':', 'A').lower()
				square = num * num
				square_root = num ** (1/2.0)
				square_root = ('%f' % square_root).rstrip('0').rstrip('.')
				cube_root = is_perfect_cube(num)
				isFib = isFibonacci(num)
				isFac = isFactorial(num)
				isReg = isRegular(num, factorization)
				isPerf = isPerfect(num, divisors)
				nat_log = math.log(num)
				dec_log = math.log10(num)
				sine = math.sin(num)
				cosine = math.cos(num)
				tangent = math.tan(num)

				print('\n')

				first_part = ''
				len1 = 20
				len2 = 19

				if len(prev_int) % 2 != 0:  # Is not even length
					len1 = 19

				first_part = (((len1 - len(prev_int)) / 2) * ' ')
				next_part = (((len2 - len(next_int)) / 2) * ' ')

				line = first_part + prev_int + next_part + str(num) + next_part + next_int

				if user_input in number_library:
					line += '       (Info Available!)\n'
				else:
					line += '\n'

				print(line)

				print('Factorization:     ' + str(factorization).replace('[', '').replace(']', '').replace(', ', ' * '))
				print('Divisors:          ' + str(divisors).replace('[', '').replace(']', ''))
				print('Count of divisors: ' + str(len(divisors)))
				print('Sum of divisors:   ' + str(sum_of_divisors) + '\n')

				prime_1 = 'Previous prime:    ' + str(previous_prime)
				prime_2 = 'Next prime:        ' + str(next_prime)
				prime_3 = ''
				prime_4 = ''

				if prime_num:
					prime_3 = 'Prime?: YES, prime #' + str(prime_num) + ''
				else:
					prime_3 = 'Prime?: NO'

				prime_s = 'Prime #' + str(num) + ' is:'
				prime_s += ' ' * (19 - len(prime_s))
				prime_4 = prime_s + str(nth_prime)

				prime_line1 = format(prime_1, prime_3)
				prime_line2 = format(prime_2, prime_4)

				print(prime_line1)
				print(prime_line2 + '\n')

				bases_1 = 'Binary:            ' + binary
				bases_2 = 'Octal:             ' + octal
				bases_3 = 'Duodecimal:        ' + duodecimal
				bases_4 = 'Hexadecimal:       ' + hexadecimal

				bases_line1 = format(bases_1, bases_3)
				bases_line2 = format(bases_2, bases_4)

				print(bases_line1)
				print(bases_line2 + '\n')

				if isFib or isFac or isReg or isPerf:
					if isFib:
						print('Is a Fibonacci number!')
					if isFac:
						print('Is a Factorial!')
					if isReg:
						print('Is a Regular number!')
					if isPerf:
						print('Is a Perfect number!')

					print('')

				square_1 = 'Square:            ' + str(square)
				square_r = 'Square root:       ' + str(square_root)

				info1 = 'Natural logarithm: ' + str(nat_log)
				info2 = 'Decimal logarithm: ' + str(dec_log)
				info3 = 'Sine:              ' + str(sine)
				info4 = 'Cosine:            ' + str(cosine)
				info5 = 'Tangent:           ' + str(tangent)

				info_line1 = format(square_1, info1)
				info_line2 = format(square_r, info2)
				info_line3 = ''

				if cube_root:
					cube_r = 'Cube root:         ' + str(cube_root)
					info_line3 = format(cube_r, info3)
				else:
					info_line3 = format('', info3)

				info_line4 = format('', info4)
				info_line5 = format('', info5)

				print(info_line1)
				print(info_line2)
				print(info_line3)
				print(info_line4)
				print(info_line5)

				pi_info = search_in_pi(num_with_leading_zeros, 1)

				print('\n' + pi_info)

				pi_sum = digit_sum_pi(num)

				if pi_sum != '':
					if (not pi_info.endswith('\n\n')) and (not pi_info.endswith('^')):			# Keep formatting consistent
						print('\n' + pi_sum)
					else:
						print(pi_sum)

			#-----------------------------------------------------------------------
			# Simple math tool

			elif try_eval:
				last_command = 'math'
				print('\n\n' + str(eval_result))

			#-----------------------------------------------------------------------
			# Library search

			elif library_search:
				last_command = 'library_search'

				console_width = get_terminal_size()[0]

				entry = number_library[library_search]
				paragraphs = entry.split('~')
				complete = ''

				for paragraph in paragraphs:
					lines = textwrap.wrap(paragraph, console_width)
					for line in lines:
						complete += line + '\n'
					complete += '\n'

				while complete.endswith('\n'): complete = complete[:-1]

				print('\n\n' + complete)

			#-----------------------------------------------------------------------
			# Pi search tool

			elif pi_search:
				last_command = 'pi_search'
				find_multiple_pi(num_with_leading_zeros)

			#-----------------------------------------------------------------------
			# Analyze gematria

			else:
				if user_input == '' or eval_user_input == '':		# The second_function sends a newline and this function may receive it
					continue

				last_command = 'gematria'

				wordnum, letternum, infostring, totalEO, totalFR, totalRO, totalRFR, all_total, EOletters, wordvals, letters, totalsimple, totalshort, totalreverse, totalkaye, totalHebrew, totalGreek = Gematria(user_input)

				if wordnum == None:
					print('\n\nText could not be decoded')
					continue

				complete = Gematria_print(wordnum, letternum, infostring, totalEO, totalFR, totalRO, totalRFR, all_total, EOletters, wordvals, letters, totalsimple, totalshort, totalreverse, totalkaye, totalHebrew, totalGreek)
				print('\n\n' + complete)

		except SystemExit:
			exit()

		except:
			pass

keyboard = Controller()
thread = None

def second_function(key):
	global extra_search, extra_search_count, last_command

	if exit_flag:
		return False

	if key == Key.shift_r:
		# Find next occurrence of last searched number in Pi

		if last_command != 'extra_search':
			if last_command == 'number':
				extra_search_count = 2
			else:
				extra_search_count = 1

		last_command = 'extra_search'
		extra_search = True

		pi_info = search_in_pi(last_num, extra_search_count)

		if 'This number does not' in pi_info and 'What occurs at' not in pi_info:
			pi_info += '\n'

		extra_search_count += 1
		sys.stdout.write('\n\n\n' + pi_info)				# No newline at end

		keyboard.press(key.enter)							# Returns to main loop
		keyboard.release(key.enter)

	if key == Key.ctrl_r:
		# Get clipboard contents and check Gematria

		last_command = 'paste_gematria'
		wordnum, letternum, infostring, totalEO, totalFR, totalRO, totalRFR, all_total, EOletters, wordvals, letters, totalsimple, totalshort, totalreverse, totalkaye, totalHebrew, totalGreek = Gematria(clipboard.paste())

		if wordnum == None:
			sys.stdout.write('\n\n\nText could not be decoded')
		else:
			complete = Gematria_print(wordnum, letternum, infostring, totalEO, totalFR, totalRO, totalRFR, all_total, EOletters, wordvals, letters, totalsimple, totalshort, totalreverse, totalkaye, totalHebrew, totalGreek)
			sys.stdout.write(('\n\n\n' + complete).encode(sys.stdout.encoding, errors='replace'))

		keyboard.press(key.enter)				# Returns to main loop
		keyboard.release(key.enter)

thread = Thread(target=mainLoop)
thread.start()

with Listener(on_release=second_function) as listener:

	pi = """"""
	phi = """"""
	e = """"""
	em = """"""
	pi2 = """"""
	GK = """"""
	cat = """"""
	KL = """"""
	sqrt2 = """"""

	the_constant = pi

	listener.join()