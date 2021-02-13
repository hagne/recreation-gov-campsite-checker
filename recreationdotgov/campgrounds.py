# -*- coding: utf-8 -*-
from recreationdotgov import recreationlab as _rcl

### CO
#### rocky moutain national park
co_rmnp_glacier_basin = _rcl.Campground(232462)

co_rmnp = _rcl.CampgroundCollection([co_rmnp_glacier_basin])

#### indian peaks
co_indian_peaks_pawnee = _rcl.Campground(232282)

co_indian_peaks = _rcl.CampgroundCollection([co_indian_peaks_pawnee])


### mount evens
co_evens_gueanella_pass = _rcl.Campground(232306)

co_evens = _rcl.CampgroundCollection([co_evens_gueanella_pass])

### all
co = _rcl.CampgroundCollection(co_rmnp.campgrounds + co_indian_peaks.campgrounds + co_evens.campgrounds)