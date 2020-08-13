# list all the nameservers for domain vincilab.co
nslookup -type=NS vincilab.co

# lookup a TXT record
# from https://docs.aws.amazon.com/ses/latest/DeveloperGuide/troubleshoot-verification.html#troubleshoot-verification-domain-dns
nslookup -type=TXT  _amazonses.<domain> <name server>