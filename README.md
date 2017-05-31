# Prime Loan Rate Analysis

This repository includes some information I found while researching the Federal Prime Loan Rate.

## What is the Prime Rate?

It's hard to top [Wikipedia](https://en.wikipedia.org/wiki/Prime_rate):

    A prime rate or prime lending rate is an interest rate used by banks, usually the interest rate at which banks lend to favored customers—i.e., those with good credit. Some variable interest rates may be expressed as a percentage above or below prime rate.

## Where's the raw data?

Historic information on the Prime Rate is provided by [Federal Reserve Economic Data (FRED)](https://fred.stlouisfed.org/) under [the series MPRIME](https://fred.stlouisfed.org/series/MPRIME). This project uses the data found in the [CSV export of the data](https://fred.stlouisfed.org/graph/fredgraph.csv?id=MPRIME).

Raw output from running the script for 5-year, 10-year, and 15-year rate comparisons are in separate files with reasonable names in this directory.

## Insights

### Overview

At a high level, the Prime Rate was first introduced in 1949 at 2%. It more or less steadily climbed up to over 2% in 1981 and fell to 6% in 1993. It slowly climbed up to 9% in 2001 and then got cut in half by the beginning of 2002. It jumped back up to 8% in 2007 and then swiftly dropped to 3.25% after the [Great Recession](https://en.wikipedia.org/wiki/Great_Recession). It finally crept up to 4% in 2017.

### Trends over time

Pretty much since its peak in the early 80's, the Prime Rate has been falling ever since. It has gone up some years, but by  in large the rate has been falling. In recent memory, the Rate began skyrocketing in 2007 and 2008 (right before the Great Recession). In fact, the Prime Rate increased at a steady clip from 2004 until early 2008 as if it were attempting to correct for the drastic drop in 2001.

### What happened around 1980 and in 2001?

From 1977 to 1981, the Prime Rate jumped from 6.25% to over 20%. It then crashed to 11% by 1984. In 2001, the Rate fell from 9% to 4.75% in a single year (with steady growth beforehand). [Per Wikipedia](https://en.wikipedia.org/wiki/Early_1980s_recession#United_States), the Federal Reserve was drastically increasing rates in an attempt to curtail inflation. However, a global recession hit in the early 80's and the Fed was forced to reverse their policy to encourage economic growth. Fear of a [looming recession in 2001](http://cnnfn.cnn.com/2001/10/02/economy/fed/) caused them to do it again.

### How low can rates go?

At the time of writing, the Prime Rate hit 4% in 2017. Rates this low haven't been seen since the 50's! With that said, the economy is improving so it would be unlikely for the rates to go down any time soon. However, inflation is still low and many people are underemployed which will make the Fed weary of increasing rates too quickly.

## How to use the script

### Requirements

* Python 3
* tabulate (`pip install tabulate`)

## Usage

The command is `python prime.py </path/to/csv> <years>`. For example

      python prime.py MPRIME.csv 5

will output 5-year moving rate differences.
