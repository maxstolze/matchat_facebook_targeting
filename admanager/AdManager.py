from facebookads import FacebookAdsApi
from facebookads import FacebookSession
from facebookads.adobjects.adaccount import AdAccount
from facebookads.adobjects.adaccountuser import AdAccountUser
from facebookads.adobjects.adstudy import AdStudy
from facebookads.adobjects.campaign import Campaign
from facebookads.api import FacebookAdsApi
from facebookads.adobjects.adset import AdSet
from facebookads import FacebookAdsApi
from facebookads.adobjects.targeting import Targeting
from facebookads import FacebookSession
from facebookads.adobjects.ad import Ad
from facebookads.adobjects.adimage import AdImage
from facebookads.adobjects.adcreative import AdCreative
from facebookads.specs import ObjectStorySpec, LinkData

import json
import os

def initSession():
    this_dir = os.path.dirname(__file__)
    config_filename = os.path.join(this_dir, 'config.json')

    config_file = open(config_filename)
    config = json.load(config_file)
    config_file.close()

    session = FacebookSession(
        config['app_id'],
        config['app_secret'],
        config['access_token'],
    )
    api = FacebookAdsApi(session)
    FacebookAdsApi.set_default_api(api)
    return api

def readCampaign(campaign_id):
    campaign = Campaign(fbid=campaign_id)
    campaign.remote_read(fields=[Campaign.Field.id, Campaign.Field.name])
    return campaign

def createCampaign(account_id):
    campaign = Campaign(parent_id = account_id)
    campaign[Campaign.Field.name] = "Matchat Campain"
    campaign[Campaign.Field.objective] = Campaign.Objective.link_clicks
    campaign[Campaign.Field.configured_status] = Campaign.Status.paused
    campaign.remote_create()
    return campaign

def readAdSet(adset_id):
    ad_set = AdSet(fbid=adset_id)
    ad_set.remote_read(fields=[AdSet.Field.id])
    return ad_set

def createAdSet(account_id, campaign_id):
    ad_set = AdSet(parent_id=account_id)
    ad_set[AdSet.Field.name] = 'Matchat AdSet'

    targeting = {}
    targeting[Targeting.Field.age_max] = 50
    targeting[Targeting.Field.age_min] = 18
    targeting[Targeting.Field.geo_locations] = {
        'countries': ['AT']
    }
    ad_set[AdSet.Field.targeting] = targeting
    ad_set[AdSet.Field.campaign_id] = campaign_id
    ad_set[AdSet.Field.is_autobid] = True
    ad_set[AdSet.Field.daily_budget] = 100 # US cents
    ad_set[AdSet.Field.billing_event] = AdSet.BillingEvent.impressions
    ad_set.remote_create()
    return ad_set

def createAd(account_id, adset_id, page_id):
    ad = Ad(parent_id=account_id)
    ad[Ad.Field.name] = ' Matchat Ad'
    ad[Ad.Field.adset_id] = adset_id

    link_data = LinkData()
    link_data[LinkData.Field.message] = 'Great looking SXT handbags in store. #prettybag'
    link_data[LinkData.Field.link] = 'http://example.com'
    link_data[LinkData.Field.caption] = 'www.example.com'
    #link_data[LinkData.Field.image_hash] = '<IMAGE_HASH>'

    call_to_action = {
        'type': 'LEARN_MORE',
    }
    call_to_action['value'] = {
        'link':'http://example.com',
    }

    link_data[LinkData.Field.call_to_action] = call_to_action

    object_story_spec = ObjectStorySpec()
    object_story_spec[ObjectStorySpec.Field.page_id] = page_id
    object_story_spec[ObjectStorySpec.Field.link_data] = link_data

    ad[Ad.Field.creative] = {
        AdCreative.Field.title: 'try out matchat!',
        AdCreative.Field.body: 'decentralized online marketplace',
        #AdCreative.Field.object_url: 'https://matchat.org',
        AdCreative.Field.object_story_spec: object_story_spec,
        #AdCreative.Field.image_hash: image_hash,
    }

    ad[Ad.Field.status] = AdSet.Status.paused
    ad.remote_create()
    return ad

def createSplitTestAdStudy(business_id, adset1_id, adset2_id):
    adstudy = AdStudy(parent_id=business_id)
    adstudy[AdStudy.Field.name] = 'Matchat AdStudy'
    adstudy[AdStudy.Field.type] = AdStudy.Type.split_test
    adstudy[AdStudy.Field.start_time] = 1532512562
    adstudy[AdStudy.Field.end_time] = 1532512563
    adstudy[AdStudy.Field.cells] = [
        {'name' : 'Men', 'adsets' : [adset1_id], 'treatment_percentage' : 50.0},
        {'name' : 'Women', 'adsets' : [adset2_id], 'treatment_percentage' : 50.0}
    ]
    adstudy.remote_create()
    return adstudy