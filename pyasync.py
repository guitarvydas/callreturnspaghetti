import queue

def output (s):
    print (s)

def fatalError ():
    print ("FATAL ERROR");


class component:
    def __init__ (self):
        self.inqueue = queue.SimpleQueue ()

    def enqueue (self, data):
        self.inqueue.put (data)

    def dequeue (self):
        self.inqueue.get ()
        
    def empty_queue (self):
        print ("empty_queue")
        print (self.inqueue.empty ())
        return self.inqueue.empty ()
 
    def exec_once (self):
        print ("exec once")
        data = self.dequeue ()
        self.func (data)

    def send (self, data):
        self.connected_to.enqueue (data)

def C (x):
    if (x == "q"):
        output ("v")
    elif (x == "r"):
        output ("w")
    elif (x == "s"):
        output ("x")
    elif (x == "t"):
        output ("y")
    elif (x == "u"):
        output ("z")
    else:
        fatalError ()

def B (x):
    if (x == "q"):
        self.send ("s")
    elif (x == "r"):
        self.send ("t")
    else:
        fatalError ()

def make_B (target):
    comp = component ()
    comp.connected_to = target
    comp.func = B
    return comp


def make_C ():
    comp = component ()
    comp.func = C
    return comp

class Dispatcher:
    def __init__ (self):
        self.component_list = queue.LifoQueue ()

    def exec (self):
        print ("disp exec 0")
        q = self.component_list
        while (not q.empty ()):
            print ("disp exec 1")
            cmponent = q.get ();
            if (not cmponent.empty_queue):
                cmponent.exec_once ()

    def nothing_to_do (self):
        q = self.component_list
        while (not q.empty ()):
            c = q.get ();
            if (not c.empty_queue ()):
                return False
        return True
            
    def initialize (self):
        Component2 = make_C ();
        Component1 = make_B (Component2);
        self.cB = Component2
        self.cC = Component1
        self.component_list.put (Component1);
        self.component_list.put (Component2);

    def get_B (self):
        return self.cB

    def get_C (self):
        return self.cC

def fasync1 ():
    print ("fasync1")
    dsptchr = Dispatcher ()
    dsptchr.initialize ()
    componentB = dsptchr.get_B ()
    componentC = dsptchr.get_C ()
    componentB.enqueue ("q")
    componentC.enqueue ("q")
    while (not dsptchr.nothing_to_do ()):
        print ("fasync1 2")
        dsptchr.exec ()

def fasync2 ():
    print ("fasync2")
    dsptchr = Dispatcher ()
    dsptchr.initialize ()
    componentB = dsptchr.get_B ()
    componentC = dsptchr.get_C ()
    componentC.enqueue ("q")
    componentB.enqueue ("q")
    while (not dsptchr.nothing_to_do ()):
        dsptchr.exec ()

fasync1 ()
# fasync2 ()
