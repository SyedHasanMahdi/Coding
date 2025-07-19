# regular expressions : allow us to search a text for strings matching a specific pattern
# example : what are all the four-letter words in a file?
# regex = regular expression
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR performing package upgrade"
# trying to get 12345 from []
index = log.index("[")
print(log[index + 1:index + 6])  # don't want to include brackets
# may not always work

import re

log = "July 31 07:51:48 computer bad_process[12345]: ERROR performing package upgrade"
regex = r"\[(/d+)\]"
result = re.search(regex, log)
print(result)

# /usr/share/dict/words one word per line

