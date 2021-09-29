function output (s) {
    console.log (s);
}

function fatalError () {
    console.log ("FATAL ERROR");
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

function codeV1 () {
    B ("q");
    C ("q");
}

function codeV2 () {
    C ("q");
    B ("q");
}    

function sync () {
    console.log ("Version 1");
    codeV1 ();
    console.log ("Version 2");
    codeV2 ();
}

sync ();

