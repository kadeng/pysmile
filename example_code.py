
# Now, we do some modeling
from pysmile import *
///

ds = DSL_dataset()
ds.ReadFile('/data/fast/ltm_wifi_test/NISLTM/train_set.csv')
///

# Learn a Tree Augmented Naived Bayes Model
learner = DSL_tan() # See
learnedTANNetwork = DSL_network()
learner.maxSearchTime=1000
learner.classvar = "wifi_usage"
learner.seed = 0
learner.Learn(ds, learnedTANNetwork)
learnedTANNetwork.WriteFile("tan_learned.xdsl")
///

# Determine training set and validation set accuracy

tds = DSL_dataset()
tds.ReadFile('/data/fast/ltm_wifi_test/NISLTM/train_set.csv')
tds.RemoveVar(tds.FindVariable("wifi_usage"))

vds = DSL_dataset()
vds.ReadFile('/data/fast/ltm_wifi_test/NISLTM/validation_set.csv')
vds.RemoveVar(vds.FindVariable("wifi_usage"))

vdsmatch = DSNetworkMatch(learnedTANNetwork)
print vdsmatch.attachDataset(vds)

wifi_usage_node = learnedTANNetwork.FindNode("wifi_usage")
learnedTANNetwork.ClearAllEvidence()
learnedTANNetwork.UpdateBeliefs()
va = doubleArray.frompointer(learnedTANNetwork.GetNode(wifi_usage_node).Value().GetMatrix().GetItems().Items())
validation_y = np.array(validation_set.wifi_usage=='s1_below_0', dtype=np.int8)

sum_of_squares = 0.0
for i in range(len(validation_y)):
    vdsmatch.enterEvidenceFromDatasetRow(i)
    learnedTANNetwork.UpdateBeliefs()
    prob = va[0]
///
#print "prob=%f - correct=%s" % (prob, validation_y[i])
    diff = float(validation_y[i]) - prob
    sum_of_squares += diff*diff

print sqrt(sum_of_squares)
///

print vdsmatch.attachDataset(tds)
train_y = np.array(train_set.wifi_usage=='s1_below_0', dtype=np.int8)
for i in range(len(train_y)):
    vdsmatch.enterEvidenceFromDatasetRow(i)
    learnedTANNetwork.UpdateBeliefs()
    prob = va[0]
    #print "prob=%f - correct=%s" % (prob, train_y[i])
    diff = float(train_y[i]) - prob
    sum_of_squares += diff*diff
    
print sqrt(sum_of_squares)
///
ds.RemoveVar(ds.FindVariable("wifi_usage"))
///

# Learn an unconstrained network (this will take some time)
bs_learner = DSL_bs() # See http://genie.sis.pitt.edu/wiki/Reference_Manual:_DSL_bs
bs_learner.maxParents = 7
bs_learner.nrIteration = 150
bs_learner.priorLinkProbability = 0.001
bs_learner.linkProbability = 0.05
bs_learner.maxTime = 3600*8
bs_learner.seed = 2

learnedBSNetwork = DSL_network()
///
bs_learner.Learn(ds, learnedBSNetwork)
learnedBSNetwork.WriteFile("bs_learned_2.xdsl")
///

bs_learner.linkProbability = 0.2
bs_learner.priorLinkProbability = 0.2
bs_learner.maxTime = 3600*2
bs_learner.Learn(ds, learnedBSNetwork)
learnedBSNetwork.WriteFile("bs_learned_4_very_dense.xdsl")
///
