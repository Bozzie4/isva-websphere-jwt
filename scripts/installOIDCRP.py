#
#  install OIDCRP
#
#
#
#    2023-09-21    Tom Bosmans (tom.bosmans@be.ibm.com)
#
import java.lang.System as system
import time
import os

AdminApp.install('/opt/IBM/WebSphere/AppServer/installableApps/WebSphereOIDCRP.ear',
                 '[ -nopreCompileJSPs -distributeApp -nouseMetaDataFromBinary -nodeployejb -appname WebSphereOIDCRP.ear -createMBeansForResources -noreloadEnabled -nodeployws -validateinstall warn -noprocessEmbeddedConfig -filepermission .*\.dll=755#.*\.so=755#.*\.a=755#.*\.sl=755 -noallowDispatchRemoteInclude -noallowServiceRemoteInclude -asyncRequestDispatchType DISABLED -nouseAutoLink -noenableClientModule -clientMode isolated -novalidateSchema -MapModulesToServers [[ "OIDC Relying Party callback Servlet" com.ibm.ws.security.oidc.servlet.war,WEB-INF/web.xml WebSphere:cell=DefaultCell01,node=DefaultNode01,server=server1 ]] -MapWebModToVH [[ "OIDC Relying Party callback Servlet" com.ibm.ws.security.oidc.servlet.war,WEB-INF/web.xml default_host ]]]' )
AdminConfig.save()