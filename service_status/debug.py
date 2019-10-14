import sys
sys.path.append("..")
from lib.logging_class import *

rz=rizhi()
rz.send_to_stdout()
rz.send_to_file("log")
rz.log("hello",log_value=40)