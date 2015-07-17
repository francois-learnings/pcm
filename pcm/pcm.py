import time
import threading

import pyperclip

import pyload_client
import parse_options

site_list = [
    "1fichier", 
    "uplea", 
    "tusfile", 
    "dl-protect", 
    "filefactory"]

def is_url_from_hoster(url):
    if url.startswith("http://") or url.startswith("https://"):
	for site in site_list:
	    if site in url:
        	return True
    return False

def push_to_pyload(clipboard_content, options):
    print "Found url: %s" % str(clipboard_content)
    server_ip = options["SERVER_IP"]
    server_port = options["SERVER_PORT"]
    username = options["USER"]
    password = options["PASSWORD"]

    client = pyload_client.PyloadClient(server_ip, server_port, username, password)
    client.push_link(str(clipboard_content), str(clipboard_content))

class ClipboardWatcher(threading.Thread):
    def __init__(self, predicate, callback, pause=5.):
	"""

	"""
        super(ClipboardWatcher, self).__init__()
        self._predicate = predicate
        self._callback = callback
        self._pause = 5
        self._stopping = False
	self.options = parse_options.parse_options()
	print self.options

    def run(self):       
        recent_value = ""
        while not self._stopping:
            tmp_value = pyperclip.paste()
            if tmp_value != recent_value:
                recent_value = tmp_value
                if self._predicate(recent_value):
                    self._callback(recent_value, self.options)
            time.sleep(self._pause)

    def stop(self):
        self._stopping = True

def main():
    watcher = ClipboardWatcher(is_url_from_hoster, 
                               push_to_pyload,
                               5.)
			       
    watcher.start()
    while True:
        try:
            print "Waiting for changed clipboard..."
            time.sleep(10)
        except KeyboardInterrupt:
            watcher.stop()
            break

if __name__ == "__main__":
    main()
