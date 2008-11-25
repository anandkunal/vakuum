# Primitive memcached locking
# Using memcache itself to store semaphores

import cPickle
import memcache

class MemcacheWrapper:
    def __init__(self): 
        pass
        
    def begin_update(self, key):
        if not mc.get("conch-%s" % (key)):
            # Storing epoch or a guid (verification) may be better
            mc.set("conch-%s" % (key), 1)
            print "Yay! You can update!"
            return True
        else:
            print "Nay...you need to wait, or do something creative."
            return False

class Person:
    def __init__(self, name):
        self.name = name

mc = memcache.Client(['127.0.0.1:11211'], debug=0)
mc.flush_all()

# Set the initial cache key/value
kunal = Person("Kunal Anand")
mc.set("kunal", cPickle.dumps(kunal))

# Try retrieving one for an update
mw = MemcacheWrapper()
mw.begin_update("kunal")
mw.begin_update("kunal")
mw.begin_update("non_existent_cache_item")