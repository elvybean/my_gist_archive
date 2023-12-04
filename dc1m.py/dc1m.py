def months_left(c_mo, c_yr, mo_lt):
    mo_rem = mo_lt % 12
    if mo_rem != 0:
        yrs_lt = (mo_lt - mo_rem) / 12
    else:
        yrs_lt = mo_lt / 12

    ftr_mo = c_mo + mo_rem

    yrSto = 0
    while ftr_mo > 12:
        ftr_mo = ftr_mo - 12
        yrSto += 1

    ftr_yrs = c_yr + yrs_lt + yrSto

    ftr_dat = [ftr_mo, ftr_yrs]

    return ftr_dat