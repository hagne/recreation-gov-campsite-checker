import pandas as pd
from datetime import datetime 
from dateutil import rrule
import requests
from fake_useragent import UserAgent
import os
import time
from itertools import count, groupby
import recreationdotgov.settings as _rdgsettings

### global constance ... todo: improve integration ... redefine, etc
ISO_DATE_FORMAT_REQUEST = "%Y-%m-%dT00:00:00.000Z"
BASE_URL = "https://www.recreation.gov"
AVAILABILITY_ENDPOINT = "/api/camps/availability/campground/"
headers = {"User-Agent": UserAgent().random}
MAIN_PAGE_ENDPOINT = "/api/camps/campgrounds/"
ISO_DATE_FORMAT_RESPONSE = "%Y-%m-%dT00:00:00Z"

settings = _rdgsettings.load_config()
### helper functions... todo: these are the originals ... consider rewrite

def consecutive_nights(available, nights):
    """
    Returns whether there are `nights` worth of consecutive nights.
    """
    ordinal_dates = [datetime.strptime(dstr, ISO_DATE_FORMAT_RESPONSE).toordinal() for dstr in available]
    c = count()
    longest_consecutive = max((list(g) for _, g in groupby(ordinal_dates, lambda x: x-next(c))), key=len)
    return len(longest_consecutive) >= nights

def format_date(date_object, format_string=ISO_DATE_FORMAT_REQUEST):
    """
    Todo: get rid of it by replacing with pandas
    This function doesn't manipulate the date itself at all, it just
    formats the date in the format that the API wants.
    """
    date_formatted = datetime.strftime(date_object, format_string)
    return date_formatted

def send_request(url, params):
    resp = requests.get(url, params=params, headers=headers)
    if resp.status_code != 200:
        raise RuntimeError(
            "failedRequest",
            "ERROR, {} code received from {}: {}".format(
                resp.status_code, url, resp.text
            ),
        )
    return resp.json()

### my helper functions
def notify_by_text(message):
    return

### classes
class Campground(object):
    def __init__(self, id):
        self._base_url_html = 'https://www.recreation.gov/camping/campgrounds/'
        self.id = id
#         self.query = Query
        self._info = None
    
    def make_query(self, checkin_date, no_of_nights, verbose = True):
        query = Query(self, checkin_date=checkin_date, no_of_nights= no_of_nights)
        self.query = query
        out = {}
        out['no_available'] = len(query.available_sites)
        out['campground_name'] = self.info['facility_name']
        out['url'] = self.info['url_html']
        if verbose:
            print(f"{out['no_available']} {out['campground_name']} {out['url']}")
        return out
    
    @property
    def info(self):
        if isinstance(self._info, type(None)):
            url = "{}{}{}".format(BASE_URL, MAIN_PAGE_ENDPOINT, self.id)
            resp = send_request(url, {})['campground']
            resp['url_api'] = url
            resp['url_html'] = f'{self._base_url_html}{self.id}'
            self._info = resp
        return self._info#["campground"]["facility_name"]
    
    @property
    def info_short(self):
        add = self.info['addresses'][0]
        short_info = f"{self.info['facility_name']}\n{self.info['url_html']}\n{add['address1']},{add['city']}, {add['state_code']}"
        return short_info

class CampgroundCollection(object):
    def __init__(self, campgrounds):
        self.campgrounds = campgrounds
        
    def make_query(self, checkin_date, no_of_nights, keep_looking = False, verbose = True, notify = False):
        """
        check for availability

        Parameters
        ----------
        checkin_date : str, e.g. '08/29/2021'
            DESCRIPTION.
        no_of_nights : int
            DESCRIPTION.
        keep_looking : bool or int, optional
            If true, the programm will check again for an availability after 
            the set number of seconds. keep_looking = 300 will check every 
            5 minutes.
        verbose : TYPE, optional
            DESCRIPTION. The default is True.
        notify: bool, str, or email. ('sound', 'text'), optional
            sound: will play a sound using spd-say. Had problems using it in 
                jupyter recently, not sure if it works in a cron-job?!?
            text: send 

        Returns
        -------
        res_list : TYPE
            DESCRIPTION.

        """
        def single_query(checkin_date, no_of_nights):
            no_of_nights = 1
            res_list = []
            for cg in self.campgrounds:
                res_list.append(cg.make_query(checkin_date,no_of_nights, verbose = False))

            res_list.sort(key = lambda x: x['no_available'], reverse=True)
            return res_list
        
        if not keep_looking:
            res_list = single_query(checkin_date, no_of_nights)
            # if verbose:
            #     for res in res_list:
            #         print(f"{res['no_available']} {res['campground_name']} {res['url']}")
        else:
            found_one = False
            while not found_one:
                now = time.strftime("%T", time.localtime())
                print(now, end = '...')
                try:
                    res_list = single_query(checkin_date, no_of_nights)
                except RuntimeError:
                    print('RTE', end = '...')
                    continue
                if max([i['no_available'] for i in res_list]) > 0:
                    found_one = True
                else:
                    time.sleep(keep_looking)
            #     break

            res_list.sort(key = lambda x: x['no_available'], reverse=True)
            print('')
            
        for res in res_list:
            print(f"{res['no_available']} {res['campground_name']} {res['url']}")
        
        if max([i['no_available'] for i in res_list]) > 0:
            if notify == 'sound':
                while 1:
                    os.system('spd-say "found one"')
                    time.sleep(5)
        return res_list

class Query(object):
    def __init__(self, campground, checkin_date = '2020-11-01', no_of_nights = 1):
        self.campground = campground
        self._api_data = None
        self.date_checkin = pd.to_datetime(checkin_date)
        self._date_checkout = None
        self.no_of_nights = no_of_nights
        self.campsite_type = False#'GROUP TENT ONLY AREA NONELECTRIC'
        return
    
    @property
    def date_checkout(self):
        if isinstance(self._date_checkout, type(None)):
            self._date_checkout = self.date_checkin + pd.to_timedelta(self.no_of_nights, 'd')
        return self._date_checkout
            
    
    @property
    def api_data(self):
        if isinstance(self._api_data, type(None)):
            # Get each first of the month for months in the range we care about.
            start_of_month = datetime(self.date_checkin.year, self.date_checkin.month, 1)
            months = list(rrule.rrule(rrule.MONTHLY, dtstart=start_of_month, until=self.date_checkout))

            # Get data for each month.
            api_data = []
            for month_date in months:
                params = {"start_date": format_date(month_date)}
#                 LOG.debug("Querying for {} with these params: {}".format(park_id, params))
                url = "{}{}{}/month?".format(BASE_URL, AVAILABILITY_ENDPOINT, self.campground.id)
                resp = send_request(url, params)
                api_data.append(resp)
            self._api_data = api_data
        return self._api_data
    
    @property
    def available_sites(self):
        # Collapse the data into the described output format.
        # Filter by campsite_type if necessary.
        data = {}
        for month_data in self.api_data:
            for campsite_id, campsite_data in month_data["campsites"].items():
                available = []
                for date, availability_value in campsite_data["availabilities"].items():
                    if availability_value != "Available":
                        continue
#                     print(campsite_data["campsite_type"])
                    if self.campsite_type and self.campsite_type != campsite_data["campsite_type"]:
                        continue
                    available.append(date)
                if available:
                    a = data.setdefault(campsite_id, [])
                    a += available
                    
        # match with what we want
#         park_information = out
        dates = pd.date_range(self.date_checkin, periods=self.no_of_nights)
        available_sites = []
        for site, availabilities in data.items():
            # List of dates that are in the desired range for this site.
            desired_available = []
            for date in availabilities:
                if date not in dates:
                    continue
                desired_available.append(date)
            if desired_available and consecutive_nights(desired_available, self.no_of_nights):
                available_sites.append(site)
        #         LOG.debug("Available site {}: {}".format(num_available, site))
        return available_sites