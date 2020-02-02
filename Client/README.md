# Multithread POST client (MTPC)
Simple multithreaded number generator that sends data to a given endpoint.  
No external dependencies, small footprint and snapped for compatibility and maintainability!

## Building snap package
`snap install snapcraft --classic`  
`snap install multipass`

Inside the root dir execute the following:  
`snapcraft`  
`snap install --devmode mtpc_1.0_all.snap`

### Running
After the snap is installed, it can be executed with the `mtpc` command.

#### FAQ
Q: Multipass fails with `exit code 2.`.  
A: Check you have the right permissions.

Q: Multipass hangs/timeout.  
A: Check firewall rules for multipass virtual network.