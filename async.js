function output (s) {
    console.log (s);
}

function fatalError () {
    console.log ("FATAL ERROR");
}


class component {
    constructor () {
	this.inqueue = [];
	this.connected_to = undefined;
	this.func = undefined;
    }

    enqueue (data) {
	this.inqueue.push (data);
    }
    
    dequeue () {
	return this.inqueue.shift ();
    }

    send (data) {
	this.enqueue (data);
    }

    empty_queue () {
	return 0 === this.inqueue.length;
    }
 
    exec_once () {
	let data = this.dequeue ();
	this.func (data);
    }
}

function C (x) {
    if (x === "q") {
	output ("v");
    } else if (x === "r") {
	output ("w");
    } else if (x === "s") {
	output ("x");
    } else if (x === "t") {
	output ("y");
    } else if (x === "u") {
	output ("z");
    } else {
	fatalError ();
    }
}

function B (x) {
    if (x === "q") {
	C ("s");
    } else if (x === "r") {
	C ("t");
    } else {
	fatalError ();
    }
}

function make_B (target) {
    let comp = new component ();
    comp.connected_to = target;
    comp.func = B;
    return comp;
}

function make_C () {
    let comp = new component ();
    comp.func = C;
    return comp;
}

class Dispatcher {
    constructor () {
	this.component_list = [];
    }

    exec () {
	this.component_list.forEach ((cmponent) => {
	    if (cmponent.empty_queue ()) {
	    } else {
		cmponent.exec_once ();
	    }
	})
    }
    
    nothing_to_do () {
	return this.component_list.every (c => { return c.empty_queue (); });
    }

    initialize () {
	let Component2 = make_C ();
	let Component1 = make_B (Component2);
	this.component_list.push (Component1);
	this.component_list.push (Component2);
    }

    get_B () {
	return this.component_list [0];
    }

    get_C () {
	return this.component_list [1];
    }
}

function fasync () {
    let dsptchr = new Dispatcher ();
    dsptchr.initialize ();
    let componentB = dsptchr.get_B ();
    let componentC = dsptchr.get_C ();
    componentB.enqueue ("q");
    componentC.enqueue ("q");
    while (!dsptchr.nothing_to_do ()) {
	dsptchr.exec ();
    }
}

fasync ();
