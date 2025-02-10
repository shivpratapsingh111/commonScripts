import json
with open('records.json', 'r') as file:
    data = json.load(file)

def extract_domains_with_anonymised_email(data):
    domains_with_anonymised_email = []
    
    whois_records = data.get("whoisRecords", {})
    for domain, details in whois_records.items():
        whois_record = details.get("whoisRecord", {})
        registrant_email = whois_record.get("Registrant Email", "")
        admin_email = whois_record.get("Admin Email", "")
        tech_email = whois_record.get("Tech Email", "")
        
        if ("anonymised.email" in registrant_email if registrant_email else False) or \
           ("anonymised.email" in admin_email if admin_email else False) or \
           ("anonymised.email" in tech_email if tech_email else False):
            domains_with_anonymised_email.append(domain)
    
    return domains_with_anonymised_email

# Extract domains
domains = extract_domains_with_anonymised_email(data)
for domain in domains:
    print(domain)