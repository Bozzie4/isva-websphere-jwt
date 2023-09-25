#
#  Load certificates
#
#
#
#    2023-09-21    Tom Bosmans (tom.bosmans@be.ibm.com)
#
import java.lang.System as system
import time
import os
print("+++++++++++++++++++++++++++++++++++++++")
print("Importing ISVA certificates")
print("+++++++++++++++++++++++++++++++++++++++")
AdminTask.addSignerCertificate(['-keyStoreName', 'NodeDefaultTrustStore',
                                '-certificateAlias', 'default',
                                '-certificateFilePath', '/tmp/isam_rp.cer',
                                '-base64Encoded', 'true'])
print("+++++++++++++++++++++++++++++++++++++++")
print("\nThis next signer should not be necessary, but the OIDCRP TAI does not work with the jwks local-app in WebSeal\n")
print("+++++++++++++++++++++++++++++++++++++++")
AdminTask.addSignerCertificate(['-keyStoreName', 'NodeDefaultTrustStore',
                                '-certificateAlias', 'signer',
                                '-certificateFilePath', '/tmp/signer.cer',
                                '-base64Encoded', 'true'])
AdminConfig.save()