#!/usr/bin/python
import sys, getopt
from instapy import InstaPy

def main(argv):
	username = '';
	password = '';
	hashtags = '';
	tagamount = 1;
	likeamount = 1;
	comment = 'Awesome,I love It';
	
	try:
		opts, args = getopt.getopt(argv,"hu:p:t:a:l:c:",["username=","password=","hashtags=","tagamount=","likeamount=","comment="])
	except getopt.GetoptError:
		print ('quickstart.py -u <username> -p <password> -t <hashtags>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print ('quickstart.py -u <username> -p <password> -t <hashtags> -t <hashtags> -a <tagamount> -l <likeamount> -c <comment>')
			sys.exit()
		elif opt in ("-u", "--username"):
			username = arg
		elif opt in ("-p", "--password"):
			password = arg
		elif opt in ("-t", "--hashtags"):
			hashtags = arg
		elif opt in ("-a", "--hashtag amount"):
			tagamount = arg
		elif opt in ("-l", "--like amount"):
			likeamount = arg
		elif opt in ("-c", "--comment"):
			comment = arg
			
			
	print ('Username is ', username)
	print ('Password is ', password)
	print ('hashtags is ', hashtags)
	print ('tagamount is ', tagamount)
	print ('likeamount is ', likeamount)
	print ('comment is ', comment)
	
	print (hashtags.split(','))
	print (comment.split(','))
	
	insta_username = username
	insta_password = password

	# set headless_browser=True if you want to run InstaPy on a server
	try:
		session = InstaPy(username=insta_username,
						  password=insta_password,
						  headless_browser=True,
						  bypass_suspicious_attempt=False,
						  multi_logs=True)
		session.login()

		# settings
		session.set_upper_follower_count(limit=550)
		session.set_lower_follower_count(limit=25)
		session.set_do_follow(enabled=True, percentage=10, times=1)
		session.set_do_comment(True, percentage=10)
		session.set_comments(comment.split(','))
		
		#session.set_dont_unfollow_active_users(enabled=True, posts=5)
		#session.unfollow_users(amount=10, onlyInstapyFollowed=True, onlyInstapyMethod = 'FIFO', sleep_delay=60)
		
		# actions
		#session.like_by_tags(hashtags.split(','), amount=1)
		
		# 14 tags
		session.set_smart_hashtags(hashtags.split(','), limit=int(tagamount), sort='top', log_tags=True)
		session.like_by_tags(amount=int(likeamount), use_smart_hashtags=True)

	finally:
		# end the bot session
		session.end()

if __name__ == "__main__":
   main(sys.argv[1:])