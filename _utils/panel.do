// Week 7b: Panel regression (an aside)
// Adapted from the Stata docs, so we have
// a dataset that's publicly available.

use http://www.stata-press.com/data/r13/nlswork

xtset idcode year


local controls ///
    grade ///
    age ///
    ttl_exp ///
    tenure

local ivs ///
    not_smsa ///
    south


reg ln_wage `controls' `ivs'

xtreg ln_wage `controls' `ivs', fe
estimates store fe

xtreg ln_wage `controls' `ivs', re
estimates store re

hausman fe re
