
#include "pysmile_helper.h"

DSL_intArray *newDSL_intArray(int size) {
	return new DSL_intArray(size);
}

DSL_doubleArray *newDSL_doubleArray(int size) {
	return new DSL_doubleArray(size);
}

DSL_stringArray *newDSL_stringArray(int size) {
	return new DSL_stringArray(size);
}

DSL_idArray *newDSL_idArray(int size) {
	return new DSL_idArray(size);
}

