import time

def performance_check(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        processing_time = (end_time - start_time) * 1000
        print('==============================')
        print(f'Function: {function.__name__}')
        print('Processing time: %.4f ms' % processing_time)
        print('==============================')
        return result
    return wrapper
