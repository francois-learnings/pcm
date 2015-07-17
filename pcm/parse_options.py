import os
import sys
import getopt

def parse_options():
    DICT_OPTS = {}
    DICT_OPTS["CONFIG_FILE"] = os.getenv('PCM_CONFIG', None)
    DICT_OPTS["USER_SETTINGS_FILE"] = os.getenv('PCM_USER_SETTINGS', None)
    DICT_OPTS["SERVER_IP"] = os.getenv('PCM_SERVER_IP', None)
    DICT_OPTS["SERVER_PORT"] = os.getenv('PCM_SERVER_PORT', None)
    DICT_OPTS["USER"] = os.getenv('PCM_USER', None)
    DICT_OPTS["PASSWORD"] = os.getenv('PCM_PASSWORD', None)

    try:
	    opts, args = getopt.getopt(
    	sys.argv[1:],
    	"a:P:u:p:h",
    	[
    	    "help",
    	    "address=",
    	    "port=",
    	    "user=",
    	    "password="
    	]
        )
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)

    # Process options
    warning_option_msg = ("Warning ! The environment variable \"%s\" is \
    	    	      BUT the value will be overwritten because of the \
    		      parameter \"%s\"")

    for o, a in opts:
        if o in ("-h", "--help"):
    	    usage()
    	    sys.exit(0)
        elif o in ("-a", "--address"):
    	    if DICT_OPTS["SERVER_IP"] is not None:
    	        print (warning_option_msg) % ("SERVER_IP", o)
    	    SERVER_IP = a
    	    # print SERVER_IP
    	    DICT_OPTS["SERVER_IP"] = SERVER_IP

        elif o in ("-P", "--port"):
    	    if DICT_OPTS["SERVER_PORT"] is not None:
    	        print (warning_option_msg) % ("SERVER_PORT", o)
    	    SERVER_PORT = a
    	    # print SERVER_PORT
    	    DICT_OPTS["SERVER_PORT"] = SERVER_PORT

        elif o in ("-u", "--user"):
    	    if DICT_OPTS["USER"] is not None:
    	        print (warning_option_msg) % ("USER", o)
    	    USER = a
    	    # print USER
    	    DICT_OPTS["USER"] = USER

        elif o in ("-p", "--password"):
    	    if DICT_OPTS["PASSWORD"] is not None:
    	        print (warning_option_msg) % ("PASSWORD", o)
    	    PASSWORD = a
    	    # print PASSWORD
    	    DICT_OPTS["PASSWORD"] = PASSWORD
    return DICT_OPTS
