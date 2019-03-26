This is for https://github.com/vipulnaik/donations/

Specific issue: https://github.com/vipulnaik/donations/issues/37

note: for the January 2019 lottery HTMLs, I've changed the "lost" and "won"
classes a bit because the processing script finds divs based on these classes.

## How to get the HTML file for a lottery

Go to a lottery page like
https://app.effectivealtruism.org/lotteries/63715163508813 and use your
browser's "inspect element" feature to find the div that contains all the
lottery entries. Then right click do Copy → Outer HTML. Paste this HTML into a
new file. Then run an HTML formatter such as `tidy` on the file. From vim this
can be done as follows:

```vim
:%!tidy -q -w 0
```

## Running the processing script

The general syntax is:

```bash
./proc.py html_filename lottery_url lottery_name lottery_blog_post_url
```

Some examples:

* old lottery:

  ```bash
  ./proc.py data.html "https://app.effectivealtruism.org/lotteries/31553453298138" 'January 2018 $100k lottery' "http://effective-altruism.com/ea/1ip/announcing_the_2017_donor_lottery/"
  ```

* the $100k lottery drawn on 2019-01-30:

  ```bash
  ./proc.py data-january-2019-100k.html "https://app.effectivealtruism.org/lotteries/63715163508812" 'January 2019 $100k lottery' "https://forum.effectivealtruism.org/posts/nuzcbhk2JYMkALHke/donor-lottery-2018-is-live"
  ```

* the $500k lottery drawn on 2019-01-30:

  ```bash
  ./proc.py data-january-2019-500k.html "https://app.effectivealtruism.org/lotteries/63715163508813" 'January 2019 $500k lottery' "https://forum.effectivealtruism.org/posts/nuzcbhk2JYMkALHke/donor-lottery-2018-is-live"
  ```
