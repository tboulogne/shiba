#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# class SalesManagement

from shibainit import ShibaInit
from shibatools import ShibaTools
import datetime


class SalesManagement(ShibaInit):
    """Primary sales management class, gather all sales-related methods. Those methods returns a obj
    from the XML given as answer by the related WebService."""

    def __init__(self, login, pwd, domain="https://ws.priceminister.com/"):
        super(SalesManagement, self).__init__(login, pwd, domain)

    def get_new_sales(self):
        """Calling get_new_sales method gives you back a obj from returned XML, featuring all the new sales which
        have been done."""
        inf = ShibaTools.inf_constructor(ShibaInit, "getnewsales", **locals())
        url = ShibaTools.url_constructor(ShibaInit, inf)
        obj = ShibaTools.retrieve_obj_from_url(url)
        return obj

    def accept_sale(self, itemid):
        """Accept the "itemid" sale"""
        inf = ShibaTools.inf_constructor(ShibaInit, "acceptsale", **locals())
        url = ShibaTools.url_constructor(ShibaInit, inf)
        obj = ShibaTools.retrieve_obj_from_url(url)
        return obj

    def refuse_sale(self, itemid):
        """Refuse the "itemid" sale"""
        inf = ShibaTools.inf_constructor(ShibaInit, "refusesale", **locals())
        url = ShibaTools.url_constructor(ShibaInit, inf)
        obj = ShibaTools.retrieve_obj_from_url(url)
        return obj

    def get_current_sales(self, ispendingorder="", purchasedate="", nexttoken=""):
        """Calling get_current_sales method gives you a obj gathering all current sales.
        :param ispendingorder: pass "y" is you want to see all preordered sales, leave empty as default
        :param purchasedate: Formatted as "yyyy-mm-dd" string allows you to filter the sales only from the given date
        :param nexttoken: Next page token argument, leave at is it, only give 0 is you want the first page"""
        assert(ispendingorder == "y" or ""), "error : ispendingorder parameter unexpected value"
        if isinstance(purchasedate, datetime.datetime):
            purchasedate = purchasedate.strftime("%d/%m/%y-%H:%M:%S")
        inf = ShibaTools.inf_constructor(ShibaInit, "getcurrentsales", **locals())
        url = ShibaTools.url_constructor(ShibaInit, inf)
        obj = ShibaTools.retrieve_obj_from_url(url)
        return obj

    def get_billing_information(self, purchaseid):
        """Calling this method gives you accounting information about a confirmed order.
        :param purchaseid: is mandatory (same as found in get_new_sales report)."""
        inf = ShibaTools.inf_constructor(ShibaInit, "getbillinginformation", **locals())
        url = ShibaTools.url_constructor(ShibaInit, inf)
        obj = ShibaTools.retrieve_obj_from_url(url)
        return obj

    def get_shipping_information(self, purchaseid):
        """Quite similar to billing information method, but returns information about shipping for a given purchaseid
        Order forms are also available from this method return.
        :param purchaseid: is mandatory (same as found in get_new_sales report)."""
        inf = ShibaTools.inf_constructor(ShibaInit, "getshippinginformation", **locals())
        url = ShibaTools.url_constructor(ShibaInit, inf)
        obj = ShibaTools.retrieve_obj_from_url(url)
        return obj

    def get_items_todo_list(self):
        """Retriving a todo list on items, such as CLAIMS or MESSAGES from buyer or PriceMinister."""
        inf = ShibaTools.inf_constructor(ShibaInit, "getitemstodolist", **locals())
        url = ShibaTools.url_constructor(ShibaInit, inf)
        obj = ShibaTools.retrieve_obj_from_url(url)
        return obj

    def get_items_info(self, itemid):
        """This methods retrieves informations from an "itemid" item, such as state, history, messages linked to it
        and actions available for this item. WARNING : All messages related to asked item will be tagged as "read"."""
        inf = ShibaTools.inf_constructor(ShibaInit, "getitemsinfo", **locals())
        url = ShibaTools.url_constructor(ShibaInit, inf)
        obj = ShibaTools.retrieve_obj_from_url(url)
        return obj

    def cancel_item(self, itemid, comment):
        """This method cancel the sale from the "itemid" item, after this one has been sold. WARNING : Cancelling
        a sale this way could harm your seller reputation. Use the "comment" param to specify the reason of this
        action to the related buyer (mandatory)."""
        inf = ShibaTools.inf_constructor(ShibaInit, "cancelitem", **locals())
        url = ShibaTools.url_constructor(ShibaInit, inf)
        obj = ShibaTools.retrieve_obj_from_url(url)
        return obj

    def contact_us_about_item(self, itemid, message, mailparentid=""):
        """This functionality permits to join the PriceMinister after-sales service as buyer or seller.
        Specify the mailparentid to reply to a previous mail exchange. Message is message content, and itemid is
        the item PriceMinister ID related to the claim."""
        inf = ShibaTools.inf_constructor(ShibaInit, "contactusaboutitem", **locals())
        url = ShibaTools.url_constructor(ShibaInit, inf)
        obj = ShibaTools.retrieve_obj_from_url(url)
        return obj

    def contact_user_about_item(self, itemid, message):
        """Contact buyer of the "itemid" item in a regular way, sending him the "message"""
        inf = ShibaTools.inf_constructor(ShibaInit, "contactuseraboutitem", **locals())
        url = ShibaTools.url_constructor(ShibaInit, inf)
        obj = ShibaTools.retrieve_obj_from_url(url)
        return obj

    def set_tracking_package_infos(self, itemid, transporter_name, tracking_number, tracking_url=""):
        """Send to buyer tracking infos, such as the transporter's name "transporter_name",
        tracking number "tracking_number" and the optional tracking url "trackin_url".
        Please note that giving "Autre" as transporter_name brings the tracking url as mandatory."""
        assert (transporter_name == "Autre" and len(tracking_url) == 0, "error : tracking url is mandatory")
        inf = ShibaTools.inf_constructor(ShibaInit, "settrackingpackageinfos", **locals())
        url = ShibaTools.url_constructor(ShibaInit, inf)
        obj = ShibaTools.retrieve_obj_from_url(url)
        return obj

    def confirm_preorder(self, advertid, stock):
        """Confirms preorders from the "advertid" item announce, will confirm "stock" items as confirmed orders."""
        assert (stock <= 0, "error : stock must be a positive number")
        inf = ShibaTools.inf_constructor(ShibaInit, "confirmpreoder", **locals())
        url = ShibaTools.url_constructor(ShibaInit, inf)
        obj = ShibaTools.retrieve_obj_from_url(url)
        return obj