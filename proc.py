#!/usr/bin/env python3
# License: CC0

from bs4 import BeautifulSoup
import datetime

def main():
    print("insert into donations(donor, donee, amount, donation_date, donation_date_precision, donation_date_basis, url, notes) values")
    first = True
    with open("data.html", "r") as f:
        soup = BeautifulSoup(f, "lxml")
        for entry in soup.find_all("div", {"class": "lost"}):
            donor = entry.find("h5").text.strip()
            ps = entry.find_all("p")
            amount = float(ps[0].find("span").text.replace("$", "").replace(",", ""))
            date = datetime.datetime.strptime(ps[1].find("span").text,
                                              "%B %d, %Y").strftime("%Y-%m-%d")
            block_info = []
            for p in ps[2:]:
                block = int(p.find("strong").text[len("Block \n"):-len("\n:")])
                spans = p.find_all("span")
                block_range = list(map(lambda x: x.text, spans))
                block_info.append("Block {}, [{}–{}]".format(block, *block_range))
            print(("    " if first else "    ,") + "(" + ",".join([
                mysql_quote(donor),  # donor
                mysql_quote("Donor lottery"),  # donee
                str(amount),  # amount
                mysql_quote(date),  # donation_date
                mysql_quote("day"),  # donation_date_precision
                mysql_quote("transaction"),  # donation_date_basis
                mysql_quote("https://app.effectivealtruism.org/lotteries/31553453298138"),  # url
                mysql_quote("{}. See https://app.effectivealtruism.org/lotteries for general background; see http://effective-altruism.com/ea/1ip/announcing_the_2017_donor_lottery/ for the blog post announcing this lottery.".format("; ".join(block_info))),  # notes
            ]) + ")")
            first = False
        print(";")


def mysql_quote(x):
    '''
    Quote the string x using MySQL quoting rules. If x is the empty string,
    return "NULL". Probably not safe against maliciously formed strings, but
    whatever; our input is fixed and from a basically trustable source..
    '''
    if not x:
        return "NULL"
    x = x.replace("\\", "\\\\")
    x = x.replace("'", "''")
    x = x.replace("\n", "\\n")
    return "'{}'".format(x)


if __name__ == "__main__":
    main()
