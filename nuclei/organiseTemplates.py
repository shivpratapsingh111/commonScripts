import os
import yaml
import shutil
import argparse
import sys
import textwrap

def usage():
    print("Examples:")
    print(f"\n[+] Provide file with `-i` flag containing `id` to exclude, one per line: \n\t- {sys.argv[0]} -dir /home/nuclei-templates -i ids.txt")
    print(f"\n[+] If you don't provide a file, It will exclude templates set by default:\n\t- {sys.argv[0]} -dir /home/nuclei-templates\n")

def get_ids_from_file(file_path):
    with open(file_path, 'r') as f:
        ids = f.read().splitlines()
    return ids

def move_matching_files(directory, ids, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.yaml') or file.endswith('.yml'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as yaml_file:
                    try:
                        content = yaml.safe_load(yaml_file)
                        if 'id' in content and content['id'] in ids:
                            shutil.move(file_path, os.path.join(output_dir, file))
                            print(f"Moved: {file_path}")
                    except yaml.YAMLError as exc:
                        print(f"Error parsing {file_path}: {exc}")

def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description='Separate Nuclei Templates files based on ID match.', epilog=textwrap.dedent(f"""Examples:
[+] Provide file with `-i` flag containing `id` to exclude, one per line: 
\t- {sys.argv[0]} -dir /home/nuclei-templates -i ids.txt
[+] If you don't provide a file, It will exclude templates set by default:
\t- {sys.argv[0]} -dir /home/nuclei-templates"""))
    
    
    parser.add_argument('-dir', required=True, help='Directory containing Nuclei Templates files')
    parser.add_argument('-i', required=False, help='File containing nuclei template IDs to exclude, Example: tech-detect, missing-csp, display-via-header')
    
    args = parser.parse_args()
    
    if args.i and args.dir:
        ids = get_ids_from_file(args.i)
        move_matching_files(args.dir, ids, 'separated')
    elif args.dir:
        ids = ["http-missing-security-headers",  "tech-detect",  "missing-csp",  "display-via-header",  "kafka-topics-list",  "cors-misconfig",  "waf-detect",  "dns-waf-detect",  "secui-waf-detect",  "spring-detect",  "favicon-detect",  "akamai-detect",  "akamai-cache-detect",  "missing-sri",  "robots-txt-endpoint",  "aws-detect",  "aws-cloudfront-service",  "https-to-http-redirect",  "caa-fingerprint",  "dns-saas-service-detection",  "mx-fingerprint",  "txt-fingerprint",  "tls-version",  "spf-record-detect",  "nameserver-fingerprint",  "dnssec-detection",  "mx-service-detector",  "dmarc-detect",  "php-user-ini",  "weak-cipher-suites",  "ssl-issuer",  "ssl-dns-names",  "wildcard-tls",  "minecraft-enum",  "request-based-interaction",  "oidc-detect",  "security-txt",  "rdap-whois",  "options-method",  "robots-txt",  "apple-app-site-association",  "external-service-interaction",  "azure-domain-tenant",  "old-copyright",  "intercom",  "metatag-cms",  "xss-deprecated-header",  "addeventlistener-detect",  "deprecated-tls",  "erlang-daemon",  "mismatched-ssl-certificate",  "pop3-detect",  "google-floc-disabled",  "aws-cloudfront-service",  "aws-bucket-service",  "detect-sentry",  "email-extractor",  "http-trace",  "apache-detect",  "revoked-ssl-certificate",  "expired-ssl",  "microsoft-iis-version",  "fingerprinthub-web-fingerprints",  "public-documents",  "google-frontend-httpserver",  "wadl-api",  "nginx-version",  "openssh-detect",  "insecure-cipher-suite-detect",  "generic-c2-jarm",  "kafka-topics-list",  "openresty-detect",  "gpc-json",  "wordpress-readme-file",  "wp-user-enum",  "aws-sftp-detect",  "wordpress-wordpress-seo",  "wordpress-post-types-order",  "wordpress-maintenance",  "wordpress-login",  "wordpress-redirection",  "wordpress-svg-support",  "wordpress-xmlrpc-listmethods",  "untrusted-root-certificate",  "switch-protocol",  "sitemap-detect"]
        move_matching_files(args.dir, ids, 'separated')        
    else: 
        print("Incorreect use of flags!")
        sys.exit(1)

if __name__ == "__main__":
    main()


# commands to filterout more by searching on some results
'''cat info.txt |grep -v dns-saas-service-detection | grep -v tls-version | grep -v mx-finger | grep -v txt-finger | grep -v caa-finger | grep -v dmarc-dete | grep -v mx-service-dete | grep -v dnssec-dete | grep -v spf-record | grep -v nameserver-finger | grep -v ssl-dns-names | grep -v ssl-issuer | grep -v wildcard-tls | grep -v minecraft-enum | grep -v request-based-interaction | grep -v waf-detect | grep -v oidc-detect | grep -v cors-miscon | grep -v missing-sri| grep -v security-txt | grep -v rdap-whois | grep -v robots-txt-endpoint | grep -v robots-txt | grep -v options-method | grep -v apple-app-site-association | grep -v aspx-debug-mode | grep -v exposed-gitignore | grep -v external-service-interaction| grep -v keycloak-openid-config | grep -v mercurial-hgignore  | grep -v http-missing-security-headers | grep -v azure-domain-tenant | grep -v intercom | grep -v old-copyr | grep -v tech-dete | grep -v azure-domain-ten | grep -v aws-dete  | grep -v metatag | grep -v missing-csp | grep -v addeventlistener-detect | grep -v display-via-header | grep -v xss-depre | grep -v deprecated-tls | grep -v pop3 | grep -v s3-detect| grep -v google-floc-disabled | grep -v default-nginx-page | grep -v aws-bucket-service | grep -v aws-cloudfront-service | grep -v akamai-detect | grep -v akamai-cache | grep -v favicon-detec | grep -v detect-sentry | grep -v http-trace | grep -v apache-detect | grep -v email-extract | grep -v cookies-without-httponly-secure | grep -v form-detection | grep -v https-to-http-redirect | grep -v dangling-cname | grep -v basic-auth-detect | grep -v microsoft-iis-version | grep -v insecure-cipher-suite-det | grep -v openssh-detect | grep -v generic-c2-jarm | grep -v kafka-topics-list | grep -v spring-detect | grep -v fingerprinthub-web-fingerprints| grep -v openresty-detect | grep -v wordpress-readme-file | grep -v gpc-json | grep -v nginx-version | grep -v wordpress-wordpress-seo | grep -v aws-sftp-detect | grep -v wordpress-post-types-order | grep -v wordpress-detect


cat low.txt | grep -v php-user-ini | grep -v weak-cipher-suites | grep -v erlang-daemon | grep -v mismatched-ssl-certificate | grep -v expired-ssl | grep -v revoked-ssl-certificate | grep -v wp-user-enum | grep -v untrusted-root-certificate
'''