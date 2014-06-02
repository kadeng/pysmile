%module pysmile
%{
/* Includes the header in the wrapper code */
#include "smile.h"
#include "smilearn.h"
%}


// basic data structures
%include "dslobject.h"
%include "nodedef.h"
%include "nodeval.h"
%include "cidefinition.h"
%include "intarray.h"
%include "doublearray.h"
%include "dmatrix.h"
%include "syscoord.h"
%include "generalclases.h"
// network structure
%include "network.h"
%include "node.h"
%include "submodel.h"
%include "simplecase.h"
%include "errorstrings.h"
%include "progress.h"

// supported node definition classes
%include "defcpt.h"
%include "deftruthtable.h"
%include "defnoisymax.h"
%include "defnoisyadder.h"
%include "deflist.h"
%include "deftable.h"
%include "defmau.h"
// %include "defdemorgan.h"
%include "defequation.h"

// supported node value classes
%include "valbeliefvector.h"
%include "vallistofdecisions.h"
%include "valexpectedutility.h"
%include "valmauexpectedutility.h"
%include "valequationevaluation.h"
%include "errors.h"
%include "errorstrings.h"
// voi
%include "valueofinfo.h"

// sensitivity
// %include "sensitivity.h"

// define SMILE_NO_DIAGNOSIS before including smile.h
// to skip diag-related functionality
%include "diag_network.h"
%include "nodecost.h"
%include "extradefinition.h"
%include "caselibrary.h"

// SMILEARN

%include "dataset.h"
%include "discretizer.h"
%include "naivebayes.h"
%include "greedythickthinning.h"
%include "essentialsearch.h"
%include "bs.h"
%include "tan.h"
%include "pc.h"
%include "em.h"
%include "validator.h"
%include "datagenerator.h"
%include "pattern.h"
%include "dbcml.h"



;