# OKD Flask App
This implementation uses Minishift CLI tools and VirtualBox for OKD cluster and app deployment.

### Deployment with OKD

1. Create an OKD project. Browse catalog and choose a Python project. Use this repository's HTTPS link as the source.

2. Build and deploy the cluster.

3. Open the .nip.io link OKD gives you to view your app in the browser. If "Hello, World!" appears, the deployment was successful.

4. Now, add /other to the end of the URL. A different message should appear. This demonstrates the implementation of routes.



### Troubleshooting
**"Could not set oc CLI context for 'minishift' profile"
"Error starting the VM"**

Known Causes: Updating VirtualBox

Workaround:
$ minishift delete --force //Must use --force flag. Regular minishidt delete does NOT work
$ rm -rf ~/.minishift
$ minishift setup-cdk //If this command does not work, proceed to the next 
$ minishift config set vm-driver virtualbox
$ minishift start


**"Cannot set oc CLI context"**

Unknown Cause

Workaround:
$ oc login
If prompted for server, enter the web console url without the '/console' attached at the end. Continue through prompts.
