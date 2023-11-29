# mailcheck
a comprehensive tool for validating email addresses from a CSV file. The script includes functions for checking various aspects of email addresses, ensuring their legitimacy and functionality. Here's an overview of its components and functionalities, rewritten using Markdown:

Python Script Overview: Email Address Validation
1. check_mx_records(domain)
Purpose: Checks for MX (Mail Exchange) records of a domain.
Method: Utilizes dns.resolver.resolve().
Returns: True if MX records exist, False otherwise.
2. check_spf_records(domain)
Purpose: Verifies SPF (Sender Policy Framework) records of a domain.
Functionality: Detects email sender address forgery.
Returns: True if SPF records are found, False otherwise.
3. check_dkim_records(domain)
Purpose: Examines DKIM (DomainKeys Identified Mail) records of a domain.
Functionality: Ensures email authenticity and unchanged content in transit.
Returns: True if DKIM records exist, False otherwise.
4. check_website(domain)
Purpose: Checks website accessibility.
Ports Checked: 80, 443, 8080.
Returns: "Web OK" if accessible, "Web not found" otherwise.
5. validate_emails(file_path)
Function: Processes a CSV file of email addresses.
Validation Steps:
Validates email format using regular expressions.
Performs checks for MX, SPF, DKIM records, and website accessibility.
Criteria: At least three checks must pass.
Output: Writes "ok" or "fail" in the last CSV column.
Result File: 'valid_emails.csv'.
The script is optimized for processing large lists of email addresses, efficiently handling memory by clearing the list of validated emails after each entry is processed.
