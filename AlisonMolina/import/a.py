#print("from a")
#import b

#b.impl1()

#import b
from b import impl1 as fn

import b as otro

def impl1():
    print("hello from b")
    
fn()
otro.impl1()
## uk = b.Ukelele()