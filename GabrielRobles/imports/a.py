#import b

#from b import implementacion1
from b import implementacion1 as fn

import b as otro

def implementacion1():
    print("hello from b")
fn()
#implementacion1()
otro.implementacion1()

#uk = b.Ukulele()