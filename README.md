---
# Read me

This repository contains demo material , as referenced as a blog entry on <https://www.gwbasics.be/2023/09/websphere_with_jwt_junction.html>


## ContainerFile

The Docker ContainerFile to build the WebSphere container , based on <icr.io/appcafe/websphere-traditional:latest>

## config

The predefined password for the wsadmin user.

## files

The public certificates used in my example setup ( the certificate of the webseal server and the signer certificat of the jwt)

## scripts

A number of Jython scripts that install the OIDCRP and DefaultApplication applications,
and configure the security of the WebSphere container.