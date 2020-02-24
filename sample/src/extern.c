#include "type.h"
#include "extern.h"

U1 extern_check_value(U1 x){
    U1 ret = 0;
    if(x > 0){
        ret = 10;
    }
    return ret;
}

U4 extern_get_value(U1* x){
    U4 ret = 0;
    *x = *x + 1;
    return ret;
}
