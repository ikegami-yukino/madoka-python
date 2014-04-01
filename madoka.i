%module madoka

typedef unsigned int uint32_t;
typedef unsigned long long uint64_t;

%typemap(in) void * = char*;
%typemap(in) const void * = char*;
%apply (char *STRING) { (const void *)}

%{
#include "src/util.h"
#include "src/exception.h"
#include "src/sketch.h"
#include "src/file.h"
#include "src/header.h"
#include "src/approx.h"
#include "src/random.h"
#include "src/croquis.h"
#include "src/hash.h"
%}

%include "src/util.h"
%include "src/exception.h"
%include "src/sketch.h"
%include "src/croquis.h"
%template(CroquisUint8) madoka::Croquis<unsigned char>;
%template(CroquisUint16) madoka::Croquis<unsigned short>;
%template(CroquisUint32) madoka::Croquis<unsigned int>;
%template(CroquisUint64) madoka::Croquis<unsigned long long>;
%template(CroquisFloat) madoka::Croquis<float>;
%template(CroquisDouble) madoka::Croquis<double>;
