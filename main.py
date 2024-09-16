import dns.resolver
from urllib.parse import urlparse

def get_domain_from_url(url):
    """Extracts the domain from a given URL."""
    parsed_url = urlparse(url)
    return parsed_url.netloc

def get_spf_record(domain):
    """Fetches the SPF record for a given domain."""
    try:
        # Query DNS for TXT records
        answers = dns.resolver.resolve(domain, 'TXT')
        for record in answers:
            for txt_record in record.strings:
                if txt_record.startswith(b"v=spf1"):
                    return txt_record.decode('utf-8')
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        return None
    return None

def main():
    # Get domain from user input
    website_url = input("Enter the website URL: ").strip()
    
    if not website_url:
        print("No URL provided.")
        return
    
    domain = get_domain_from_url(website_url)
    if not domain:
        print("Invalid URL provided.")
        return

    print(f"Domain extracted: {domain}")

    # Fetch SPF record
    spf_record = get_spf_record(domain)
    if spf_record:
        print(f"SPF record for {domain}: {spf_record}")
    else:
        print(f"No SPF record found for {domain}")

if __name__ == "__main__":
    main()
