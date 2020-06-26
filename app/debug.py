import sys
from inspect import getframeinfo, stack
from datetime import datetime

    
def DEBUG(BOOLEAN, *args, **kwargs):
    """BOOLEAN, ("cos tam :", zmienna), ("-- cos tam2:", zmienna2), debug_code=, debug_codes=
    if no (debug_codes or debug_code) then just the booleans"""
    if BOOLEAN:
        caller = getframeinfo( stack()[1][0] )
        time = datetime.now()
        time_str = "{}:{}:{} ".format( time.hour, time.minute, time.second )
        
        # if list of debug_codes and debug_code of statement are present function will be run
        if kwargs and "debug_code" in kwargs and "debug_codes" in kwargs:
            
            # if both are present we will check if debug_code is present
            if kwargs["debug_code"] in kwargs["debug_codes"]:
                try:
                    name = sys._getframe(1).f_code.co_name
                except (IndexError, TypeError, AttributeError):
                    name = "<unknown>"
                for data in args:
                    try:
                        print(time_str, caller.filename.split("\\")[-1], ":", caller.lineno," ", name, end=" | ", sep="")
                        
                        if type(data) == tuple:     # example: 
                            print(*data)            # 10:12:333 models.py | smth1 smth2 smth3 ...
                        
                        elif type(data) == list:
                            for something in data:
                                print(time_str, caller.filename.split("\\")[-1], ":", caller.lineno," ", name, end=" | ", sep="")
                                                    # example:
                                print(something)    # 10:12:333 models.py | smth1
                                                    # 10:12:333 models.py | smth2
                                                    # 10:12:333 models.py | smth3
                                                    # 10:12:333 models.py |  ...
                    except:
                        print(time_str, caller.filename.split("\\")[-1], ":", caller.lineno," ", name, end=" | ", sep="")
                        print(data)
        
        # if there is no list of debug_codes or debug_code, only BOOLEAN will be considered
        else:
            try:
                name = sys._getframe(1).f_code.co_name
            except (IndexError, TypeError, AttributeError):
                name = "<unknown>"
            for data in args:
                try:
                    print(time_str, caller.filename.split("\\")[-1], ":", caller.lineno," ", name, end=" | ", sep="")
                    
                    if type(data) == tuple:     # example: 
                        print(*data)            # 10:12:333 models.py | smth1 smth2 smth3 ...
                    
                    elif type(data) == list:
                        for something in data:
                            print(time_str, caller.filename.split("\\")[-1], ":", caller.lineno," ", name, end=" | ", sep="")
                                                # example:
                            print(something)    # 10:12:333 models.py | smth1
                                                # 10:12:333 models.py | smth2
                                                # 10:12:333 models.py | smth3
                                                # 10:12:333 models.py |  ...
                except:
                    print(time_str, caller.filename.split("\\")[-1], ":", caller.lineno," ", name, end=" | ", sep="")
                    print(data)



"""Lista z kodami debugowania debug_codes_ls = ["sch_lj1", "Stdnt_jzd10"]
kiedy wolamy DEBUG(debugowanie_bool, ("wartosc_czegos", ta_zmienna_wartosci), debug_codes=debug_code_ls, debug_code="Sch_lj1")
Kiedy nie checmy tego to wywalamy z debug_codes_ls ten string"""













