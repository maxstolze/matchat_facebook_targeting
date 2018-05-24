from facebook_business.adobjects.adsinsights import AdsInsights

from admanager.AdManager import *

if __name__ == '__main__':

    this_dir = os.path.dirname(__file__)
    resource_path = os.path.join(this_dir, 'resources')

    admanager = AdManager(resource_path)

    # the fields we want to return from the adsinsights analysis results
    adsinsights_fields = ['adset_name', 'adset_id', 'clicks', 'cpc', 'frequency', 'reach', 'impressions', 'spend', 'relevance_score']

    # the breakdowns we want to apply for the adsinsights analysis results
    # (gender and age, so we do not have to include these in our targting for the split testing)
    adsinsights_params_gender = {
        'breakdowns': ['gender']
    }
    adsinsights_params_age = {
        'breakdowns': ['age']
    }

    for adset in admanager.listAllAdsets():
        adsinsights = admanager.readInsightsForAdset(adset.get_id(), fields=adsinsights_fields)
        print adsinsights
        adsinsights = admanager.readInsightsForAdset(adset.get_id(), fields=adsinsights_fields, params=adsinsights_params_gender)
        print adsinsights
        adsinsights = admanager.readInsightsForAdset(adset.get_id(), fields=adsinsights_fields, params=adsinsights_params_age)
        print adsinsights