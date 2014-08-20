"""
file        SciPyLab.py
author      ierturk @ StarGateInc <ierturk@ieee.org>
version     0.0.0
date        20-Aug-2014
brief       Python Scilab binding

COPYRIGHT 2014 StarGate Inc

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from scilink import SciLink
from threading import Thread
from configparser import ConfigParser

import os
import sys
import time


class ScilabError(Exception):
    """ Define an exception class """
    pass


class doEval(object):
    """
    """

    def __init__(self, name):
        if type(name) != type(""):
            raise TypeError("name must be a string")
        self.name = name

    def __call__(self, *args):
        """
        """


        cmd = self.name + "("
        lenArgs = len(args)

        for (i, arg) in enumerate(args):
            cmd += str(arg)
            if(i<lenArgs-1):
                cmd += ","
        cmd += ")"

        print(cmd)            
        scilink.Eval(cmd + "; disp(ans)")

class Scilab(object):
    """
    Call any Scilab function from Python
    """

    def __getattr__(self, name):
        return doEval(name)

class ScilabThread(Thread):
        """ Defines the Scilab thread to start """
        def __init__(self, func):
                Thread.__init__(self)
                self.func = func
                self.daemon = True

        def run(self):
                self.func()

def scipoll():
    while 1:
        scilink.Eval("")
        time.sleep(0.1)

# Create SciLink objects
scilink = SciLink()
scilab = Scilab()

# Start thread
poll_thread = ScilabThread(scipoll)
poll_thread.start()

"""
COPYRIGHT 2014 StarGate Inc / END OF FILE
"""