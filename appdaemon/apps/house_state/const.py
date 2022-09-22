from enum import IntEnum

DAY_ACTIONS ={
     'TV':1
    ,'EATING':2
}


HOME_STATES={
     'DAY':DAY_ACTIONS
    ,'NIGHT':1
}

MAIN_STATES = {
     'HOME':HOME_STATES
    ,'AWAY':1
    ,'VACATION':2
}
