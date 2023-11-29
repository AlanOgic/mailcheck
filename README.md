
# Email Validation Script

This Python script efficiently validates a list of email addresses from a CSV file. It is designed to perform extensive checks on each email address, ensuring their authenticity and functionality.

## Features

- **MX Record Validation**: Confirms the presence of Mail Exchange (MX) records for the domain of each email address.
- **SPF Record Check**: Detects Sender Policy Framework (SPF) records to prevent sender address forgery.
- **DKIM Record Verification**: Assesses DomainKeys Identified Mail (DKIM) records, guaranteeing the email’s source and content integrity.
- **Website Accessibility Test**: Checks if the domain's website is reachable on common ports (80, 443, 8080).

## Functionality

1. **CSV File Reading**: The script processes email addresses from a specified CSV file.
2. **Email Format Validation**: Each email is validated using a regular expression pattern.
3. **Performing Domain Checks**: The script evaluates MX, SPF, DKIM records, and tests website accessibility.
4. **Validity Assessment**: An email is marked as 'valid' if it passes at least three of the above checks.
5. **Output Generation**: Results are recorded in a new CSV file (`valid_emails.csv`), labeling each email as 'ok' or 'fail'.

## Usage

To use the script, simply place your list of email addresses in a CSV file named 'emails.csv' and run the script. Make sure to have the necessary Python dependencies installed (`dns.resolver`, etc.).

```python
# Run the script with the following command
validate_emails('emails.csv')
```

## Optimization

The script is tailored for processing large volumes of email addresses. It optimizes memory usage by clearing the list of validated emails after processing each entry.

