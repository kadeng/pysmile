
#Testing the functionality of the pysmile library. This library is a direct wrapper around the SMILE and SMILEARN Libraries which belong to the GeNiE Bayesian Network Software. The Library is documented here: <a href="http://genie.sis.pitt.edu/wiki/Main_Page">GeNiE & Smile Documentation Wiki</a>

from pysmile import *
# Basic int array functionality
ia2 = DSL_intArray(20)
items = intArray.frompointer(ia2.Items()) # Warning: items is an *unchecked* array of ints now.
# We can even do pointer stuff
for i in range(0,20):
    items[i] = i+6
    
h = intPointer.frompointer(ia2.Subscript(10))

h.assign(21)
# Basic double array functionality
da2 = DSL_doubleArray(20)
ditems = doubleArray.frompointer(da2.Items()) # Warning: items is an *unchecked* array of doubles now.

for i in range(0,20):
    ditems[i] = i+6.4
    
ditems[10]
# Basic string array functionality
sa2 = DSL_stringArray(20,10)

for i in range(0,20):
    sa2.SetString(i, "Alles klar %d" % (i))
    
print sa2.Subscript(10)
# Basic id array functionality
ia2 = DSL_idArray(20,10)

for i in range(0,20):
    ia2.SetString(i, "AllesKlar%d" % (i))
    
print ia2.Subscript(10)
ia2.SetString(4, "Alles Klar %d" % (4))

print ia2.Subscript(4)
ar = toDSL_intArray([1,2,3])
ari = intArray.frompointer(ar.Items())

ar = toDSL_doubleArray([1.1,2.2,3.3])
ari = doubleArray.frompointer(ar.Items())
dm = DSL_Dmatrix(toDSL_intArray([2,2,3]))
import pysmile
theNet = DSL_network()
success = theNet.AddNode(DSL_CPT,"Success")
someNames = DSL_stringArray()
someNames.Add("Success")
someNames.Add("Failure")
theNet.GetNode(success).Definition().SetNumberOfOutcomes(someNames)
forecast = theNet.AddNode(DSL_CPT,"Forecast")
someNames.Flush()
someNames.Add("Good")
someNames.Add("Moderate")
someNames.Add("Poor")
theNet.GetNode(forecast).Definition().SetNumberOfOutcomes(someNames)
theNet.AddArc(success,forecast)
theProbs = DSL_doubleArray()
theProbs.SetSize(2)
theProbs.setUnchecked(1, 0.3)
theProbsItem = doubleArray.frompointer(theProbs.Items())
theProbsItem[0] = 0.7
theNet.GetNode(success).Definition().SetDefinition(theProbs);
theNet.WriteFile("tutorial.xdsl")
theCoordinates = DSL_sysCoordinates(theNet.GetNode(forecast).Definition());
theCoordinates.GoTo(0)
ds = DSL_dataset()
ds.ReadFile('/data/fast/ltm_wifi_test/NISLTM/train_set.csv')
ds.GetNumberOfRecords()
ds.GetNumberOfVariables()
learner = DSL_tan()
learnedTANNetwork = DSL_network()
learner.maxSearchTime=1000
learner.classvar = "wifi_usage"
learner.Learn(ds, learnedTANNetwork)
learnedTANNetwork.WriteFile("tan_learned1.xdsl")
from pysmile import *

ds = DSL_dataset()
ds.ReadFile('/data/fast/ltm_wifi_test/NISLTM/train_set.csv')

# Learn a Tree Augmented Naived Bayes Model
learner = DSL_tan() 
learnedTANNetwork = DSL_network()
learner.maxSearchTime=int(1000)
learner.classvar = "wifi_usage"
learner.Learn(ds, learnedTANNetwork)
learnedTANNetwork.WriteFile("tan_learned.xdsl")

learnedTANNetwork.GetNode(learnedTANNetwork.FindNode("domain_content")
vds = DSL_dataset()
vds.ReadFile('validation_set.csv')
vds.RemoveVar(vds.FindVariable("wifi_usage"))
vds.RemoveVar(vds.FindVariable("domain_content"))
vds.RemoveVar(vds.FindVariable("domain_context"))
vds.RemoveVar(vds.FindVariable("domain_activity"))
vds.RemoveVar(vds.FindVariable("device_wifi_usage_class"))

vmatches = DSL_datasetMatch_vector()
vds.MatchNetworkSimple(learnedTANNetwork, vmatches)
case = DSL_simpleCase(learnedTANNetwork)
case.SetEvidenceByHandle(learnedTANNetwork.FindNode("age"), 1)
case.CaseToNetwork()
learnedTANNetwork.UpdateBeliefs()
wifi_node = learnedTANNetwork.GetNode(learnedTANNetwork.FindNode("age"))
val = wifi_node.Value()
values = val.GetMatrix()
va = doubleArray.frompointer(wifi_node.Value().GetMatrix().GetItems().Items())
va[1]
learnedTANNetwork.ClearAllEvidence()
learnedTANNetwork.UpdateBeliefs()
age_node = learnedTANNetwork.GetNode(learnedTANNetwork.FindNode("age"))
val = age_node.Value()
val.SetEvidence(1)
values = val.GetMatrix()
va[0]
ds2 = DSL_dataset()
ds2.ReadFile('/data/fast/ltm_wifi_test/NISLTM/train_set.csv')
for name in ds2.GetStateNames(ds2.FindVariable("domain_content")):
    print name

for name in vds.GetStateNames(vds.FindVariable("domain_content")):
    print name

x = DSNetworkMatch(learnedTANNetwork)
print x.attachDataset(vds)
wifi_usage_node = learnedTANNetwork.FindNode("wifi_usage")
learnedTANNetwork.ClearAllEvidence()
learnedTANNetwork.UpdateBeliefs()
va = doubleArray.frompointer(learnedTANNetwork.GetNode(wifi_usage_node).Value().GetMatrix().GetItems().Items())
print va[0]

for i in range(10):
    x.enterEvidenceFromDatasetRow(21*i)
    learnedTANNetwork.UpdateBeliefs()
    print va[0]

outc = ndef.GetOutcomesNames()
for i in range(outc.GetSize()):
    print outc.Subscript(i)
