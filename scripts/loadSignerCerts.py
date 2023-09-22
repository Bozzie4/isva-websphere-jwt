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
print("Importing ISVA certificates")
AdminTask.addSignerCertificate(['-keyStoreName', 'NodeDefaultTrustStore',
                                '-certificateAlias', 'default',
                                '-certificateFilePath', '/tmp/isam_rp.cer',
                                '-base64Encoded', 'true'])
AdminTask.addSignerCertificate(['-keyStoreName', 'NodeDefaultTrustStore',
                                '-certificateAlias', 'signer',
                                '-certificateFilePath', '/tmp/signer.cer',
                                '-base64Encoded', 'true'])
AdminConfig.save()