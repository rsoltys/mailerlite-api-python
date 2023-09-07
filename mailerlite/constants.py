"""File containing global contants ."""

from collections import namedtuple

MAILERLITE_API_V2_URL = 'https://api.mailerlite.com/api/v2/'

API_KEY_TEST = "fc7b8c5b32067bcd47cafb5f475d2fe9"

VALID_REQUEST_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

Field = namedtuple('Field', ['key', 'value', 'type', 'title', 'id',
                             'date_updated', 'date_created'])
Group = namedtuple('Group', ["id", "name", "total", "active", "unsubscribed",
                             "bounced", "unconfirmed", "junk", "sent",
                             "opened", "clicked", "date_created",
                             "date_updated", "parent_id"])
Activity = namedtuple('Activity', ['date', 'report_id', 'subject',
                                   'campaign_name', 'type',
                                   'campaign_id', 'link_id', 'link',
                                   'receiver', 'receiver_name',
                                   'receiver_email', 'sender', 'sender_name',
                                   'sender_email'])
Subscriber = namedtuple('Subscriber', ['id', 'name', 'email', 'sent',
                                       'opened', 'clicked', 'type',
                                       'signup_ip', 'signup_timestamp',
                                       'confirmation_ip',
                                       'confirmation_timestamp',
                                       'fields', 'date_subscribe',
                                       'subscribe_date',
                                       'webform_subscribe_date',
                                       'date_unsubscribe', 'date_created',
                                       'date_updated', 'opened_rate',
                                       'clicked_rate', 'country_id',
                                       'user_agent', 'first_subscribed_at',
                                       'opted_in_at'
                                       ])
Pagination = namedtuple('Pagination', ["total", "count", "per_page",
                                       "current_page", "total_pages",
                                       "links"])
Meta = namedtuple('Meta', ['pagination', ])
Segment = namedtuple('Segment', ['id', 'title', 'filter', 'total', 'sent',
                                 'opened', 'clicked', 'created_at',
                                 'updated_at', 'timed_out'])
Stats = namedtuple('Stats', ['count', 'rate'])
Campaign = namedtuple('Campaign', ['id', 'total_recipients', 'type',
                                   'date_created', 'date_send', 'name',
                                   'subject', 'status',
                                   'opened', 'clicked'])
Webhook = namedtuple('Webhook', ['id', 'event', 'url', 'created_at',
                                 'updated_at'])

for nt in [Subscriber, Field, Group, Activity, Segment, Meta, Pagination,
           Campaign, Stats, Webhook]:
    nt.__new__.__defaults__ = (None,) * len(nt._fields)


def validate_or_make_namedtuples(obj, keys):

    if not set(keys).issubset(obj._fields):
        diff = set(list(obj._fields)).symmetric_difference(set(keys))
        return namedtuple(f'{obj.__name__}2', obj._fields + tuple(diff))
    return obj
