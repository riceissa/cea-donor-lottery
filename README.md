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
