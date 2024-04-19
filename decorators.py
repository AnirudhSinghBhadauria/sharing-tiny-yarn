# Time it took to execute the funciton
import time

# These are like higher order funcitons in js
# These are very commonly used in django

# Example 1

# def timer(func):
#      def wrapper(*args, **kwargs):
#           start = time.time()
#           result = func(*args, **kwargs)
#           end = time.time()
#           total_time = round(end-start, 2)
#           print(func.__name__, 'ran in', total_time, 'time')
#           return result
#      return wrapper

# @timer  # Decorator - now this method will pass through timer function before running itself
# def example_function(n):
#      time.sleep(n)

# example_function(2)

# Example 2

# def debug(func):
#      def wrapper(*args, **kwargs):
#           args_value = ', '.join(str(arg) for arg in args)
#           kwargs_value = ', '.join(f"{k}:{v}" for k,v in kwargs.items())
#           print(f"Calling: {func.__name__} with args {args_value} and {kwargs_value}")
#           result = func(*args, **kwargs)
#           return result
#      return wrapper

# @debug
# def greet(name, greeting="Hello"):
#      print(f"{greeting}, {name}")


# Example 3 - Caching

def cache(func):
     cache_value = {}
     print(cache_value)
     def wrapper(*args, **kwargs):
          if args in cache_value:
              return cache_value[args] 
          result = func(*args, **kwargs)
          # Saving the value of resuslt in cache dict
          cache_value[args] = result
          return result
         
     return wrapper

@cache
def long_running_function(a, b):
     time.sleep(4)
     return a + b

print(long_running_function(2,3))
print(long_running_function(2,3))