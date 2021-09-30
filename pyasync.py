import queue

def output (s):
    print (s)

def fatalError ():
    print ("FATAL ERROR");


class component:
    def __init__ (self, name):
        self.inqueue = queue.LifoQueue ()
        self.name = name

    def enqueue (self, data):
        self.inqueue.put (data)

    def dequeue (self):
        return self.inqueue.get ()
        
    def empty_queue (self):
        print ("empty_queue")
        print (self.inqueue.empty ())
        return self.inqueue.empty ()
 
    def exec_once (self):
        print ("exec once")
        data = self.dequeue ()
        print (data)
        self.func (data)

    def send (self, data):
        self.connected_to.enqueue (data)

def C (x):
    print ("C")
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
    print ("B")
    if (x == "q"):
        self.send ("s")
    elif (x == "r"):
        self.send ("t")
    else:
        fatalError ()

def make_B (target):
    comp = component ("B")
    comp.connected_to = target
    comp.func = B
    return comp


def make_C ():
    comp = component ("C")
    comp.func = C
    return comp

class Dispatcher:
    def __init__ (self):
        self.component_list = queue.SimpleQueue ()

    def exec (self):
        componentlis = self.component_list
        print ("disp.exec " + str (self.component_list.qsize ()) + " " + str (componentlis.qsize ()))
        while (not componentlis.empty ()):
            cmponent = componentlis.get ()
            print ("disp exec 1 " + cmponent.name)
            print (cmponent.inqueue.qsize ())
            if (not cmponent.empty_queue () ):
                print ("disp exec 2 " + cmponent.name)
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
        print ("disp.initialize size=" + str (self.component_list.qsize ()))
        self.component_list.put (Component1)
        print ("disp.initialize size=" + str (self.component_list.qsize ()))
        self.component_list.put (Component2)
        print ("disp.initialize size=" + str (self.component_list.qsize ()))
        print ("disp.initialize " + str (self.component_list.qsize ()));

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
