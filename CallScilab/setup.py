"""
file        setup.py
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

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import os

common_include_base = r"C:\Program Files\scilab-5.5.0\modules"
sci_include = [
            os.path.join(common_include_base, "core", "includes"),
            os.path.join(common_include_base, "call_scilab", "includes"),
            os.path.join(common_include_base, "api_scilab", "includes"),
            os.path.join(common_include_base, "output_stream", "includes")
		       ]

sci_lib_dir =  [r"C:\Program Files\scilab-5.5.0\bin"]
sci_librairies = ['core', 'api_scilab', 'call_scilab', 'output_stream']
sci_extra_link_args = ['']

sci_sources = ['scilink.pyx']

scicy_module = Extension(name='scilink',
                            sources = sci_sources,
                            include_dirs = sci_include,
                            libraries = sci_librairies,
                            library_dirs = sci_lib_dir,
                            extra_link_args = sci_extra_link_args,
                            )

long_description = r"""
The goal of SciPyLab is to give an access to Scilab features inside Python.
"""

setup( name = 'SciPyLab',
              version = '0.0.0',
              author = 'Ibrahim ERTURK <ierturk@ieee.org>',
              url = "http://www.stargate-tr.com",
              license = "GPL",
              description = 'Python Scilab binding by Cython',
              long_description = long_description,
              ext_modules = [scicy_module],
                cmdclass = {'build_ext': build_ext},
            )

"""
COPYRIGHT 2014 StarGate Inc / END OF FILE
"""
