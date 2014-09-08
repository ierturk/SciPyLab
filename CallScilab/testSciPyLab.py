"""
file        testSciPyLab.py
author      ierturk @ StarGateInc <ierturk@ieee.org>
version     0.0.0
date        Aug 28, 2014
brief       Python Scilab binding

COPYRIGHT 2014 StarGate Inc

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


from SciPyLab import Scilab

sci = Scilab()

sci.plot([0,1,2,3,4,5,4,3,2,1,0])

if __name__ == '__main__':
    pass

"""
COPYRIGHT 2014 StarGate Inc / END OF FILE
"""