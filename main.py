import requests, re, argparse

def get_website_data(url):
    '''Request the URL and import it
    into BeautifulSoup for processing'''

    # Get the URL data
    res = requests.get(url)

    # Check to ensure there's no problems with it
    try:
        res.raise_for_status()
    except:
        print("There's a problem with the url: %s" % url)
        return False

    return res.text

def find_emails(data):

    emailRegex = re.compile(r'[\w\.-]+@[\w\.-]+', re.VERBOSE)

    emails = emailRegex.findall(data)

    return emails

def remove_duplicate_emails(emails):

    unique_emails = []

    for email in emails:
        if email[-1] == '.':
            email = email[0:-1]

        if email not in unique_emails:
            unique_emails.append(email)

    return unique_emails

def parse_arguments():
    parser = argparse.ArgumentParser(description = "Email Scraper")
    parser.add_argument("--urls", type=str, help="URLs split by comma")

    return parser.parse_args()

def main():
    args = parse_arguments()

    if not args.urls:
        raise Exception("Please provide at least 1 url")

    for url in args.urls.split(","):

        data = get_website_data(url)

        emails = remove_duplicate_emails(find_emails(data))

        if len(emails) == 0:
            print("No emails found for {}".format(url))
        else:
            print("Emails found for {}:\n{}\n\n".format(url, ", ".join(emails)))

if __name__ == "__main__":
    main()