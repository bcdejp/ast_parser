#include "type.h"

#define STATE_INT   (0)
#define STATE_001   (1)
#define STATE_002   (2)
#define STATE_XXX   (9)

static U4 state;
U4 global;

static void target_function_s_001(void);

/* 内部変数の初期化関数 */
U4 target_function_init(){
    state = STATE_INT;
    global = STATE_002;
    return 0;
}

/* 内部変数の参照 */
U4 target_fuction_001(U4 x, U4 y){
    U4 ret;
    if(state == STATE_INT){
        ret = x + y;
    } else if(state == STATE_001){
        ret = x -y;
    } else {
        ret = 0;
    }
    return(ret);
}

void target_function_002(void){
    target_function_s_001();
    return;
}

/* 内部変数の更新 */
static void target_function_s_001(void){
    state = STATE_XXX;
}
