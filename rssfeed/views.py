# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
# from .models import News
from datetime import datetime
import feedparser


RSS_FEEDS = {
    "1": {
        "title": "The Jerusalem Post",
        "rss_link": "https://www.jpost.com/Rss/RssFeedsHeadlines.aspx"
    },
    "2": {
        "title": "Daily Mail",
        "rss_link": "http://www.dailymail.co.uk/articles.rss"
    },
    "3": {
        "title": "Wired Magazine",
        "rss_link": "http://feeds.wired.com/wired/index"
    },
}

def index(request):
    return HttpResponse("Welcome to the RSS News feed App")

def news_sources(request):
    return render(request, template_name='rssfeed/sources.html')



def newsList(request):

    desired_rss_feed = request.GET.get('id', "1")
    print("went in" + desired_rss_feed)
    if desired_rss_feed not in RSS_FEEDS:
        desired_rss_feed = "1"


    feed = feedparser.parse(RSS_FEEDS[desired_rss_feed]["rss_link"])


    headlines = [
        {"title": entry["title"], "link": entry["link"]}
        for entry in feed["entries"]
    ]

    visited_at = request.COOKIES.get("visited_at")

    response_dict = {
        "headlines": headlines,
        "last_visited": visited_at
    }
    # Let the client know the last time the page was refreshed based on datetime value stored in a cookie.

    # Update the cookie the current datetime.
    response = render(request, 'rssfeed/index.html', response_dict)
    response.set_cookie("visited_at", str(datetime.now()), max_age=3600 * 24)
    return response