#
#  Configure security
#
#
#
#    2023-09-21    Tom Bosmans (tom.bosmans@be.ibm.com)
#
import java.lang.System as system
import time
import os
print("Enable trust association")
AdminTask.configureTrustAssociation('-enable true')
print(AdminTask.listInterceptors())
print("Configure OIDCRP TAI")
AdminTask.configureInterceptor('[-interceptor com.ibm.ws.security.oidc.client.RelyingParty \
                                 -customProperties ["provider_1.useJwtFromRequest=required",\
                                                    "provider_1.identifier=isamjwt",\
                                                    "provider_1.issuerIdentifier=https://issuer"]]')
AdminConfig.save()
print("Saved configuration")