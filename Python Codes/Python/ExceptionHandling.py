def divide(a,b):
    try:
        return (a/b)
    except TypeError:
        return('invalid value - TypeError')
    except NameError:
        return('invalid parameter - NameError')
    except ZeroDivisionError:
        return('ZeroDivisionError occurred')
    except Exception as e:
        return (e)
    else:
        print('Execution faced no exceptions.')
    finally:
        print('Execution finished.')
    
def add(a,b):
    try:
        if isinstance(a,int) or isinstance(a,float) and (isinstance(b,int) or isinstance(b,float)):
            return (a+b)
    except TypeError:
        return('invalid value')
    except NameError:
        return('invalid parameter')
    except Exception as e:
        return (e)
    else:
        print("success")
    finally:
        print("end")
    
print(divide('1',0));  #invalid value - TypeError
print(divide(1,0));  #ZeroDivisionError occurred

print(add(2,1))

'''
# syntax:
try:
    run this code
except: # with condition or not
    execute this code when there is an exception
else:
    no exceptions, run this code
finally:
    always run this code


# except condition code: 
except Exception as e:
    if not condition:
        raise

'''