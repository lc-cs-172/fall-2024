# Note 07

## The call stack

When your program calls a function, the program's execution pauses at the
calling point, the function executes until it returns, and then execution
resumes where it left off in the program. Behind the scenes, a structure called
a call frame keeps track of where you are in each function as well as any local
variables.
