# -*- coding: utf-8 -*-
import sys

import xbmcgui
import xbmcplugin

try:
    # Python 3
    from urllib.parse import parse_qsl, urlencode
except ImportError:
    from urllib import urlencode
    from urlparse import parse_qsl

import ipfs

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])
_rootCid = xbmcplugin.getSetting(_handle, "rootCid")
_ipfs = ipfs.via(xbmcplugin.getSetting(_handle, "ipfsGateway"))


def self_url(**kwargs):
    """
    Create a URL for calling the plugin recursively from the given set of keyword arguments.

    :param kwargs: "argument=value" pairs
    :type kwargs: dict
    :return: plugin call URL
    :rtype: str
    """
    return "{0}?{1}".format(_url, urlencode(kwargs))


def list_node(cid):
    """
    Create a listing of the given ipfs cid

    :param cid: content identifier
    :type category: str
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_handle, cid)
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_handle, "videos")
    # Get the list of videos in the category.
    links = _ipfs.list(cid)

    for link in links:
        is_folder = len(_ipfs.list(link["hash"]["/"])) > 0

        list_item = xbmcgui.ListItem(label=link["name"])
        # Set additional info for the list item.
        # 'mediatype' is needed for skin to display info for this ListItem correctly.
        list_item.setInfo("video", {"title": link["name"], "mediatype": "video"})
        # TODO set thumbnails
        # list_item.setArt({'thumb': video['thumb'], 'icon': video['thumb'], 'fanart': video['thumb']})

        list_item.setProperty("IsPlayable", ("false" if is_folder else "true"))

        url = self_url(action=("list" if is_folder else "play"), cid=link["hash"]["/"])
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_TITLE)
    xbmcplugin.endOfDirectory(_handle)


def play_node(cid):
    """
    Play a video by the provided cid.

    :param cid: Content id
    :type path: str
    """
    play_item = xbmcgui.ListItem(path=_ipfs.link(cid))
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring

    :param paramstring: URL encoded plugin paramstring
    :type paramstring: str
    """
    params = dict(parse_qsl(paramstring))

    # Default action
    if not params:
        params["action"] = "list"
        params["cid"] = _rootCid

    # Check the parameters passed to the plugin
    if params["action"] == "list":
        list_node(params["cid"])
    elif params["action"] == "play":
        play_node(params["cid"])
    else:
        raise ValueError("Invalid paramstring: {0}!".format(paramstring))


if __name__ == "__main__":
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
