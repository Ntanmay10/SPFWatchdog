import dns.resolver

def check_spf(domain):
    try:
        resolver = dns.resolver.Resolver()
        resolver.nameservers = ['8.8.8.8', '8.8.4.4']
        
        result = resolver.resolve(domain, 'TXT')
        
        for txt_record in result:
            record = str(txt_record).strip('"')
            if record.startswith('v=spf1'):
                return record
        
        return "No SPF record found for this domain."

    except dns.resolver.NoAnswer:
        return "No DNS records found for the domain."
    except dns.resolver.NXDOMAIN:
        return "Domain does not exist."
    except Exception as e:
        return f"An error occurred: {e}"

domain = input("Enter the domain to check SPF record: ")
spf_record = check_spf(domain)
print(f"SPF Record for {domain}: {spf_record}")