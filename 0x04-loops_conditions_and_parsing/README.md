# 0x04. Loops, conditions and parsing
## Resources
### Read or watch:
* [Loops sample](https://www.tldp.org/LDP/Bash-Beginners-Guide/html/sect_09_01.html)
* [Variable assignment and arithmetic](https://tldp.org/LDP/abs/html/ops.html)
* [Comparison operators](https://tldp.org/LDP/abs/html/comparison-ops.html)
* [File test operators](https://tldp.org/LDP/abs/html/fto.html)
* [Make your scripts portable](https://www.cyberciti.biz/tips/finding-bash-perl-python-portably-using-env.html)
### man or help:
* `env`
* `cut`
* `for`
* `while`
* `until`
* `if`
## General
* How to create SSH keys
* What is the advantage of using `#!/usr/bin/env bash` over `#!/bin/bash`
* How to use `while`, `until` and `for` loops
* How to use `if`, `else`, `elif` and `case` condition statements
* How to use the `cut` command
* What are files and other comparison operators, and how to use them
## Shellcheck
[Shellcheck](https://github.com/koalaman/shellcheck) is a tool that helps the user write proper Bash scripts. It makes recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about.
Here is how to [install it](https://github.com/koalaman/shellcheck#installing).
Examples:
Not passing `Shellcheck`:
![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/251/Vxotqyj.png)
Passing `Shellcheck`:
![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/251/ubHWxDU.png)
<font size="1"> For every feedback, Shellcheck will provide a code that can be used to get more information about the issue, for example for code `SC2034`, you can browse [https://github.com/koalaman/shellcheck/wiki/SC2034](https://github.com/koalaman/shellcheck/wiki/SC2034).</font>
