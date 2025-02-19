# 0x05. Processes and signals
## Resources
* [Linux PID](https://www.linfo.org/pid.html)
* [Linux process](https://www.thegeekstuff.com/2012/03/linux-processes-environment/)
* [Linux signal](https://www.educative.io/answers/what-are-linux-signals)
* [Process management in linux](https://www.digitalocean.com/community/tutorials/process-management-in-linux)
* [Linux signals](https://www.computerhope.com/unix/signals.htm)
* [&](https://bashitout.com/2013/05/18/Ampersands-on-the-command-line.html)
* [init.d](https://www.ghacks.net/2009/04/04/get-to-know-linux-the-etcinitd-directory/)
* [Daemon](https://en.wikipedia.org/wiki/Daemon_%28computing%29)
* [Positional parameters](https://www.gnu.org/software/bash/manual/html_node/Positional-Parameters.html)
* [What a zombie process is](https://zombieprocess.wordpress.com/what-is-a-zombie-process/)

### Linux commands
* `ps`(Process Status):
`ps` is a command used to display information about running processes on a Linux system. It provides a snapshot of the currently executing processes, including their process IDs (PIDs), CPU and memory usage, and more. It's a handy tool for monitoring and troubleshooting system activity.
* `pgrep`(Process Grepper):
`pgrep` is a command used to search for and list the process IDs of running processes that match a specified pattern or criteria. It's a useful tool for finding processes by their names or other attributes, which can be helpful for automation or when you need to kill specific processes.
* `pkill`(Process Kill):
`pkill` is a command that allows you to send signals to and terminate processes based on their names or other attributes. It's a convenient way to stop one or more processes without needing to know their PIDs individually.
* `kill`:
`kill` is a command used to send signals to processes. By default, it sends the **TERM** (terminate) signal, which requests a process to gracefully exit. It can used with a specific PID or process name to send signals like **SIGTERM**, **SIGKILL**, or others to control processes effectively.
* `exit`:
`exit` is a shell command used to exit the current shell or terminal session. When `exit` is run, it terminates the shell session, logging you out if you are in a remote connection. It's used to close the current shell or exit a script when its execution is complete.
* `trap`:
`trap` is a shell command that allows you to set up signals and actions to be executed when those signals are received by a script or shell. It's used for signal handling and can be used to ensure clean-up actions or specific responses when a script or program receives certain signals, such as **SIGINT** (interrupt) or **SIGTERM** (terminate).
## General
* **PID (Process ID)**
A PID, or Process ID, is a unique numerical identifier assigned to each running process on a Unix-like operating system, including Linux. It helps the operating system keep track of and manage processes. PIDs are essential for identifying and interacting with processes.
* **Process**:
A process is an independent program or task that is running on a computer's operating system. It has its own memory space and system resources, such as CPU and I/O devices. Each process performs a specific function and operates independently of other processes. Processes are the building blocks of multitasking and allow multiple programs to run concurrently on a system.
* **How to Find a Process' PID:**
There are several ways to find a process's PID:
- `ps` **Command**: The `ps` command to list all processes along with their PIDs.
- `pgrep` **Command**: `pgrep` followed by the process name will find the PID of a specific process.
- `pidof` **Command**: `pidof` followed by the process name will find the PID of a specific process.
* **How to Kill a Process**:
You can terminate a process using the `kill` command followed by the PID of the process you want to kill. By default, `kill` sends the **TERM** (terminate) signal, but you can specify other signals as well.
* **Signal:**
A signal is a software interrupt delivered to a running process to notify it of a specific event or request. Signals are used to control and communicate with processes. They can instruct a process to take a particular action, such as terminating gracefully or reloading its configuration. Signals are identified by names or numeric values.
* **The 2 Signals That Cannot Be Ignored:**
There are two signals that cannot be ignored or caught by a process:
- **SIGKILL (9)**: `Signal 9`, known as **SIGKILL**, is a forceful termination signal. It immediately and unconditionally kills a process without allowing it to clean up or save any data.
- **SIGSTOP (19)**: `Signal 19`, known as **SIGSTOP**, is used to pause a process. Unlike other signals, a process stopped with **SIGSTOP** cannot be resumed until it receives a **SIGCONT** signal, which instructs it to continue executing.
