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
#AdminTask.configureInterceptor('[-interceptor com.ibm.ws.security.oidc.client.RelyingParty \
#                                 -customProperties ["provider_1.useJwtFromRequest=required",\
#                                                    "provider_1.identifier=isamjwt",\
#                                                    "provider_1.issuerIdentifier=https://issuer"]]')
AdminTask.configureInterceptor(['-interceptor', 'com.ibm.ws.security.oidc.client.RelyingParty',
                                '-customProperties', '["provider_1.useJwtFromRequest=required",\
                                                       "provider_1.identifier=isamjwt",\
                                                       "provider_1.issuerIdentifier=https://issuer",\
                                                       "provider_1.interceptedPathFilter=/snoop/.*",\
                                                       "provider_1.filter=request-url%=/snoop/",\
                                                       "provider_1.tokenReuse=true",\
                                                       "provider_1.signVerifyAlias=signer",\
                                                       "provider_1.audiences=ALL_AUDIENCES",\
                                                       "provider_1.setLtpaCookie=true",\
                                                       "provider_1.useRealm=WAS_DEFAULT",\
                                                       "provider_1.useRealm=https://default.verifyaccess.local/jwks.json",\
                                                       "provider_1.signatureAlgorithm=RS256"]'
                                ])
AdminConfig.save()
print("Saved configuration")


|provider_1.useJwtFromRequest|required||
|provider_1.identifier|isvajwt||
|provider_1.issuerIdentifier|https://issuer||
|provider_1.interceptedPathFilter|/snoop/.*||
|provider_1.filter|request-url%=/snoop/||
|provider_1.tokenReuse|true||
|provider_1.signVerifyAlias|signer| The name of the alias, in both the local keystore and jwks.json                        |
|provider_1.audiences|ALL_AUDIENCES| Required                                                                               |
|provider_1.setLtpaCookie|true| This generates an ltpa cookie, so the jwt is only used on the first request            |
|provider_1.useRealm|WAS_DEFAULT| Required, otherwise the authentication fails (it obviously can be any WebSphere domain |
|provider_1.jwkEndpointUrl|https://default.verifyaccess.local/jwks.json||
|provider_1.signatureAlgorithm|RS256||