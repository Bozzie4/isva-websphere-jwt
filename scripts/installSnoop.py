#
#  install defaultApplication (aka Snoop)
#
#
#
#    2023-09-21    Tom Bosmans (tom.bosmans@be.ibm.com)
#
import java.lang.System as system
import time
import os

AdminApp.install('/opt/IBM/WebSphere/AppServer/installableApps/DefaultApplication.ear',
                 '[ -nopreCompileJSPs -distributeApp -nouseMetaDataFromBinary -nodeployejb -appname DefaultApplication.ear -createMBeansForResources -noreloadEnabled -nodeployws -validateinstall warn -noprocessEmbeddedConfig -filepermission .*\.dll=755#.*\.so=755#.*\.a=755#.*\.sl=755 -noallowDispatchRemoteInclude -noallowServiceRemoteInclude -asyncRequestDispatchType DISABLED -nouseAutoLink -noenableClientModule -clientMode isolated -novalidateSchema -MapModulesToServers [[ "Default Web Application" DefaultWebApplication.war,WEB-INF/web.xml WebSphere:cell=DefaultCell01,node=DefaultNode01,server=server1 ]]]' )
AdminConfig.save()

