"""
file        scilink.pyx
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

class ScilabError(Exception):
    pass

cdef extern from "call_scilab.h":
    int StartScilab(char*, char*, int)
    int SendScilabJob(char*)
    void ScilabDoOneEvent()
    int ScilabHaveAGraph()
    int getVariableType(char*)

cdef extern from "api_scilab.h":
    cdef struct api_Ctx:
        char* pstName
        
    ctypedef api_Ctx StrCtx
    StrCtx* pvApiCtx

    int isNamedIntegerType(void*, const char*)
    int getNamedMatrixOfIntegerPrecision(void*, const char*, int*)
    int createNamedScalarInteger32(void*, const char*, int)
    int getNamedScalarInteger32(void* , const char*, int*)
    
    int readNamedMatrixOfInteger32(void*, const char*, int*, int*, int*)


class SciLink:
    """Scilab link"""
    def __init__(self):
        print("Starting Scilab Engine ....")
        if(StartScilab(NULL, NULL, 0)):
            print("Scilab Engine has been started succesfully!!!")
        else:
            raise ScilabError("Scilab Engine could not be started!!!")
        
    def Eval(self, job):
        self.job = str.encode(job)
        SendScilabJob(self.job)
        while(ScilabHaveAGraph()):
            ScilabDoOneEvent()

"""
COPYRIGHT 2014 StarGate Inc / END OF FILE
"""





