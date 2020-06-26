<h1>Python DEBUG function</h1>

<h5>This function is used to make one line debug statemts.</h5>
<br>
<p>Example statement and the output</p>

```
# debugginig on?
dbg = True

a = 12
b = { "x":tuple, "list":list("1,2,3") }

DEBUG(dbg, (""b["x"]"", b["x"]), ("a =", a))

# OUT:
# time; filename; func_name; our input
9:13:11 <stdin>:1 <module> | b["x"] <class 'tuple'>
9:13:11 <stdin>:1 <module> | a = 12

```
#### More advanced

<p>In order to better control which debug statements will be printed out</p>

```

# debugging on?
dbg = True

# What do you want to debug?
ls_dbg = ["Code_in_list"]

smth = 12
smth2 = 142

# wont be printed out
DEBUG(dbg, ("smth", smth), debug_code="Not_in_ls", debug_codes=ls_dbg )

# This will be printed out
DEBUG(dbg, ("smth2", smth2), debug_code="Code_in_list", debug_codes=ls_dbg )



>>> OUT <<<
9:49:41 <stdin>:2 <module> | smth2 142

```
