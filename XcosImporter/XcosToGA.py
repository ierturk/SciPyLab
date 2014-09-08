#############################################################################
## file        XcosToGA.py
## author      ierturk @ StarGateInc <ierturk@ieee.org>
## version     0.0.0
## date        Aug 28, 2014
## brief       Xcos diagram browser as treewiev
##
## COPYRIGHT 2014 StarGate Inc
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
#############################################################################


from lxml import etree

class XcosToGA:
    
    def Convert(self, XcosFile):
        self.XcosDiag = etree.parse('testDiagram.xml')
        self.GAModel = etree.ElementTree(etree.Element('GASystemModel'))

        self.ContainerTag = self.XcosDiag.xpath('/XcosDiagram/mxCell[@as="defaultParent"]')
        if len(self.ContainerTag) == 1:
            self.ContainerID = self.ContainerTag[0].attrib["id"]
            
        self.ContainerTag = self.GAModel.xpath('/GASystemModel')
        self.ContainerTag[0].attrib["id"] = self.ContainerID
        
        
        #print(ContainerID)
        self.BasicBlocks = self.XcosDiag.xpath('/XcosDiagram/mxGraphModel/root/BasicBlock\
                                        [@parent="' + self.ContainerID + '"]')
        
        print(len(self.BasicBlocks))
        
        for Block in self.BasicBlocks:
            print(Block.attrib["simulationFunctionName"])
            #ContainerTag[0] = ContainerID
            self.NewBlock = etree.Element("Block", id=Block.attrib["id"], testattr="5")
            self.ContainerTag[0].append(self.NewBlock)

        self.GAModel.write('testGA.xml')

#############################################################################
## COPYRIGHT 2014 StarGate Inc / END OF FILE
#############################################################################