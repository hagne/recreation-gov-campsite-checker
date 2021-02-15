# -*- coding: utf-8 -*-
from recreationdotgov import recreationlab as _rcl

### CO
#### rocky moutain national park
co_rmnp_glacier_basin = _rcl.Campground(232462)

co_rmnp = _rcl.CampgroundCollection([co_rmnp_glacier_basin])

#### indian peaks
co_indian_peaks_pawnee = _rcl.Campground(232282)
co_indian_peaks_camp_dick = _rcl.Campground(232369)
co_indian_peaks_peaceful_valley = _rcl.Campground(232368)
co_indian_peaks_olive_ridge = _rcl.Campground(232281)

co_indian_peaks = _rcl.CampgroundCollection([co_indian_peaks_pawnee, co_indian_peaks_camp_dick, co_indian_peaks_peaceful_valley, co_indian_peaks_olive_ridge])


#### mount evens
co_evens_gueanella_pass = _rcl.Campground(232306)
co_evens_geneva_park = _rcl.Campground(234118)
co_evens_burning_bear = _rcl.Campground(234737)
co_evens_west_chicago_creek = _rcl.Campground(231859)
co_evens_echo_lake = _rcl.Campground(231857)

co_evens = _rcl.CampgroundCollection([co_evens_gueanella_pass, 
                                      co_evens_geneva_park, 
                                      co_evens_burning_bear, 
                                      co_evens_west_chicago_creek,
                                      co_evens_echo_lake])

#### great sand dunes
co_great_sand_dunes_pinon_flats = _rcl.Campground(234685)
co_great_sand_dunes = _rcl.CampgroundCollection([co_great_sand_dunes_pinon_flats])

### all
co = _rcl.CampgroundCollection(co_rmnp.campgrounds + co_indian_peaks.campgrounds + co_evens.campgrounds)