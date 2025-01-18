# SPF Record Checker

This Python script checks the SPF (Sender Policy Framework) record for a given website URL. SPF records help prevent email spoofing by specifying which mail servers are permitted to send email on behalf of a domain.

## Features

- Extracts the domain from a given URL.
- Fetches and displays the SPF record associated with the domain.
- Generates pdf for the spf record.

## Prerequisites

To run this script, you need Python installed along with the `dnspython` and `fpdf` library. You can install the necessary library using pip:

```
pip install dnspython fpdf
```

## Usage

1. **Run the Script**

   Execute the script from the command line:

   ```
   python spf_checker.py
   ```

2. **Input URL**

   When prompted, enter the website URL for which you want to check the SPF record.

3. **View Results**

   The script will display the extracted domain and the associated SPF record (if available).

## Example

```
Enter the website URL: https://example.com
Domain extracted: example.com
SPF record for example.com: v=spf1 include:_spf.google.com ~all
```

## Error Handling
- **Invalid URL**: If the URL format is incorrect or cannot be parsed, the script will indicate an invalid URL.
- **No SPF Record Found**: If no SPF record is found for the domain, the script will notify the user.


## Contact

For any questions or feedback, please contact findtanmay10@gmail.com.
