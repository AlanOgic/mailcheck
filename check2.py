
# import
import csv
import re
import dns.resolver
import socket

# Function to check MX records
def check_mx_records(domain):
    try:
        return bool(dns.resolver.resolve(domain, 'MX'))
    except Exception:
        return False

# Function to check SPF
def check_spf_records(domain):
    try:
        return bool(dns.resolver.resolve(domain, 'TXT'))
    except Exception:
        return False

# Function to check DKIM records
def check_dkim_records(domain):
    try:
        return bool(dns.resolver.resolve(domain, 'TXT'))
    except Exception:
        return False

# Function to check website
def check_website(domain):
    ports = [80, 443, 8080]
    for port in ports:
        try:
            socket.create_connection((domain, port), timeout=10)
            return "Web OK"
        except Exception:
            pass
    return "Web not found"

# Function to validate emails
def validate_emails(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        valid_emails = []
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        for row in reader:
            email = row[0]
            if re.match(pattern, email):
                domain = email.split('@')[1]
                has_mx = check_mx_records(domain)
                has_spf = check_spf_records(domain)
                has_dkim = check_dkim_records(domain)
                web_test_result = check_website(domain)
                tests_passed = sum([has_mx, has_spf, has_dkim, web_test_result == "Web OK"])
                test_result = "ok" if tests_passed >= 3 else "fail"
                if has_mx:
                    valid_emails.append([email, web_test_result, "email address", "MX found", "SPF found" if has_spf else "No SPF", "DKIM found" if has_dkim else "No DKIM", test_result])
                else:
                    valid_emails.append([email, web_test_result, "email address", "No MX found", "SPF found" if has_spf else "No SPF", "DKIM found" if has_dkim else "No DKIM", test_result])
                with open('valid_emails.csv', 'a', newline='') as valid_emails_file:
                    writer = csv.writer(valid_emails_file)
                    writer.writerow(valid_emails[-1])
                valid_emails.clear()

# Replace with the appropriate file path
validate_emails('emails.csv')
