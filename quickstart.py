#!/usr/bin/python
import sys, getopt
from instapy import InstaPy

def main(argv):
	username = '';
	password = '';
	hashtags = '';

	try:
		opts, args = getopt.getopt(argv,"hu:p:t:",["username=","password=","hashtags="])
	except getopt.GetoptError:
		print ('quickstart.py -u <username> -p <password> -t <hashtags>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print ('quickstart.py -u <username> -p <password> -t <hashtags>')
			sys.exit()
		elif opt in ("-u", "--username"):
			username = arg
		elif opt in ("-p", "--password"):
			password = arg
		elif opt in ("-t", "--hashtags"):
			hashtags = arg

	print ('Username is ', username)
	print ('Password is ', password)
	print ('hashtags is ', hashtags)
	
	insta_username = username
	insta_password = password

	# set headless_browser=True if you want to run InstaPy on a server
	try:
		session = InstaPy(username=insta_username,
						  password=insta_password,
						  headless_browser=False,
						  bypass_suspicious_attempt=False,
						  multi_logs=True)
		session.login()

		# settings
		session.set_upper_follower_count(limit=2500)
		session.set_do_comment(True, percentage=10)
		session.set_comments(['aMEIzing!', 'So much fun!!', 'Nicey!'])
		session.set_dont_include(['friend1', 'friend2', 'friend3'])
		session.set_dont_like(['pizza', 'girl'])
		
		print (hashtags.split(','))
		
		# actions
		session.like_by_tags(hashtags.split(','), amount=1)

	finally:
		# end the bot session
		session.end()

if __name__ == "__main__":
   main(sys.argv[1:])