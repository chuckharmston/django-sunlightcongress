from django.contrib import admin
from sunlightcongress.models import Committee, Legislator


class LegislatorAdmin(admin.ModelAdmin):
    """
    ModelAdmin object for the Legislator model
    """
    list_display = (
        'fullname',
        'party',
        'house',
        'state',
    )
    list_filter = (
        'title',
        'party',
        'in_office',
        'gender',
    )
    search_fields = (
        'firstname',
        'middlename',
        'lastname',
    )
    readonly_fields = (
        'title',
        'firstname',
        'middlename',
        'lastname',
        'name_suffix',
        'nickname',
        'party',
        'state',
        'district',
        'in_office',
        'gender',
        'phone',
        'fax',
        'website',
        'webform',
        'email',
        'congress_office',
        'bioguide_id',
        'votesmart_id',
        'fec_id',
        'govtrack_id',
        'crp_id',
        'congresspedia_url',
        'twitter_id',
        'youtube_url',
        'facebook_id',
        'senate_class',
        'official_rss',
        'birthdate',
    )

admin.site.register(Legislator, LegislatorAdmin)


class CommitteeAdmin(admin.ModelAdmin):
    """
    ModelAdmin object for the Committee model
    """
    filter_horizontal = ('members',)
    readonly_fields = (
        'id',
        'chamber',
        'name',
        'parent',
        'members',
    )

admin.site.register(Committee, CommitteeAdmin)
